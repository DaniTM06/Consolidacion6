import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app


def main():
    st.sidebar.title("Menú de Navegación")
    option = st.sidebar.selectbox("Selecciona una sección:", ["Home", "EDA", "ML", "Info"])

    if option == "Home":
        st.markdown(
            "<div style='background-color: #007BFF; padding: 20px; border-radius: 10px;'>"
            "<h1 style='color: white; text-align: center;'>APP PARA LA DETECCIÓN TEMPRANA DE DM (DIABETES MELLITUS)</h1>"
            "</div>",
            unsafe_allow_html=True
        )
        st.title("App para la detección temprana de DM")
        st.markdown("Dataset que contiene señales y síntomas que pueden indicar diabetes o posibilidad de diabetes")
        st.title("Contenidos de la App")
        st.markdown("- **EDA Section:** Análisis exploratorio de los datos")
        st.markdown("- **ML Section:** Predicción de Diabetes basada en ML (Machine Learning)")

    elif option == "EDA":
        run_eda_app()
    
    elif option == "ML":
        run_ml_app()

    elif option == "Info":
        st.subheader("Info")
        st.text("MBIT, proyecto de consolidación. Como la pagina de MBIT me rechazaba la conexion, intuyo que por seguridad, pongo la de google para que aparezca algo.")
        st.components.v1.iframe("https://www.wikipedia.com/")

if __name__ == '__main__':
    main()