# app.py
import streamlit as st
from app.ui import render_ui
from app.lyrics_generator import generate_lyrics
from app.music_generator import generate_music
from app.utils import save_temp_audio

def main():
    story, genre, generate = render_ui()

    if generate and story.strip():
        with st.spinner("Generating lyrics..."):
            prompt = {"story": story, "genre": genre}
            lyrics = generate_lyrics(prompt)
            st.subheader("📝 Generated Lyrics")
            st.text(lyrics)

        with st.spinner("Generating instrumental music..."):
            audio_path = generate_music(f"A {genre} beat for a song about {story}")
            audio_data = save_temp_audio(audio_path)

            if audio_data:
                st.subheader("🎧 Instrumental Preview")
                st.audio(audio_data, format='audio/wav')

if __name__ == "__main__":
    main()
