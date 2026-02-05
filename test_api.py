import requests
import base64
import numpy as np
import soundfile as sf
import io
import json

def create_dummy_audio_base64():
    """
    Generate a test audio file (1 second sine wave at 440Hz) encoded as base64.
    """
    sr = 22050
    t = np.linspace(0, 1, sr)
    # 440Hz sine wave
    audio = 0.5 * np.sin(2 * np.pi * 440 * t)
    
    # Save to memory buffer as WAV format
    buffer = io.BytesIO()
    sf.write(buffer, audio, sr, format='WAV')
    buffer.seek(0)
    
    # Encode to base64
    audio_b64 = base64.b64encode(buffer.read()).decode('utf-8')
    return audio_b64

def test_detection(language="English", port=8000, timeout=60):
    url = f"http://localhost:{port}/detect"
    
    print("Generating dummy audio...")
    try:
        audio_b64 = create_dummy_audio_base64()
    except Exception as e:
        print(f"Error creating audio: {e}")
        return

    payload = {
        "audio_base64": audio_b64,
        "language": language
    }
    
    print(f"Sending request to {url} with language={language}...")
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response JSON:")
            print(json.dumps(response.json(), indent=2))
        else:
            print("Error Response:")
            print(response.text)
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    import sys
    lang = "English"
    if len(sys.argv) > 1:
        lang = sys.argv[1]
    test_detection(language=lang)
