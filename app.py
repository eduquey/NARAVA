# --- COMANDOS PARA EJECUTAR EN VS CODE ---
# 1. Instalar Streamlit: python -m pip install streamlit
# 2. Ejecutar la Web:    python -m streamlit run app.py
# -----------------------------------------------------------------------

import streamlit as st
import base64
import os

# Configuración de la página
st.set_page_config(
    page_title="NARAVA | Consultoría Medioambiental y Seguridad Laboral",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UTILIDADES PARA IMÁGENES LOCALES ---
def find_image(name):
    # Ruta absoluta basada en tu configuración local
    base_folder = r"C:\Users\LENOVO\OneDrive\Escritorio\NARAVA\Proyecto_Narava"
    paths = [
        os.path.join(base_folder, f"{name}.png"),
        os.path.join(base_folder, f"{name}.jpg"),
        os.path.join(base_folder, "logo.png") if name == "logo" else None
    ]
    for path in paths:
        if path and os.path.exists(path):
            return path
    return None

def get_image_base64(path):
    if path and os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception:
            return None
    return None

# Carga de imágenes (Solo se ejecutan una vez)
ruta_flor = find_image("flor")
ruta_logo = find_image("logo")
flor_b64 = get_image_base64(ruta_flor)
logo_b64 = get_image_base64(ruta_logo)

# --- CSS PROFESIONAL ---
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

:root {
    --primary-dark: #122315;
    --accent-gold: #B89352;
    --bg-light: #FDFDFD;
    --text-main: #1A1A1A;
    --text-muted: #4A4A4A;
    --white: #FFFFFF;
}

.stApp { background-color: var(--bg-light); color: var(--text-main); }
[data-testid="stHeader"], header { display: none !important; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stVerticalBlock"] { gap: 0rem !important; }

h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: var(--primary-dark); }
p, span, div, a, li { font-family: 'Inter', sans-serif !important; line-height: 1.6; }

.nav-bar {
    display: flex; justify-content: space-between; align-items: center;
    padding: 0 8%; background: rgba(255, 255, 255, 0.95);
    position: fixed; top: 0; left: 0; width: 100%; height: 85px;
    z-index: 9999; border-bottom: 1px solid rgba(0,0,0,0.06);
}

.nav-links { display: flex; gap: 40px; }
.nav-links a {
    text-decoration: none; color: var(--primary-dark) !important;
    font-size: 0.8rem; font-weight: 600; letter-spacing: 1.5px;
}

.hero-section {
    padding-top: 85px; min-height: 90vh; display: flex; align-items: center; justify-content: center;
    background: linear-gradient(rgba(18, 35, 21, 0.75), rgba(18, 35, 21, 0.75)), 
                url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2070');
    background-size: cover; background-position: center; text-align: center; color: var(--white);
}

.hero-title { font-size: clamp(2.8rem, 5vw, 4.5rem); color: var(--white) !important; font-weight: 700; }
.hero-subtitle { font-size: 1.2rem; margin-bottom: 40px; color: var(--white) !important; }

.content-section { padding: 100px 10%; background-color: var(--white); }
.label-luxury {
    display: inline-block; font-size: 0.75rem; font-weight: 600; letter-spacing: 4px;
    text-transform: uppercase; color: var(--accent-gold); border-bottom: 2px solid var(--accent-gold); padding-bottom: 5px;
}

.service-card {
    background: var(--white); padding: 50px 40px; border-radius: 4px; border: 1px solid #F0F0F0;
    transition: 0.4s; height: 100%;
}
.service-card:hover { border-color: var(--accent-gold); transform: translateY(-5px); }

.contact-section { background-color: var(--primary-dark); color: var(--white); padding: 100px 10%; }
.contact-input {
    width: 100%; background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important; padding: 15px !important; margin-bottom: 20px !important;
}

.btn-luxury {
    background: var(--accent-gold) !important; color: var(--primary-dark) !important;
    font-weight: 700 !important; padding: 18px 45px !important; border: none !important; width: 100%;
}

.wa-btn {
    position: fixed; bottom: 40px; right: 40px; background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- NAVBAR ---
logo_nav = f'<img src="data:image/png;base64,{flor_b64}" width="40">' if flor_b64 else "🌿"
st.markdown(f"""
<div class="nav-bar">
    <div style="display: flex; align-items: center; gap: 15px;">
        {logo_nav}
        <span style="font-family:'Playfair Display'; font-size: 1.6rem; font-weight:700; color:var(--primary-dark); letter-spacing:1px;">NARAVA</span>
    </div>
    <div class="nav-links">
        <a href="#inicio">INICIO</a>
        <a href="#empresa">ESTRATEGIA</a>
        <a href="#servicios">SERVICIOS</a>
        <a href="#contacto">CONTACTO</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral.</p>
        <a href="#servicios" style="text-decoration:none; color:var(--primary-dark); background:var(--accent-gold); padding:20px 50px; border-radius:4px; font-weight:700; font-size:0.85rem; letter-spacing:2px; display:inline-block;">NUESTROS SERVICIOS</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- ESTRATEGIA ---
st.markdown('<section id="empresa" class="content-section">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1], gap="large")
with c1:
    st.markdown("""
    <span class="label-luxury">Visión Estratégica</span>
    <h2 style="font-size: 3.2rem; line-height: 1.1; margin-bottom: 30px;">Solidez Técnica en <br>Cada Decisión</h2>
    <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 25px;">
        En NARAVA S.A.S. transformamos los retos regulatorios en ventajas competitivas integrando ciencia ambiental y eficiencia.
    </p>
    """, unsafe_allow_html=True)
with c2:
    logo_main = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="text-align: center;">{logo_main}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio</span><h2>Nuestros Servicios</h2></div>', unsafe_allow_html=True)

servicios = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST de alto impacto.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto social y ambiental.", "📈"),
    ("Asesoría Jurídica", "Blindaje legal ambiental especializado.", "⚖️"),
    ("Diseño Paisajístico", "Arquitectura y ecosistemas sostenibles.", "🍃"),
    ("Interventoría", "Supervisión técnica de alta precisión.", "🏗️")
]

for i in range(0, 6, 3):
    cols = st.columns(3, gap="large")
    for j in range(3):
        idx = i + j
        with cols[j]:
            st.markdown(f"""
            <div class="service-card">
                <span class="service-icon">{servicios[idx][2]}</span>
                <h3>{servicios[idx][0]}</h3>
                <p style="color: var(--text-muted);">{servicios[idx][1]}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('<div style="height:30px;"></div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem;">CONTÁCTANOS</h2>
    <p style="color:white !important; opacity:0.8;">Expertos listos para analizar su caso.</p>
    <div style="color:white !important; margin-top:30px;">
        <p><b>MEDELLÍN, COLOMBIA</b></p>
        <p>gerencianarava@gmail.com</p>
        <p>+57 311 719 9811</p>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 40px; border: 1px solid rgba(255,255,255,0.1);">
        <form action="https://formsubmit.co/gerencianarava@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Nombre completo" required class="contact-input">
            <input type="email" name="email" placeholder="Email corporativo" required class="contact-input">
            <textarea name="message" placeholder="Mensaje..." required class="contact-input" style="height:100px;"></textarea>
            <button type="submit" class="btn-luxury">ENVIAR</button>
        </form>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)
