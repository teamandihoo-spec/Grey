import streamlit as st

# Configuration de la page
st.set_page_config(page_title="GREY - Nu Metal Madagascar", layout="wide")

# Injection du CSS personnalisé
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# Initialisation des données basées strictement sur le PDF
if 'content' not in st.session_state:
    st.session_state.content = {
        "title": "GREY",
        [cite_start]"style": "Nu Metal / Fusion / Rap Metal / Hardcore [cite: 4]",
        [cite_start]"bio_short": "GREY est un quatuor de nu metal malgache né de la rencontre de quatre univers artistiques différents en 2020[cite: 9]. [cite_start]*Slam, rap, rock et metal* s'y mélangent pour donner naissance à une musique **hybride, brute et urgente**[cite: 9].",
        "lineup": """
* [cite_start]**Voix** : RAZAFINDRAIBE Andrianavalona (Navalona) [cite: 6]
* [cite_start]**Guitare** : RAMIZAHERIVELOMALALA Kanto Dina (JT) [cite: 7]
* [cite_start]**Basse** : RASOLONDRAIBE Mandrindra Henintsoa (Mandrindra) [cite: 7]
* [cite_start]**Batterie** : RANAIVOSON Sedraniaina Fanantenana (Nyaina) [cite: 7]
        """,
        [cite_start]"ep_info": "Le 29 mars 2025, GREY a sorti son premier EP intitulé **« MADAFAKA »** en collaboration avec ROXICOMANIA Production[cite: 55].",
        "image_url": "https://images.unsplash.com/photo-1528642466241-001097e30d7b?q=80&w=1000&auto=format&fit=crop" # Image par défaut (style Metal)
    }

# Authentification
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Header avec bouton Admin
col_t, col_a = st.columns([0.85, 0.15])
with col_a:
    if not st.session_state.logged_in:
        if st.button("🔓 Admin Login"):
            st.session_state.show_login = True
    else:
        if st.button("🔒 Déconnexion"):
            st.session_state.logged_in = False
            st.rerun()

# Formulaire de connexion
if st.session_state.get('show_login') and not st.session_state.logged_in:
    with st.sidebar.form("login_form"):
        st.subheader("Accès Administrateur")
        u = st.text_input("Identifiant")
        p = st.text_input("Mot de passe", type="password")
        if st.form_submit_button("Connexion"):
            if u == "admin" and p == "adminpass":
                st.session_state.logged_in = True
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error("Identifiants incorrects")

# --- INTERFACE ADMIN ---
if st.session_state.logged_in:
    st.markdown("### 🛠️ Mode Édition")
    with st.expander("Modifier le contenu de la page"):
        c = st.session_state.content
        new_title = st.text_input("Nom du groupe", c["title"])
        new_style = st.text_input("Style musical", c["style"])
        new_img = st.text_input("URL de l'image (Lien direct)", c["image_url"])
        new_bio = st.text_area("Biographie (Markdown autorisé)", c["bio_short"], height=150)
        new_lineup = st.text_area("Line-up", c["lineup"], height=150)
        new_ep = st.text_area("Info EP", c["ep_info"])
        
        if st.form_submit_button if False else st.button("Mettre à jour la page"):
            st.session_state.content.update({
                "title": new_title, "style": new_style, "image_url": new_img,
                "bio_short": new_bio, "lineup": new_lineup, "ep_info": new_ep
            })
            st.success("Modifications enregistrées !")
            st.rerun()

# --- AFFICHAGE PUBLIC ---
st.markdown(f"<h1 class='main-title'>{st.session_state.content['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>{st.session_state.content['style']}</p>", unsafe_allow_html=True)

c1, c2 = st.columns([0.6, 0.4])

with c1:
    st.image(st.session_state.content["image_url"], use_container_width=True)
    st.markdown("### L'Urgence de s'exprimer")
    st.markdown(st.session_state.content["bio_short"])
    [cite_start]st.info("Porté par la rage et l'espoir de la jeunesse malgache[cite: 10].")

with c2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### ⚡ Membres")
    st.markdown(st.session_state.content["lineup"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💿 Dernier EP")
    st.markdown(st.session_state.content["ep_info"])
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.subheader("📅 Parcours & Actu")
[cite_start]st.write("Le groupe prépare son premier album pour **2026**[cite: 56].")

# Footer
st.markdown("---")
[cite_start]st.markdown("📍 Antananarivo, Madagascar [cite: 3] | [cite_start]📧 greyband261@gmail.com [cite: 137]")
