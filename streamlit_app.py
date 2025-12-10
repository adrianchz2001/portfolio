import streamlit as st
import glob, os, time
from PIL import Image
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
import base64
from pathlib import Path


def slideshow_local():
    # 👇 Carpeta de imágenes
    IMAGE_DIR = Path("Images")  # ajusta si la tienes en otro sitio

    # Extensiones permitidas
    exts = (".png", ".webp")

    files = sorted([p for p in IMAGE_DIR.iterdir() if p.suffix.lower() in exts])

    if not files:
        st.error(f"No se han encontrado imágenes en {IMAGE_DIR.resolve()}")
        return

    # Construcción dinámica de las diapositivas (base64)
    slides_html = ""
    n = len(files)

    for i, p in enumerate(files, start=1):
        data = p.read_bytes()
        suf = p.suffix.lower()

        mime = "image/webp" if suf == ".webp" else "image/png"
        b64 = base64.b64encode(data).decode("utf-8")
        src = f"data:{mime};base64,{b64}"

        slides_html += f"""
        <div class="mySlide fade">
          <div class="numbertext">{i} / {n}</div>

          <div class="slide-inner">
              <img src="{src}">
          </div>

          <!-- No caption -->
        </div>
        """

    # Puntos de navegación
    dots_html = "".join('<span class="dot"></span>' for _ in range(n))

    html_code = f"""
<!DOCTYPE html>
<html>
<head>

<style>
* {{ box-sizing: border-box; }}
body {{ font-family: Verdana, sans-serif; margin: 0; background: transparent; }}

/* Ocultar todas las slides inicialmente */
.mySlide {{ display: none; }}

/* CONTENEDOR PRINCIPAL — ANCHO MÁXIMO, ALTURA VARIABLE */
.slideshow-container {{
  max-width: 900px;        /* ancho máximo */
  width: 100%;             /* ocupa todo el ancho disponible hasta 900px */
  position: relative;
  margin: auto;
  border-radius: 16px;
  overflow: hidden;
  background: #ffffff;      /* fondo blanco */
  box-shadow: 0 16px 40px rgba(0,0,0,0.18);
}}

/* CONTENEDOR INTERNO DE LA IMAGEN */
.slide-inner {{
  width: 100%;
  background: white;        /* fondo blanco detrás de transparencias */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 20px 36px 20px; /* algo de aire alrededor de la imagen */
}}

/* IMAGEN — SE ADAPTA SIN CORTARSE */
.slide-inner img {{
  max-width: 100%;
  height: auto;             /* altura se ajusta según la proporción */
  object-fit: contain;      /* por si el navegador lo aplica */
  background: white;
}}

/* Texto (caption) al pie */
.caption {{
  color: #000;
  font-size: 15px;
  padding: 6px 12px;
  position: absolute;
  bottom: 0;
  width: 100%;
  text-align: center;
  background: rgba(255,255,255,0.85);
}}

/* Texto superior (1/5, 2/5, etc.) */
.numbertext {{
  color: #000;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}}

/* Puntos inferiores */
.dot {{
  height: 12px;
  width: 12px;
  margin: 0 3px;
  background-color: #ccc;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease, transform 0.3s ease;
}}

.active {{
  background-color: #333;
  transform: scale(1.25);
}}

/* Animación fade */
.fade {{
  animation-name: fade;
  animation-duration: 1.2s;
}}

@keyframes fade {{
  from {{opacity: .4}}
  to   {{opacity: 1}}
}}
</style>

</head>
<body>

<div class="slideshow-container">
  {slides_html}
</div>

<br>

<div style="text-align:center">
  {dots_html}
</div>

<script>
let currentIndex = 0;
showSlides();

function showSlides() {{
  let i;
  const slides = document.getElementsByClassName("mySlide");
  const dots = document.getElementsByClassName("dot");

  for (i = 0; i < slides.length; i++) {{
    slides[i].style.display = "none";
  }}

  currentIndex++;
  if (currentIndex > slides.length) {{ currentIndex = 1; }}

  for (i = 0; i < dots.length; i++) {{
    dots[i].className = dots[i].className.replace(" active", "");
  }}

  slides[currentIndex - 1].style.display = "block";
  dots[currentIndex - 1].className += " active";

  setTimeout(showSlides, 2500);
}}
</script>

</body>
</html>
"""

    components.html(html_code, height=650, scrolling=False)


def main():
    st.set_page_config(page_icon="🐍", page_title="Portfolio")

    bar = st.sidebar.selectbox(
        "Selecciona una página", ["Sobre mí", "Proyectos", "Contacto"]
    )
    if bar == "Sobre mí":
        intro()
    elif bar == "Proyectos":
        projects()
    elif bar == "Contacto":
        contact()


def intro():
    st.title("Hello, world! 👋")
    st.write("\n")
    st.write(
        "Soy Adrián. Soy analista y científico de datos. Estudié economía y un máster en Ciencia de Datos con la universidad Camilo José Cela (cursos y certificados aparte). He trabajado durante 2 años como analista de datos 🤓 y durante, aproximadamente, un año como científico de datos y transformador digital, trabajando para que las empresas puedan digitalizar y modernizar sus procesos internos, ganando eficiencia operativa con ello."
    )
    st.write(
        "Os dejo una muestra de algunas de las tecnologías que he usado en mi día a día durante mi trayectoria profesional como analista y científico de datos:"
    )
    slideshow_local()


