# app/music_generator.py
import torchaudio
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import torch

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

model.to("cpu")  # or 'cuda' if you’re using Colab with GPU

def generate_music(description, output_path="output_song.wav"):
    inputs = processor(
        text=[description],
        padding=True,
        return_tensors="pt"
    )
    audio_values = model.generate(**inputs, max_new_tokens=1500)
    sampling_rate = model.config.audio_encoder.sampling_rate

    torchaudio.save(output_path, audio_values[0].cpu(), sampling_rate, format="wav")

    return output_path
