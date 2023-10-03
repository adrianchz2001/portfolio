import streamlit as st

def main():
    st.set_page_config(page_icon = "🐍", page_title = "Portfolio")
    st.title("Mi portfolio profesional")
    st.write("Selecciona a la izquierda la página que deseas ver.")
    st.markdown("**Leyenda**")
    st.markdown("- Intro = Introducción a quién soy yo como profesional")
    st.markdown("- Projects = Enlaces y explicación breve de los proyectos que he realizado")
    st.markdown("- Contact me = Enlace a mi LinkedIn y correo electrónico")
    
    bar = st.sidebar.selectbox("Selecciona una página", ["Intro", "Projects", "Contact me"])
    if bar == "Intro":
        intro()
    elif bar == "Projects":
        projects()
    elif bar == "Contact me":
        contact()
        
def intro():
    st.write("¡Hola! Bienvenido a mi portfolio profesional como Científico de Datos. Aquí podrás hallar tanto los proyectos que he realizado individualmente como en cooperación estrecha con mi equipo académico.")
    boton_1 = st.button("¿Quién soy yo?", key = "about_me")
    if boton_1 == True:
        c1, c2 = st.columns(2)
        with c1:
            st.image("venv/Data/FotoJet.jpg")
        with c2:
            st.write("Mi nombre es Adrián. Soy un economista graduado (y colegiado) y también un científico de datos. No creo que ambas cosas vayan por separado, pues ambas se complementan como ninguna. Aunque trabajo principalmente con Python, también sé realizar trabajos de análisis y visualización de datos en R.")
            st.write("Aun así, al especializarme con Python, es con este lenguaje con el que soy capaz de realizar:")
            st.markdown("- Análisis de datos")
            st.markdown("- Visualización de datos")
            st.markdown("- Modelos de Machine Learning y Redes Neuronales para aprendizaje supervisado y no supervisado")
            st.markdown("- Sistemas de recomendación basados en filtro colaborativo o empleando redes neuronales")
            st.markdown("- Algoritmos genéticos con propósitos de optimización")
            st.markdown("- Computer Vision y NLP")
            st.write("Además, también trabajo con Tableau para crear reportes visuales y con Streamlit para desplegar aplicaciones como este portfolio. Aunque también trabajo con Power BI, suelo preferir Tableau debido a la gratuidad de éste al trabajar como individuo. No obstante, he trabajado con Power BI y su apartado de DAX")
            
def projects():
    st.write("A continuación, te presento todos mis proyectos:")
    with st.expander("Comparación de salarios ajustados por PPA"):
        st.write("El PPA, o Paridad de Poder Adquisitivo, es una medición que sirve para que podamos comparar los salarios de diferentes regiones tomando en cuenta su poder adquisitivo.")
        st.write("Es decir, que comparamos los salarios por todos los bienes que pueden comprar y no por si son cuantitativamente mayores o menores. Un salario de 4.000 u.m (unidades monetarias) es superior a uno de 600 u.m, ¿no?")
        st.write("Pues depende. Si en China puedes comprar con 600 u.m lo mismo que un estadounidense con 4000 u.m, entonces no es más, sino que es lo mismo. Queremos el dinero para adquirir bienes y servicios, así que es lógico comparar quién gana más o quién tiene más por su capacidad de adquirir dichos bienes y servicios y no solo por quién parece que tiene más en cuanto a monedas.")
        st.image("https://assets-us-01.kc-usercontent.com/fa776f1a-4d27-4a6b-ae1c-2ce928f9647d/3f823e77-d1c5-4143-b007-9ae35cf16476/wage-increase_2_cropped.jpg")
        st.markdown("[Enlace al proyecto](https://ppp-adjusted-wage-comparator.streamlit.app/)", unsafe_allow_html=True)
        
    with st.expander("Predicción de precios y demandas de energía en España"):
        st.write("Para este trabajo se tomaron los datos de la API de Red Eléctrica de España, quien es el único encargado de distribuir y abastecer en cuanto a electricidad a toda la industria española y, por consecuencia, a todos los ciudadanos españoles")
        st.write("Hecho esto, se tomaron los datos, se limpiaron, se procesaron y se entrenaron diferentes arquitecturas de redes neuronales hasta obtener resultados altamente provechosos. Posteriormente, se pasó a hacer que estos modelos hicieran predicciones a futuro. En concreto, a un año vista.")
        st.write("Hay que tener cuidado, eso sí, con los resultados. Pues si bien el modelo es fiable, las predicciones, cuanto más a largo plazo, más riesgo corren de ser incorrectas, pues pueden existir eventos que produzcan cambios en la tendencia y/o generen ruido blanco que antes no existía")
        st.image("https://i.pinimg.com/originals/3a/a1/01/3aa101db445d4fe5b29e0af57fe1b660.gif")
        st.markdown("[Enlace al proyecto](https://prediccion-redes-neuronales-ree.streamlit.app/)", unsafe_allow_html = True)
        
    with st.expander("Predicción de equipo ganador en League of Legends"):
        st.write("En este proyecto se tomaron datos de partidas del famoso videojuego League of Legends y se aplicaron técnicas de reducción de dimensionalidad tales como PCA y Gaussian Random Projection con tal de simplificar el problema y llevarlo a producción, pues el proyecto consiste en preguntarle al jugador por determinados datos y que el modelo envíe una respuesta.")
        st.write("Si tuviera que realizar 10 preguntas sería factible que el jugador las responda progresivamente. Lo que no es viable es que el jugador deba responder más de 20 preguntas en un juego que requiere respuestas rápidas y actuación eficiente.")
        st.image("https://e00-marca.uecdn.es/assets/multimedia/imagenes/2022/03/16/16474268125074.jpg")
        st.markdown("[Enlace al proyecto](https://lol-winner-predicter.streamlit.app/)", unsafe_allow_html = True)
        
    with st.expander("Otros proyectos"):
        st.write("Estos son proyectos que, sin restarles mérito ni importancia, no tienen una versión desplegada en Streamlit, por lo que solo os puedo compartir el código subido en GitHub mediante repositorios públicos.")
        st.markdown("- Sistema de recomendación de libros basado en filtraje colaborativo")
        st.image("https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books-illustration_23-2149341898.jpg?w=360")
        st.markdown("[Enlace al proyecto](https://github.com/adrianchz2001/recomendador_libros)", unsafe_allow_html = True)
        
        st.markdown("- Sistema de predicción de enfermedades")
        st.image("https://media.istockphoto.com/id/1187492975/vector/magnifying-lens-viruses.jpg?s=612x612&w=0&k=20&c=TxfNgofljtO26UHj4dKh1h9k-KL8BEpfQ-M7zbIAVyQ=")
        st.markdown("[Enlace al proyecto](https://github.com/adrianchz2001/predictor_de_enfermedades)", unsafe_allow_html = True)
        
def contact():
    st.header("¡Hola!")
    st.markdown("Si deseas contactarme, te dejo aquí mi [enlace a LinkedIn](https://www.linkedin.com/in/adri%C3%A1n-ch%C3%A1vez/)", unsafe_allow_html = True)
    st.write("Mi correo electrónico es: adrianchz2001@gmail.com")
    st.write("¡Encantado de conocerte!")
    
main()