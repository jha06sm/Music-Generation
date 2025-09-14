# app/utils.py
import os

def save_temp_audio(audio_path):
    if os.path.exists(audio_path):
        with open(audio_path, 'rb') as f:
            return f.read()
    return None
