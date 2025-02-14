import streamlit as st

st.set_page_config(page_title="Ciencia y Tecnología", layout="wide")

# Cargar un logo pequeño en la parte superior izquierda
logo_top_path = "SV_insignia.png"  # Asegúrate de subir este archivo al mismo directorio que el script
col1, col2 = st.columns([1, 10])
with col1:
    st.image(logo_top_path, width=200)
with col2:
    st.title("Ciencia y Tecnología")

st.sidebar.title("Menú")
seccion = st.sidebar.selectbox("Selecciona una sección", ["Inicio", "Química", "Física", "Biología", "Calendario", "Útiles Escolares"])

# Diccionario de imágenes para cada sección en la barra lateral
imagenes = {
    "Inicio": "inicio.jpg",
    "Química": "quimica.jpg",
    "Física": "fisica.jpg",
    "Biología": "biologia.jpg",
    "Calendario": "calendario.jpg",
    "Útiles Escolares": "materiales.jpg"
}

# Mostrar imagen correspondiente a la sección seleccionada en la barra lateral
if seccion in imagenes:
    st.sidebar.image(imagenes[seccion], use_container_width=True)

if seccion == "Inicio":
    st.header("Docentes:")
    st.write("**Coordinador del área:** Julio Barrios")
    st.write("**Coordinadora de Química:** Cecilia Castillo")
    st.write("**Coordinador de Física:** Luis Samaniego")
    st.write("**Coordinador de Biología:** José Cantela")

elif seccion == "Química":
    st.header("Química")
    st.write("**Coordinadora de Química:** Cecilia Castillo")
    with st.expander("Contenido del curso"):
        st.write("- Introducción a la química general")
        st.write("- Propiedades de la materia")
        st.write("- Reacciones químicas y estequiometría")

elif seccion == "Física":
    st.header("Física")
    st.write("**Coordinador de Física:** Luis Samaniego")
    with st.expander("Contenido del curso"):
        st.write("- Conceptos básicos de cinemática")
        st.write("- Leyes de Newton")
        st.write("- Energía y trabajo")

elif seccion == "Biología":
    st.header("Biología")
    st.write("**Coordinador de Biología:** José Cantela")
    with st.expander("Contenido del curso"):
        st.write("- Introducción a la biología celular")
        st.write("- Genética y herencia")
        st.write("- Evolución y biodiversidad")

elif seccion == "Calendario":
    st.header("Calendario de Horarios")
    with st.expander("Ver calendario"):
        st.write("| Docente | Día | Horario |")
        st.write("|---------|-----|---------|")
        st.write("| Julio Barrios | Lunes y Miércoles | 10:00 - 12:00 |")
        st.write("| Cecilia Castillo | Martes y Jueves | 14:00 - 16:00 |")
        st.write("| Luis Samaniego | Miércoles y Viernes | 08:00 - 10:00 |")
        st.write("| José Cantela | Martes y Jueves | 10:00 - 12:00 |")

elif seccion == "Útiles Escolares":
    st.header("Teória")
    with st.expander("Química"):
        st.write("- 01 cuad. A4 100 hojas (cuadriculado)")
        st.write("- Color: Verde Oscuro")
        st.write("- Ejemplo")
        st.image("q.jpg", width=500)
    with st.expander("Física"):
        st.write("- 01 cuad. A4 100 hojas (cuadriculado)")
        st.write("- Color: Verde Limón")
        st.write("- Ejemplo")
        st.image("f.jpg", width=500)
    with st.expander("Biología"):
        st.write("- 01 cuad. A4 100 hojas (cuadriculado)")
        st.write("- Color: Verde Claro")
        st.write("- Ejemplo")
        st.image("b.jpg", width=500)
    st.header("Laboratorio")
    st.write("- 01 guardapolvo blanco para laboratorio.")
    st.image("gu.jpg", width=400)
    st.write("- 01 gafas de seguridad para laboratorio.")
    st.image("ga.jpg", width=400)
    st.write("- 01 guante desechable para laboratorio (látex o nitrilo) para cada práctica de laboratorio.")
    st.image("gua.jpg", width=400)    

