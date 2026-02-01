import base64
import io
import librosa
import numpy as np
import soundfile as sf

def decode_audio(base64_string: str):
    """
    Decodes a Base64 string into a numpy audio array and sampling rate.
    """
    try:
        # Decode base64 string
        audio_bytes = base64.b64decode(base64_string)
        
        # Load audio from bytes
        # soundfile is robust for reading from memory
        audio_file = io.BytesIO(audio_bytes)
        y, sr = librosa.load(audio_file, sr=None)
        
        return y, sr
    except Exception as e:
        raise ValueError(f"Error decoding audio: {str(e)}")

def extract_features(y, sr):
    """
    Extracts features from the audio signal.
    For a real model, this would match the training preprocessing (e.g., Mel-spectrogram).
    Here we extract some basic features for demonstration/heuristic use.
    """
    # Example: MFCCs (Mel-frequency cepstral coefficients)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)
    
    # Spectral Centroid (often higher in some synthetic speech)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    centroid_mean = np.mean(spectral_centroid)
    
    return {
        "mfcc_mean": mfcc_mean.tolist(),
        "spectral_centroid_mean": float(centroid_mean),
        "duration": float(librosa.get_duration(y=y, sr=sr))
    }
