# app/ui.py
import streamlit as st

def render_ui():
    st.title("🎧 SongTeller AI")
    st.markdown("Turn your stories or emotions into a song!")

    story = st.text_area("📝 Enter your story, message or idea:")
    genre = st.selectbox("🎶 Choose a genre", ["lo-fi", "rap", "romantic", "sad", "EDM"])
    generate = st.button("🎤 Generate Song")

    return story, genre, generate
