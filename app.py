import streamlit as st
import requests
import base64

# Configuración de la página con estilo profesional
st.set_page_config(
    page_title="NARAVA | Consultoría Medioambiental y Seguridad Laboral",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UTILIDADES PARA IMÁGENES (OPTIMIZADAS PARA GITHUB RAW) ---
def get_image_base64_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except Exception:
        return None
    return None

# URLs de los archivos en el repositorio GitHub
URL_FLOR = "https://raw.githubusercontent.com/eduquey/NARAVA/main/Flor.png"
URL_LOGO = "https://raw.githubusercontent.com/eduquey/NARAVA/main/Logo.png"

flor_b64 = get_image_base64_from_url(URL_FLOR)
logo_b64 = get_image_base64_from_url(URL_LOGO)

# --- CSS PROFESIONAL DE ALTA GAMA ---
# Definimos el CSS en una variable separada para evitar errores de sintaxis en el bloque st.markdown
CUSTOM_CSS = """
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

/* Ajuste de márgenes para el control total del diseño */
.main .block-container { 
    padding: 0 !important; 
    max-width: 100% !important;
}

/* Corrección de espacio vertical: valor numérico simple */
[data-testid="stVerticalBlock"] { 
    gap: 0 !important; 
}

/* Tipografía de Lujo */
h1, h2, h3 { 
    font-family: 'Playfair Display', serif !important; 
    color: var(--primary-dark);
}
p, span, div, a, li { 
    font-family: 'Inter', sans-serif !important; 
    line-height: 1.6;
}

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES ESTILIZADAS */
.social-links {
    display: flex;
    gap: 25px;
    margin-top: 35px;
}
.social-icon {
    color: white;
    opacity: 0.8;
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
    transform: translateY(-3px);
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
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
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank" title="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank" title="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
        <form action="https://formsubmit.co/gerencianarava@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Nombre y Apellidos" required class="contact-input">
            <input type="email" name="email" placeholder="Correo Corporativo" required class="contact-input">
            <button type="submit" class=            <textarea name="message" placeholder="Describa brevemente su requerimiento..." required class="contact-input" style="height:120px;"></textarea>
"btn-luxury">SOLICITAR INFORMACIÓN</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="margin-top:80px; text-align:center; opacity:0.3; font-size:0.7rem; letter-spacing:3px; font-weight:600; color:white !important;">
        NARAVA S.A.S. © 2026 | MEDELLÍN, COLOMBIA
    </div>
</section>
""", unsafe_allow_html=True)@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

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

/* Ajuste de márgenes para el control total del diseño */
.main .block-container { 
    padding: 0 !important; 
    max-width: 100% !important;
}

/* Solución al error de sintaxis: simplificación de la regla gap */
[data-testid="stVerticalBlock"] { 
    gap: 0 !important; 
}

/* Tipografía de Lujo */
h1, h2, h3 { 
    font-family: 'Playfair Display', serif !important; 
    color: var(--primary-dark);
}
p, span, div, a, li { 
    font-family: 'Inter', sans-serif !important; 
    line-height: 1.6;
}

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES ESTILIZADAS */
.social-links {
    display: flex;
    gap: 25px;
    margin-top: 35px;
}
.social-icon {
    color: white;
    opacity: 0.8;
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ---
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

# --- SECCIÓN HERO ---
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank" title="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank" title="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
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
""", unsafe_allow_html=True)@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

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

/* Ajuste de márgenes para el control total del diseño */
.main .block-container { 
    padding: 0 !important; 
    max-width: 100% !important;
}

[data-testid="stVerticalBlock"] { 
    gap: 0px !important; 
}

/* Tipografía de Lujo */
h1, h2, h3 { 
    font-family: 'Playfair Display', serif !important; 
    color: var(--primary-dark);
}
p, span, div, a, li { 
    font-family: 'Inter', sans-serif !important; 
    line-height: 1.6;
}

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES ESTILIZADAS */
.social-links {
    display: flex;
    gap: 25px;
    margin-top: 35px;
}
.social-icon {
    color: white;
    opacity: 0.8;
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ---
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

# --- SECCIÓN HERO ---
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Cumplimiento normativo rigurooso</li>
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Mitigación proactiva de riesgos</li>
        <li><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Sostenibilidad con retorno de inversión</li>
    </ul>
    """, unsafe_allow_html=True)
with c_logo:
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank" title="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank" title="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
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
""", unsafe_allow_html=True)@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

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

/* Ajuste de márgenes para el control total del diseño */
.main .block-container { 
    padding: 0 !important; 
    max-width: 100% !important;
}

[data-testid="stVerticalBlock"] { 
    gap: 0px !important; 
}

/* Tipografía de Lujo */
h1, h2, h3 { 
    font-family: 'Playfair Display', serif !important; 
    color: var(--primary-dark);
}
p, span, div, a, li { 
    font-family: 'Inter', sans-serif !important; 
    line-height: 1.6;
}

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES ESTILIZADAS */
.social-links {
    display: flex;
    gap: 25px;
    margin-top: 35px;
}
.social-icon {
    color: white;
    opacity: 0.8;
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ---
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

# --- SECCIÓN HERO ---
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Cumplimiento normativo rigurooso</li>
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Mitigación proactiva de riesgos</li>
        <li><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Sostenibilidad con retorno de inversión</li>
    </ul>
    """, unsafe_allow_html=True)
