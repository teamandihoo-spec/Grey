import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS personnalisé
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# Initialisation du contenu basé sur le PDF
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        "style": "Nu Metal / Fusion / Rap Metal / Hardcore",
        "bio": "GREY est un quatuor de nu metal malgache né de la rencontre de quatre univers artistiques différents en 2020. *Slam, rap, rock et metal* s'y mélangent pour donner naissance à une musique **hybride, brute et urgente**.",
        "lineup": "• **Voix** : RAZAFINDRAIBE Andrianavalona (Navalona)\\n• **Guitare** : RAMIZAHERIVELOMALALA Kanto Dina (JT)\\n• **Basse** : RASOLONDRAIBE Mandrindra Henintsoa (Mandrindra)\\n• **Batterie** : RANAIVOSON Sedraniaina Fanantenana (Nyaina)",
        "img_data": None
    }

# Gestion de l'authentification
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Header avec bouton Admin
col_title_space, col_admin_btn = st.columns([0.85, 0.15])
with col_admin_btn:
    if not st.session_state.auth:
        if st.button("🔒 Admin"):
            st.session_state.show_login = True
    else:
        if st.button("🔓 Déconnexion"):
            st.session_state.auth = False
            st.rerun()

# Modal de connexion
if st.session_state.get('show_login') and not st.session_state.auth:
    with st.sidebar.form("login_form"):
        st.subheader("Connexion Admin")
        u = st.text_input("Identifiant")
        p = st.text_input("Mot de passe", type="password")
        if st.form_submit_button("Se connecter"):
            if u == "admin" and p == "adminpass":
                st.session_state.auth = True
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error("Accès refusé")

# --- INTERFACE ADMIN ---
if st.session_state.auth:
    st.markdown("---")
    st.markdown("### 🛠️ Panneau d'administration")
    
    # Zone de téléchargement d'image
    uploaded_file = st.file_uploader("Modifier la photo du groupe (JPG/PNG)", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.session_state.content["img_data"] = uploaded_file.getvalue()
        st.success("Image mise à jour avec succès !")

    # Zone de modification des textes
    with st.form("edit_texts"):
        c = st.session_state.content
        new_title = st.text_input("Nom du groupe", c["title"])
        new_bio = st.text_area("Biographie (Gras ** et Italique * possibles)", c["bio"], height=150)
        new_lineup = st.text_area("Membres (Line-up)", c["lineup"], height=150)
        
        if st.form_submit_button("Enregistrer les modifications"):
            st.session_state.content.update({
                "title": new_title,
                "bio": new_bio,
                "lineup": new_lineup
            })
            st.rerun()

# --- VUE PUBLIQUE ---
st.markdown(f"<h1 class='main-title'>{st.session_state.content['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>{st.session_state.content['style']} | Antananarivo</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 0.4])

with col1:
    if st.session_state.content["img_data"]:
        st.image(st.session_state.content["img_data"], use_container_width=True)
    else:
        st.info("Aucune photo disponible. Utilisez le compte admin pour téléverser une image.")
    
    st.markdown("### 📜 BIOGRAPHIE")
    st.markdown(st.session_state.content["bio"])

with col2:
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("### ⚡ LINE-UP")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("### 💿 DERNIER EP")
    st.markdown("« **MADAFAKA** » (2025)")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("Site officiel basé sur le dossier de presse de GREY.")
