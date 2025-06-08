import json
import streamlit as st
from main import generiere_reflexion

# Begriffs-Datenbank beim Start laden
with open("begriffs_datenbank.json", "r", encoding="utf-8") as f:
    datenbank = json.load(f)

# Mapping von Begriff zu Datenbankeintrag erstellen
begriffe_map = {eintrag["begriff"]: eintrag for eintrag in datenbank.values()}

st.title("Limitologisches Denklabor")

begriff = st.text_input("Begriff eingeben:")

# Dropdown-Menü mit allen Begriffen aus der Datenbank
auswahl = st.selectbox(
    "Begriff aus der Datenbank wählen:",
    [""] + sorted(begriffe_map.keys()),
)

if auswahl:
    eintrag = begriffe_map[auswahl]
    st.subheader(auswahl)
    st.markdown(f"**Zitat:** {eintrag['zitat']}")
    st.markdown(f"**Kontext:** {eintrag['kontext']}")
    st.markdown(f"**Quelle:** {eintrag['quelle']}")

if st.button("Reflektieren"):
    if begriff:
        st.write(generiere_reflexion(begriff))
    else:
        st.write("Bitte gib einen Begriff ein.")