with c_logo:
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank" title="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank" title="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
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
""", unsafe_allow_html=True)@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

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

/* Ajuste de márgenes para el control total del diseño */
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

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES ESTILIZADAS */
.social-links {
    display: flex;
    gap: 25px;
    margin-top: 35px;
}
.social-icon {
    color: white;
    opacity: 0.8;
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ---
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

# --- SECCIÓN HERO ---
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Cumplimiento normativo rigurooso</li>
        <li style="margin-bottom: 12px;"><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Mitigación proactiva de riesgos</li>
        <li><span style="color:var(--accent-gold); font-weight:bold; margin-right:10px;">•</span> Sostenibilidad con retorno de inversión</li>
    </ul>
    """, unsafe_allow_html=True)
with c_logo:
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank" title="Instagram">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank" title="LinkedIn">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
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
""", unsafe_allow_html=True)@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

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

/* Ajuste de márgenes para el control total del diseño */
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

/* BARRA DE NAVEGACIÓN FIJA */
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

/* SECCIÓN HERO */
.hero-section {
    padding-top: 85px;
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
    font-size: clamp(2.2rem, 5vw, 4.5rem);
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

.service-card {
    background: var(--white);
    padding: 50px 40px;
    border-radius: 4px;
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

.wa-btn {
    position: fixed; bottom: 40px; right: 40px;
    background: #25D366; width: 65px; height: 65px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); z-index: 9999;
}

/* REDES SOCIALES */
.social-links {
    display: flex;
    gap: 20px;
    margin-top: 30px;
}
.social-icon {
    color: white;
    opacity: 0.7;
    transition: 0.3s;
    text-decoration: none;
}
.social-icon:hover {
    opacity: 1;
    color: var(--accent-gold);
}
</style>
""", unsafe_allow_html=True)

# --- BOTÓN WHATSAPP ---
st.markdown("""
<a href="https://wa.me/573117199811" class="wa-btn" target="_blank">
    <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.406.836 2.946 1.285 4.527 1.285 4.899 0 8.885-3.987 8.888-8.887.001-2.37-.922-4.599-2.598-6.275s-3.906-2.597-6.278-2.597c-4.9 0-8.887 3.987-8.889 8.888-.001 1.517.379 2.998 1.098 4.303l-.403 1.476 1.49-.391zm11.287-5.461c-.304-.152-1.799-.886-2.078-.987-.278-.101-.481-.152-.682.152-.201.304-.777.987-.951 1.189-.174.202-.348.228-.652.076-.304-.151-1.284-.474-2.446-1.511-.904-.806-1.513-1.802-1.69-2.105-.177-.303-.019-.467.133-.617.136-.135.304-.354.456-.531.152-.177.202-.304.304-.506.101-.203.051-.38-.025-.532-.076-.151-.682-1.644-.935-2.251-.246-.591-.497-.511-.682-.511h-.581c-.202 0-.531.076-.81.38-.278.303-1.062 1.037-1.062 2.529 0 1.492 1.087 2.934 1.239 3.136.152.202 2.14 3.268 5.183 4.579.724.312 1.29.499 1.731.639.728.231 1.39.198 1.912.12.583-.088 1.799-.734 2.052-1.442.253-.708.253-1.316.177-1.442-.076-.126-.278-.202-.582-.354z"/></svg>
</a>
""", unsafe_allow_html=True)

# --- BARRA DE NAVEGACIÓN ---
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

# --- SECCIÓN HERO ---
st.markdown(f"""
<div id="inicio" class="hero-section">
    <div style="padding: 0 10%;">
        <h1 class="hero-title">Consultoría Técnica de <br>Ingeniería Ambiental y SST</h1>
        <p class="hero-subtitle">Optimizamos la operatividad de su empresa mediante gestión ambiental especializada y sistemas de seguridad laboral de alto rendimiento.</p>
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
    logo_img = f'<img src="data:image/png;base64,{logo_b64}" style="max-width:500px;">' if logo_b64 else "<h2>NARAVA</h2>"
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center;">{logo_img}</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown('<section id="servicios" class="content-section" style="background: #FDFDFD; border-top: 1px solid #EEE;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; margin-bottom:70px;"><span class="label-luxury">Portafolio Especializado</span><h2 style="font-size:3rem;">Nuestros Servicios</h2></div>', unsafe_allow_html=True)

serv_data = [
    ("Gestión Ambiental", "Tramitología especializada ante autoridades regionales y nacionales.", "🌿"),
    ("Seguridad Laboral", "Sistemas SG-SST enfocados en la protección del capital humano.", "🛡️"),
    ("Sostenibilidad ESG", "Estrategias de impacto ambiental, social y de gobernanza.", "📈"),
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
st.markdown('</section>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<section id="contacto" class="contact-section">', unsafe_allow_html=True)
con1, con2 = st.columns([1, 1], gap="large")
with con1:
    st.markdown("""
    <h2 style="color:white !important; font-size:3.5rem; line-height:1; margin-bottom:30px;">CONTÁCTENOS</h2>
    <p style="color:white !important; opacity:0.8; font-size:1.1rem; margin-bottom:40px;">Nuestros consultores expertos están listos para analizar su caso.</p>
    <div style="font-size:1rem; color:white !important;">
        <p style="margin-bottom:15px;"><b>DIRECCIÓN:</b> Medellín, Antioquia.</p>
        <p style="margin-bottom:15px;"><b>CORREO:</b> gerencianarava@gmail.com</p>
        <p style="margin-bottom:15px;"><b>TELÉFONO:</b> +57 311 719 9811</p>
    </div>
    <div class="social-links">
        <a href="https://www.instagram.com/narava.amb" class="social-icon" target="_blank">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="https://www.linkedin.com/company/naravaservicios" class="social-icon" target="_blank">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://facebook.com" class="social-icon" target="_blank">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
with con2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.03); padding: 50px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.08);">
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





