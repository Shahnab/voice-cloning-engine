import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide", theme=light)

st.sidebar.image("https://static.thenounproject.com/png/821139-200.png", width=100)
st.subheader("About Voice Cloning")
st.markdown("##### Voice cloning is the name of the process that allows artificial intelligence to create a cloned or copied version of a natural human voice")

st.sidebar.subheader("How to use the Voice Cloning Engine")
st.sidebar.markdown("##### 1. Input text you want to create")
st.sidebar.markdown("##### 2. Upload sample voice or record from the microphone")
st.sidebar.markdown("##### 3. Click Submit")
st.sidebar.markdown("Sample Voice Samples for uploading- [link](https://drive.google.com/drive/folders/1VT3QOnl9E3_OEelNOCp2BqcFs2dJ68ju?usp=sharing)")


st.sidebar.caption("</Shahnab>")

st.subheader("Voice Cloning Engine")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-voice-cloning.hf.space", width=1100, height=650, scrolling=True)
