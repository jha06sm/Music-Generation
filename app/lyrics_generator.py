from transformers import pipeline

# Force PyTorch (not TensorFlow)
generator = pipeline("text-generation", model="gpt2", framework="pt")


def generate_lyrics(prompt, max_length=150):
    """
    Generate lyrics from user input.
    """
    prompt = f"Write a {prompt['genre']} style song about: {prompt['story']}"
    lyrics = generator(prompt, max_length=max_length, num_return_sequences=1)[0]["generated_text"]
    return lyrics.strip()
