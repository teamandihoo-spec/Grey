import streamlit as st

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS personnalisé
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# [cite_start]Initialisation des données (Contenu basé sur le document PDF) [cite: 1, 2, 4]
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        "bio_short": "**GREY** est un quatuor de nu metal malgache né de la rencontre de quatre univers artistiques différents en 2020. *Slam, rap, rock et metal* s'y mélangent pour donner naissance à une musique hybride.",
        "lineup": """
        * [cite_start]**Voix** : RAZAFINDRAIBE Andrianavalona (Navalona) [cite: 6]
        * [cite_start]**Guitare** : RAMIZAHERIVELOMALALA Kanto Dina (JT) [cite: 7]
        * [cite_start]**Basse** : RASOLONDRAIBE Mandrindra Henintsoa (Mandrindra) [cite: 7]
        * [cite_start]**Batterie** : RANAIVOSON Sedraniaina Fanantenana (Nyaina) [cite: 7]
        """,
        [cite_start]"style": "Nu Metal / Fusion / Rap Metal / Hardcore [cite: 4]",
        [cite_start]"ep_info": "Le 29 mars 2025, GREY a sorti son premier EP intitulé **« MADAFAKA »**[cite: 55].",
        "image_url": "https://via.placeholder.com/800x400.png?text=GREY+MADAFAKA" 
    }

# Gestion de l'authentification
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Barre de navigation / En-tête
col_title, col_admin = st.columns([0.9, 0.1])
with col_admin:
    if not st.session_state.logged_in:
        if st.button("Admin"):
            st.session_state.show_login = True
    else:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

# Fenêtre de connexion
if st.session_state.get('show_login') and not st.session_state.logged_in:
    with st.form("login_form"):
        u = st.text_input("Identifiant")
        p = st.text_input("Mot de passe", type="password")
        if st.form_submit_button("Se connecter"):
            if u == "admin" and p == "adminpass":
                st.session_state.logged_in = True
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error("Identifiants incorrects")

# --- VUE ADMINISTRATEUR ---
if st.session_state.logged_in:
    st.title("🔧 Panneau d'administration")
    with st.expander("Modifier les textes et l'image"):
        new_title = st.text_input("Nom du groupe", st.session_state.content["title"])
        new_style = st.text_input("Style musical", st.session_state.content["style"])
        new_bio = st.text_area("Biographie courte (Markdown supporté)", st.session_state.content["bio_short"])
        new_lineup = st.text_area("Line-up", st.session_state.content["lineup"])
        new_ep = st.text_area("Infos EP", st.session_state.content["ep_info"])
        new_img = st.text_input("URL de l'image principale", st.session_state.content["image_url"])
        
        if st.button("Sauvegarder les modifications"):
            st.session_state.content.update({
                "title": new_title, "style": new_style, "bio_short": new_bio,
                "lineup": new_lineup, "ep_info": new_ep, "image_url": new_img
            })
            st.success("Contenu mis à jour !")
    st.divider()

# --- VUE PUBLIQUE ---
st.markdown(f"<h1 class='main-title'>{st.session_state.content['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>{st.session_state.content['style']}</p>", unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.image(st.session_state.content["image_url"], use_container_width=True)
    st.markdown("### À propos")
    st.markdown(st.session_state.content["bio_short"])

with col2:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("### Line-up")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("### Dernier Projet")
    st.markdown(st.session_state.content["ep_info"])
    st.markdown("</div>", unsafe_allow_html=True)

# Section Parcours (Lecture seule - PDF)
st.divider()
st.subheader("🚀 Parcours Scénique")
[cite_start]st.write("Le groupe s'est illustré sur de nombreuses scènes comme le DAGO MADNESS BEATZ ou en première partie de THE DIZZY BRAINS[cite: 74, 81, 89].")

# Pied de page
st.markdown("---")
[cite_start]st.markdown("📩 **Contact:** greyband261@gmail.com | 📞 +261 32 35 507 78 [cite: 135, 137]")