def projects():
    st.title("Proyectos 🔥")
    st.write(
        "Saber no es suficiente; hay que aplicar. Querer no es suficiente; hay que hacer"
    )
    st.markdown("**~ Leonardo Da Vinci**")
    st.write(
        "\nExplora los proyectos, ordenados de más recientes a más antiguos. "
        "Siéntete libre de emplear filtros si estás buscando algo en concreto."
    )

    # ====== Definición de etiquetas ======
    eda = "Análisis de datos"
    series = "Series temporales"
    ap_s = "Aprendizaje supervisado"
    ap_no_s = "Aprendizaje no supervisado"
    ap_r = "Aprendizaje por refuerzo"
    grafos = "Análisis de grafos"
    llm = "IA generativa y LLMs"
    comp_vi = "Computer Vision"
    nlp = "Natural Language Processing"
    etl = "ETL/ELT"
    mlops = "MLOps"
    bases = "Bases de datos"

    # ====== Datos de proyectos ======
    projects_data = [
        {
            "title": "Comparación de salarios ajustados por PPA",
            "description": (
                "App interactiva para comparar salarios entre países ajustando por "
                "Paridad de Poder Adquisitivo (PPA)."
            ),
            "image": (
                "https://assets-us-01.kc-usercontent.com/"
                "fa776f1a-4d27-4a6b-ae1c-2ce928f9647d/3f823e77-d1c5-4143-b007-9ae35cf16476/"
                "wage-increase_2_cropped.jpg"
            ),
            "url": "https://ppp-adjusted-wage-comparator.streamlit.app/",
            "tags": [eda, series],
            "order": 3,
        },
        {
            "title": "Predicción de precios y demandas de energía en España",
            "description": (
                "Modelos de redes neuronales para predecir precios y demanda eléctrica "
                "a partir de datos de Red Eléctrica de España."
            ),
            "image": "https://i.pinimg.com/originals/3a/a1/01/3aa101db445d4fe5b29e0af57fe1b660.gif",
            "url": "https://prediccion-redes-neuronales-ree.streamlit.app/",
            "tags": [etl, series, ap_s],
            "order": 2,
        },
        {
            "title": "Predicción de equipo ganador en League of Legends",
            "description": (
                "Modelo que predice el equipo ganador aplicando reducción de dimensionalidad "
                "y aprendizaje supervisado sobre datos de partidas."
            ),
            "image": "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2022/03/16/16474268125074.jpg",
            "url": "https://lol-winner-predicter.streamlit.app/",
            "tags": [eda, ap_s],
            "order": 1,
        },
    ]

    projects_data = sorted(projects_data, key=lambda p: p["order"])

    # ====== Estilos de las cards ======
    st.markdown(
    """
<style>
.project-card {
    border-radius: 14px;
    padding: 0;
    overflow: hidden;
    background: #ffffff;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 1.4rem;
    transition: transform .15s ease, box-shadow .15s ease;
}
.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.18);
}
.project-image {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    display: block;
}
.project-body {
    padding: 0.7rem 0.9rem 0.9rem 0.9rem;
}

/* 🔥 Forzamos colores oscuros dentro de la card */
.project-title {
    margin: 0 0 0.3rem 0;
    font-size: 1.0rem;
    font-weight: 600;
    color: #111111 !important;  /* título bien negro */
}
.project-desc {
    margin: 0;
    font-size: 0.88rem;
    color: #333333 !important;  /* texto gris oscuro */
}
.tag-pill {
    display: inline-block;
    padding: 0.12rem 0.5rem;
    border-radius: 999px;
    background: #f1f3f5;
    color: #444444 !important;  /* texto de la pill más oscuro */
    font-size: 0.72rem;
    margin-right: 0.25rem;
    margin-top: 0.35rem;
}
a.project-link {
    text-decoration: none;
    color: inherit;
}
</style>
""",
    unsafe_allow_html=True,
)

    # ====== Filtro por etiquetas (multiselect) ======
    all_tags = sorted({tag for p in projects_data for tag in p["tags"]})

    selected_tags = st.multiselect(
        "Filtrar por tecnología usada",
        options=all_tags,
        default=[],
        help="Puedes elegir una o varias etiquetas.",
    )

    # OR lógico: proyecto válido si tiene AL MENOS una de las etiquetas seleccionadas
    def match_project(p):
        if not selected_tags:
            return True
        return bool(set(selected_tags) & set(p["tags"]))

    filtered_projects = [p for p in projects_data if match_project(p)]

    st.write("")  # pequeño espacio

    if not filtered_projects:
        st.info("No hay proyectos que cumplan ese filtro todavía.")
        return

    # ====== Render de cards tipo “listing item” ======
    cols_per_row = 3
    for i, p in enumerate(filtered_projects):
        if i % cols_per_row == 0:
            cols = st.columns(cols_per_row)
        col = cols[i % cols_per_row]

        with col:
            st.markdown(
                f"""
<a href="{p['url']}" target="_blank" class="project-link">
  <div class="project-card">
    <img src="{p['image']}" class="project-image" alt="{p['title']}">
    <div class="project-body">
      <h4 class="project-title">{p['title']}</h4>
      <p class="project-desc">{p['description']}</p>
      {''.join(f'<span class="tag-pill">{t}</span>' for t in p['tags'])}
    </div>
  </div>
</a>
""",
                unsafe_allow_html=True,
            )


def contact():
    st.title("Contáctame 📱")
    st.markdown(
        "Si deseas contactarme, te dejo aquí mi [enlace a LinkedIn](https://www.linkedin.com/in/adri%C3%A1n-ch%C3%A1vez/)",
        unsafe_allow_html = True,
    )
    st.write("Si prefieres, puedes enviar un correo electrónico a adrianchz2001@gmail.com")


main()
