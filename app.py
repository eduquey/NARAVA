 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/app.py b/app.py
index 25ad222689304dd0904b12bbe78c5df19ee45d30..1090cc712615c83554d53a186d03c076678180b9 100644
--- a/app.py
+++ b/app.py
@@ -1,54 +1,60 @@
 # --- COMANDOS PARA EJECUTAR EN VS CODE ---
 # 1. Instalar Streamlit: python -m pip install streamlit
 # 2. Ejecutar la Web:    python -m streamlit run app.py
 # -----------------------------------------------------------------------
 
-import streamlit as st
-import pandas as pd
-import os
+import base64
+import os
+
+import streamlit as st
+import pandas as pd
 
 # Configuración de la página con estilo profesional
 st.set_page_config(
     page_title="NARAVA | Consultoría Medioambiental y Seguridad Laboral",
     page_icon="🌿",
     layout="wide",
     initial_sidebar_state="collapsed"
 )
 
 # --- UTILIDADES PARA IMÁGENES ---
-def find_image(name):
-    base_folder = r"C:\Users\LENOVO\OneDrive\Escritorio\NARAVA\Proyecto_Narava"
-    paths = [
-        os.path.join(base_folder, f"{name}.png"),
-        os.path.join(base_folder, f"{name}.jpg"),
-        os.path.join(base_folder, "logo.png") if name == "logo" else None
-    ]
-    for path in paths:
-        if path and os.path.exists(path):
-            return path
-    return None
+def find_image(name):
+    base_folder = os.path.dirname(__file__)
+    candidates = {
+        f"{name}.png",
+        f"{name}.jpg",
+        f"{name}.jpeg",
+    }
+    if name == "logo":
+        candidates.update({"logo.png", "logo.jpg", "logo.jpeg"})
+    existing = {entry.lower(): entry for entry in os.listdir(base_folder)}
+    for candidate in candidates:
+        match = existing.get(candidate.lower())
+        if match:
+            return os.path.join(base_folder, match)
+    return None
 
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
 
EOF
)
