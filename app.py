import streamlit as st

st.set_page_config(page_title="Curso de Ciencia y Tecnología", layout="wide")

# Cargar un logo pequeño en la parte superior
logo_top_path = "SV_insignia.jpg"  # Asegúrate de subir este archivo al mismo directorio que el script
st.image(logo_top_path, width=100)

st.title("Curso de Ciencia y Tecnología")

# Cargar un logo desde un archivo local en la barra lateral
logo_path = "SV_logo.jpg"  # Asegúrate de subir este archivo al mismo directorio que el script
st.sidebar.image(logo_path, use_column_width=True)

st.sidebar.title("Menú")
seccion = st.sidebar.selectbox("Selecciona una sección", ["Inicio", "Química", "Física", "Biología", "Calendario", "Materiales"])

# Diccionario de imágenes para cada sección
imagenes = {
    "Inicio": "inicio.jpg",
    "Química": "quimica.jpg",
    "Física": "fisica.jpg",
    "Biología": "biologia.jpg",
    "Calendario": "calendario.jpg",
    "Materiales": "materiales.jpg"
}

# Mostrar imagen correspondiente a la sección seleccionada
if seccion in imagenes:
    st.image(imagenes[seccion], use_column_width=True)

if seccion == "Inicio":
    st.header("Coordinadores y Docentes")
    st.write("**Coordinador del curso:** Julio Barrios")
    st.write("**Coordinadora de Química:** Cecilia Castillo")
    st.write("**Coordinador de Física:** Luis Samaniego")
    st.write("**Coordinador de Biología:** José Cantela")

elif seccion == "Química":
    st.header("Área de Química")
    with st.expander("Contenido del curso"):
        st.write("- Introducción a la química general")
        st.write("- Propiedades de la materia")
        st.write("- Reacciones químicas y estequiometría")

elif seccion == "Física":
    st.header("Área de Física")
    with st.expander("Contenido del curso"):
        st.write("- Conceptos básicos de cinemática")
        st.write("- Leyes de Newton")
        st.write("- Energía y trabajo")

elif seccion == "Biología":
    st.header("Área de Biología")
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

elif seccion == "Materiales":
    st.header("Materiales del curso")
    with st.expander("Ver materiales"):
        st.write("- Libros de referencia")
        st.write("- Apuntes y presentaciones")
        st.write("- Prácticas y experimentos")
        
