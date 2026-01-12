import streamlit as st

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# Initialisation des données (Source: GREY - Bio & Parcours.pdf)
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        "style": "Nu Metal / Fusion / Rap Metal / Hardcore",
        "bio": "GREY est un quatuor de nu metal malgache né de la rencontre de quatre univers artistiques différents en 2020[cite: 9]. Slam, rap, rock et metal s'y mélangent pour donner naissance à une musique hybride, brute et urgente[cite: 9].",
        "lineup": "• **Voix** : RAZAFINDRAIBE Andrianavalona (Navalona) [cite: 6]\\n• **Guitare** : RAMIZAHERIVELOMALALA Kanto Dina (JT) [cite: 7]\\n• **Basse** : RASOLONDRAIBE Mandrindra Henintsoa (Mandrindra) [cite: 7]\\n• **Batterie** : RANAIVOSON Sedraniaina Fanantenana (Nyaina) [cite: 7]",
        "img_data": None
    }

# Authentification
if 'auth' not in st.session_state:
    st.session_state.auth = False

# Barre de navigation discrète
nav_col1, nav_col2 = st.columns([0.9, 0.1])
with nav_col2:
    if not st.session_state.auth:
        if st.button("🔒 Admin"):
            st.session_state.show_login = True
    else:
        if st.button("🔓 Quitter"):
            st.session_state.auth = False
            st.rerun()

# Connexion Admin
if st.session_state.get('show_login') and not st.session_state.auth:
    with st.sidebar.form("login"):
        u = st.text_input("Identifiant")
        p = st.text_input("Mot de passe", type="password")
        if st.form_submit_button("Entrer"):
            if u == "admin" and p == "adminpass":
                st.session_state.auth = True
                st.session_state.show_login = False
                st.rerun()

# --- ESPACE ADMIN ---
if st.session_state.auth:
    st.markdown("### 🛠️ Gestion du site")
    with st.expander("Modifier les informations"):
        up = st.file_uploader("Téléverser la photo du groupe", type=["jpg", "png", "jpeg"])
        if up: st.session_state.content["img_data"] = up.getvalue()
        
        st.session_state.content["title"] = st.text_input("Nom du groupe", st.session_state.content["title"])
        st.session_state.content["bio"] = st.text_area("Biographie (Markdown possible)", st.session_state.content["bio"])
        st.session_state.content["lineup"] = st.text_area("Membres", st.session_state.content["lineup"])
        if st.button("Sauvegarder"): st.rerun()

# --- DESIGN PUBLIC ---

# Section Hero
st.markdown(f"""
    <div class='hero'>
        <img src="assets/logo.png" class="logo" alt="GREY logo">
        <p class='subtitle'>{st.session_state.content['style']} | Antananarivo, Madagascar [cite: 3]</p>
    </div>
""", unsafe_allow_html=True)

# Section Contenu
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    if st.session_state.content["img_data"]:
        st.image(st.session_state.content["img_data"], use_container_width=True)
    else:
        st.markdown("<div class='placeholder'>PHOTO DU GROUPE</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("### ⚡ BIOGRAPHIE")
    st.markdown(st.session_state.content["bio"])
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### LINE-UP")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444;'>Nu Metal Made in Mada | 2026</p>", unsafe_allow_html=True)
