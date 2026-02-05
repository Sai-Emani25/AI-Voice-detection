import base64
import io
import numpy as np
import soundfile as sf
import wave
import struct

def decode_audio(base64_string: str):
    """
    Decodes a Base64 string into a numpy audio array and sampling rate.
    """
    # Decode base64 string
    audio_bytes = base64.b64decode(base64_string)
    audio_file = io.BytesIO(audio_bytes)
    # Try reading with soundfile (supports many formats on libsndfile)
    try:
        y, sr = sf.read(audio_file, always_2d=False)
        # ensure mono
        if isinstance(y, np.ndarray) and y.ndim > 1:
            y = np.mean(y, axis=1)
        return y.astype(np.float32), int(sr)
    except Exception:
        # Fallback: try WAV via built-in wave module
        try:
            audio_file.seek(0)
            with wave.open(audio_file, "rb") as wf:
                sr = wf.getframerate()
                n_frames = wf.getnframes()
                n_channels = wf.getnchannels()
                sampwidth = wf.getsampwidth()
                frames = wf.readframes(n_frames)
                # Convert bytes to numpy array
                fmt_char = {1: 'b', 2: 'h', 4: 'i'}.get(sampwidth)
                if not fmt_char:
                    raise ValueError("Unsupported sample width")
                fmt = f"<{n_frames * n_channels}{fmt_char}"
                data = struct.unpack(fmt, frames)
                y = np.array(data, dtype=np.float32)
                if n_channels > 1:
                    y = y.reshape(-1, n_channels).mean(axis=1)
                # Normalize based on bit depth
                max_val = float(2 ** (8 * sampwidth - 1))
                y = y / max_val
                return y, sr
        except Exception as e:
            raise ValueError(f"Unsupported or unreadable audio format: {str(e)}")

def extract_features(y, sr):
    """
    Extracts features from the audio signal for AI voice detection.
    Returns features that are analyzed by Gemini AI.
    """
    # Basic feature set implemented using numpy
    y = np.asarray(y, dtype=np.float32)
    duration = float(len(y) / sr) if sr else 0.0
    
    # RMS energy
    rms_mean = float(np.sqrt(np.mean(y ** 2))) if y.size else 0.0
    
    # Zero crossing rate
    zero_crossing_rate_mean = float(np.mean(np.abs(np.diff(np.sign(y)))) / 2.0) if y.size else 0.0
    
    # Spectral features
    if y.size:
        # Use a window to avoid edge artifacts
        win = min(len(y), 2048)
        segment = y[:win]
        window = np.hanning(win)
        segment = segment * window
        spectrum = np.abs(np.fft.rfft(segment))
        freqs = np.fft.rfftfreq(win, d=1.0 / sr) if sr else np.arange(len(spectrum))
        
        # Spectral centroid
        if spectrum.sum() > 0:
            spectral_centroid_mean = float((freqs * spectrum).sum() / spectrum.sum())
        else:
            spectral_centroid_mean = 0.0
        
        # Spectral rolloff (frequency below which 85% of energy is contained)
        cumsum = np.cumsum(spectrum)
        rolloff_threshold = 0.85 * cumsum[-1]
        rolloff_idx = np.where(cumsum >= rolloff_threshold)[0]
        spectral_rolloff_mean = float(freqs[rolloff_idx[0]]) if len(rolloff_idx) > 0 else 0.0
    else:
        spectral_centroid_mean = 0.0
        spectral_rolloff_mean = 0.0
    
    return {
        "rms_mean": rms_mean,
        "zero_crossing_rate_mean": zero_crossing_rate_mean,
        "spectral_centroid_mean": spectral_centroid_mean,
        "spectral_rolloff_mean": spectral_rolloff_mean,
        "duration": duration
    }
