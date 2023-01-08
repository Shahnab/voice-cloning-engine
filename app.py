import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://static.thenounproject.com/png/821139-200.png", width=100)
st.sidebar.subheader("About Voice Cloning")
st.sidebar.markdown("##### Voice cloning is the name of the process that allows artificial intelligence to create a cloned or copied version of a natural human voice")

st.sidebar.subheader("How to use the Voice Cloning Engine")
st.sidebar.markdown("##### Input text you want to create and upload sample voice to clone the text voice sample")

st.sidebar.caption("</Shahnab>")

st.subheader("Voice Cloning Engine")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-voice-cloning.hf.space", width=1100, height=650, scrolling=True)