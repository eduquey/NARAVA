# --- COMANDOS PARA EJECUTAR EN VS CODE ---
# 1. Instalar Streamlit: python -m pip install streamlit
# 2. Ejecutar la Web:    python -m streamlit run app.py
# -----------------------------------------------------------------------

import base64
import os

import streamlit as st
import pandas as pd

# Configuración de la página con estilo profesional
st.set_page_config(
    page_title="NARAVA | Consultoría Medioambiental y Seguridad Laboral",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UTILIDADES PARA IMÁGENES ---
def find_image(name):
    base_folder = os.path.dirname(__file__)
    candidates = {
        f"{name}.png",
        f"{name}.jpg",
        f"{name}.jpeg",
    }
    if name == "logo":
        candidates.update({"logo.png", "logo.jpg", "logo.jpeg"})
    existing = {entry.lower(): entry for entry in os.listdir(base_folder)}
    for candidate in candidates:
        match = existing.get(candidate.lower())
        if match:
            return os.path.join(base_folder, match)
    return None

def get_image_base64(path):
    if path and os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

flor_b64 = get_image_base64(find_image("flor"))
logo_b64 = get_image_base64(find_image("logo"))

# --- CSS PROFESIONAL DE ALTA GAMA ---
st.markdown("""
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

/* Limpieza de la interfaz de Streamlit */
.stApp { background-color: var(--bg-light); color: var(--text-main); }
[data-testid="stHeader"], header { display: none !important; }

/* Ajuste de márgenes para control total del diseño */
.main .block-container { 
    padding: 0 !important; 
    max-width: 100% !important;
}

[data-testid="stVerticalBlock"] { gap: 0rem !important; }

/* Tipografía de Lujo */
h1, h2, h3 { 
    font-family: 'Playfair Display', serif !important; 
    color: var(--primary-dark);
}
p, span, div, a, li { 
    font-family: 'Inter', sans-serif !important; 
    line-height: 1.6;
}

/* BARRA DE NAVEGACIÓN ESTÁTICA / FIXED */
.nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 8%;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 85px;
    z-index: 9999;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 2px 20px rgba(0,0,0,0.02);
}

.nav-links { display: flex; gap: 40px; }
.nav-links a {
    text-decoration: none;
    color: var(--primary-dark) !important;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    transition: 0.3s;
}
.nav-links a:hover { color: var(--accent-gold) !important; }

/* HERO SECTION - Refinado */
.hero-section {
    padding-top: 85px; /* Espacio para la nav fija */
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(rgba(18, 35, 21, 0.75), rgba(18, 35, 21, 0.75)), 
                url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2070');
    background-size: cover;
    background-position: center;
    text-align: center;
    color: var(--white);
}

.hero-title {
    font-size: clamp(2.8rem, 5vw, 4.5rem);
    color: var(--white) !important;
    margin-bottom: 25px;
    font-weight: 700;
}

.hero-subtitle {
    font-size: 1.2rem;
    font-weight: 300;
    letter-spacing: 1px;
    margin-bottom: 40px;
    opacity: 0.95;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    color: var(--white) !important;
}

/* SECCIONES - Espacios acordes */
.content-section {
    padding: 100px 10%;
    background-color: var(--white);
}

.label-luxury {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 20px;
    border-bottom: 2px solid var(--accent-gold);
    padding-bottom: 5px;
}

/* TARJETAS DE SERVICIO - Bordes y Sombras Sutiles */
.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px; /* Bordes más rectos y profesionales */
    border: 1px solid #F0F0F0;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    height: 100%;
}
.service-card:hover {
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    border-color: var(--accent-gold);
    transform: translateY(-5px);
}

.service-icon {
    font-size: 2.5rem;
    margin-bottom: 25px;
    display: block;
    color: var(--primary-dark);
}

/* CONTACTO - Fondo Acorde */
.contact-section {
    background-color: var(--primary-dark);
    color: var(--white);
    padding: 100px 10%;
}

.contact-input {
    width: 100%;
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
    padding: 15px !important;
    margin-bottom: 20px !important;
    font-size: 0.9rem;
}

.btn-luxury {
    background: var(--accent-gold) !important;
    color: var(--primary-dark) !important;
    font-weight: 700 !important;
    padding: 18px 45px !important;
    border: none !important;
    letter-spacing: 2px;
    cursor: pointer;
    transition: 0.3s;
    width: 100%;
}

/* WhatsApp */
.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

.logo-image {
    max-width: 500px;
    width: 100%;
    height: auto;
    display: block;
}

.contact-form {
    background: rgba(255,255,255,0.03);
    padding: 50px;
    border-radius: 4px;
    border: 1px solid rgba(255,255,255,0.08);
}

@media (max-width: 1024px) {
    .content-section,
    .contact-section {
        padding: 80px 6%;
    }

    .nav-bar {
        padding: 0 5%;
    }

    .nav-links {
        gap: 24px;
    }

    .service-card {
        padding: 40px 28px;
    }
}

@media (max-width: 768px) {
    .nav-bar {
        height: auto;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        padding: 14px 6%;
    }

    .nav-links {
        flex-wrap: wrap;
        gap: 12px;
        padding-bottom: 10px;
    }

    .nav-links a {
        font-size: 0.72rem;
        letter-spacing: 1px;
    }

    .hero-section {
        padding-top: 140px;
        min-height: auto;
        padding-bottom: 80px;
    }

    .hero-title {
        font-size: clamp(2.2rem, 8vw, 3rem);
    }

    .hero-subtitle {
        font-size: 1rem;
    }

    .content-section,
    .contact-section {
        padding: 70px 6%;
    }

    .service-card {
        padding: 32px 24px;
    }

    .contact-form {
        padding: 30px;
    }

    .wa-btn {
        width: 52px;
        height: 52px;
        right: 20px;
        bottom: 20px;
    }
}

@media (max-width: 480px) {
    .nav-links {
        justify-content: flex-start;
    }

    .hero-section {
        padding-top: 160px;
    }

    .hero-title {
        font-size: 2rem;
    }

    .hero-subtitle {
        font-size: 0.95rem;
    }

    .content-section,
    .contact-section {
        padding: 60px 7%;
    }
}
</style>
""", unsafe_allow_html=True)

# --- WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- NAVBAR ---
logo_html = f'<img src="data:image/png;base64,{flor_b64}" width="40">' if flor_b64 else "🌿"
st.markdown(f"""
<div class="nav-bar">
    <div style="display: flex; align-items: center; gap: 15px;">
        {logo_html}
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
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestion ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
        <a href="#servicios" style="text-decoration:none; color:var(--primary-dark); background:var(--accent-gold); padding:20px 50px; border-radius:4px; font-weight:700; font-size:0.85rem; letter-spacing:2px; display:inline-block;">NUESTROS SERVICIOS</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- ESTRATEGIA / EMPRESA ---
st.markdown('<section id="empresa" class="content-section">', unsafe_allow_html=True)
c_info, c_logo = st.columns([1, 1], gap="large")
with c_info:
    st.markdown("""
    <span class="label-luxury">Visión Estratégica</span>
    <h2 style="font-size: 3.2rem; line-height: 1.1; margin-bottom: 30px;">Solidez Técnica en <br>Cada Decisión</h2>
    <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 25px;">
        En NARAVA S.A.S. transformamos los retos regulatorios en ventajas competitivas. Nuestra metodología integra la ciencia ambiental con la eficiencia operativa.
    </p>
    <ul style="list-style: none; padding: 0; color: var(--text-muted); font-size: 1rem;">
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Cumplimiento normativo riguroso</li>
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Mitigación proactiva de riesgos</li>
        <li><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Sostenibilidad con retorno de inversión</li>
    </ul>
    """, unsafe_allow_html=True)
with c_logo:
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" class="logo-image">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f"""
    <div style="background: #F8F8F8; padding: 0px; display: flex; justify-content: center; align-items: center; border-radius: 0px;">
        {logo_img}
    </div>
    """, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    (
        "Gestión de Calidad",
        "Sistemas de Gestión de Calidad (SGC), aplicable a organizaciones de cualquier tamaño o sector",
        "📈",
    ),
    ("Asesoría Jurídica", "Blindaje legal ambiental para proyectos de gran escala.", "⚖️"),
    ("Diseño Paisajístico", "Fusión de arquitectura y ecosistemas naturales sostenibles.", "🍃"),
    ("Interventoría", "Supervisión técnica de alta precisión en proyectos críticos.", "🏗️")
]

for i in range(0, 6, 3):
    cols = st.columns(3, gap="large")
    for j in range(3):
        idx = i + j
        with cols[j]:
            st.markdown(f"""
            <div class="service-card">
                <span class="service-icon">{serv_data[idx][2]}</span>
                <h3 style="font-size: 1.6rem; margin-bottom:15px;">{serv_data[idx][0]}</h3>
                <p style="color: var(--text-muted); font-size: 0.95rem;">{serv_data[idx][1]}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    # SE ASEGURA COLOR BLANCO EXPLÍCITO PARA EL TEXTO SOBRE FONDO OSCURO
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px; font-family:'Playfair Display', serif;">CONTACTANOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; opacity:0.9; color:white !important;">
        <p style="margin-bottom:15px; color:white !important;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px; color:white !important;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="color:white !important;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div class="contact-form">
        <form action="https://formsubmit.co/gerencianarava@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Nombre y Apellidos" required class="contact-input">
            <input type="email" name="email" placeholder="Correo Corporativo" required class="contact-input">
            <textarea name="message" placeholder="Describa brevemente su requerimiento..." required class="contact-input" style="height:120px;"></textarea>
            <button type="submit" class="btn-luxury">SOLICITAR INFORMACIÓN</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="margin-top:80px; text-align:center; opacity:0.3; font-size:0.7rem; letter-spacing:3px; font-weight:600; color:white !important;">
        NARAVA S.A.S. © 2026 | MEDELLÍN, COLOMBIA
    </div>
</section>
""", unsafe_allow_html=True)

