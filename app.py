import streamlit as st
from main import generiere_reflexion

st.title("Limitologisches Denklabor")

begriff = st.text_input("Begriff eingeben:")

if st.button("Reflektieren"):
    if begriff:
        st.write(generiere_reflexion(begriff))
    else:
        st.write("Bitte gib einen Begriff ein.")
