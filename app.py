import streamlit as st

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS pour le look Nu Metal
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# Initialisation du contenu (Données extraites du PDF)
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        "style": "Nu Metal / Fusion / Rap Metal / Hardcore",
        "origin": "Antananarivo, Madagascar",
        "bio": "GREY est un quatuor de nu metal malgache né en **2020**. Slam, rap, rock et metal s'y mélangent pour donner naissance à une musique *hybride, brute et urgente*.",
        "lineup": "• **Voix** : Navalona\\n• **Guitare** : JT\\n• **Basse** : Mandrindra\\n• **Batterie** : Nyaina",
        "img_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=1000" # Image par défaut
    }

# Système d'authentification simple
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Barre de navigation haute
col_space, col_btn = st.columns([0.85, 0.15])
with col_btn:
    if not st.session_state.auth:
        if st.button("🔑 Admin"):
            st.session_state.show_login = True
    else:
        if st.button("🚪 Déconnexion"):
            st.session_state.auth = False
            st.rerun()

# Fenêtre de login
if st.session_state.get('show_login') and not st.session_state.auth:
    with st.sidebar.form("login"):
        user = st.text_input("ID")
        pwd = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if user == "admin" and pwd == "adminpass":
                st.session_state.auth = True
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error("Échec")

# --- INTERFACE ADMINISTRATEUR ---
if st.session_state.auth:
    st.markdown("### 🛠️ Panneau de modification")
    with st.expander("Modifier les textes et l'image"):
        c = st.session_state.content
        st.session_state.content["title"] = st.text_input("Nom du groupe", c["title"])
        st.session_state.content["style"] = st.text_input("Style", c["style"])
        st.session_state.content["img_url"] = st.text_input("Lien de l'image (URL)", c["img_url"])
        st.session_state.content["bio"] = st.text_area("Biographie (Markdown autorisé)", c["bio"])
        st.session_state.content["lineup"] = st.text_area("Line-up (Membres)", c["lineup"])
        if st.button("Enregistrer"):
            st.success("Mise à jour effectuée !")
            st.rerun()

# --- AFFICHAGE PUBLIC ---
# Titre et Style
st.markdown(f"<h1 class='hero-title'>{st.session_state.content['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='hero-subtitle'>{st.session_state.content['style']} | {st.session_state.content['origin']}</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.image(st.session_state.content["img_url"], use_container_width=True)
    st.markdown("### 📜 BIOGRAPHIE")
    st.markdown(st.session_state.content["bio"])

with col2:
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    st.markdown("### ⚡ LINE-UP")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='dark-card'>", unsafe_allow_html=True)
    st.markdown("### 💿 DERNIER PROJET")
    st.write("EP **MADAFAKA** sorti le 29 mars 2025.")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.caption("© 2026 GREY - Nu Metal Made in Mada")
