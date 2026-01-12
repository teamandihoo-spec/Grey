import streamlit as st
from PIL import Image
import io

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# Initialisation du contenu
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        [cite_start]"style": "Nu Metal / Fusion / Rap Metal / Hardcore [cite: 4]",
        [cite_start]"origin": "Antananarivo, Madagascar [cite: 3]",
        [cite_start]"bio": "GREY est un quatuor de nu metal malgache né en **2020**[cite: 4, 9]. [cite_start]*Slam, rap, rock et metal* s'y mélangent pour donner naissance à une musique **hybride, brute et urgente**[cite: 9].",
        [cite_start]"lineup": "• **Voix** : Navalona [cite: 6][cite_start]\\n• **Guitare** : JT [cite: 7][cite_start]\\n• **Basse** : Mandrindra [cite: 7][cite_start]\\n• **Batterie** : Nyaina [cite: 7]",
        "img_data": None  # Stockera l'image téléversée
    }

# Authentification
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Header
col_space, col_btn = st.columns([0.85, 0.15])
with col_btn:
    if not st.session_state.auth:
        if st.button("🔑 Admin"):
            st.session_state.show_login = True
    else:
        if st.button("🚪 Déconnexion"):
            st.session_state.auth = False
            st.rerun()

if st.session_state.get('show_login') and not st.session_state.auth:
    with st.sidebar.form("login"):
        u = st.text_input("ID")
        p = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if u == "admin" and p == "adminpass":
                st.session_state.auth = True
                st.session_state.show_login = False
                st.rerun()

# --- INTERFACE ADMIN ---
if st.session_state.auth:
    st.markdown("### 🛠️ Panneau d'administration")
    with st.expander("Modifier le contenu et l'image"):
        # Téléversement de la photo
        uploaded_file = st.file_uploader("Téléverser une nouvelle photo du groupe", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            # Conversion en octets pour stockage en session
            st.session_state.content["img_data"] = uploaded_file.getvalue()
            st.success("Image chargée avec succès !")

        # Modification des textes
        c = st.session_state.content
        st.session_state.content["title"] = st.text_input("Nom du groupe", c["title"])
        st.session_state.content["bio"] = st.text_area("Biographie (Gras ** et Italique * possibles)", c["bio"])
        st.session_state.content["lineup"] = st.text_area("Membres", c["lineup"])
        
        if st.button("Sauvegarder tout"):
            st.rerun()

# --- AFFICHAGE PUBLIC ---
st.markdown(f"<h1 class='hero-title'>{st.session_state.content['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='hero-subtitle'>{st.session_state.content['style']}</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 0.4])

with col1:
    if st.session_state.content["img_data"]:
        st.image(st.session_state.content["img_data"], use_container_width=True)
    else:
        # Image par défaut si rien n'est téléversé
        st.warning("Aucune photo téléversée. Connectez-vous en admin pour en ajouter une.")
    
    st.markdown("### 📜 BIOGRAPHIE")
    st.markdown(st.session_state.content["bio"])

with col2:
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    st.markdown("### ⚡ LINE-UP")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
[cite_start]st.caption("Données extraites du document officiel GREY - Bio & Parcours [cite: 1, 2]")
