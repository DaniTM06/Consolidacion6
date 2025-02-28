import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run_eda_app():
    st.title("Exploratory Data Analysis (EDA)")
    submenu = st.sidebar.selectbox("Selecciona tipo de análisis:", ["Descriptivo", "Gráfico"])

    df_clean = pd.read_csv("data/diabetes_data_upload_clean.csv")

    if submenu == "Descriptivo":
        st.subheader("Análisis Descriptivo")
        st.dataframe(df_clean)

        col1, col2 = st.columns(2)

        with col1:
            with st.expander("Tipos de datos"):
                dtypes_df = pd.DataFrame(df_clean.dtypes).reset_index()
                dtypes_df.columns = ['Columna', 'Tipo de dato']  
                st.write(dtypes_df.set_index('Columna'))

            with st.expander("Resumen descriptivo"):
                st.write(df_clean.describe())

        with col2:
            with st.expander("Distribución por género"):
                st.write(df_clean['gender'].map({1: 'male', 0: 'female'}).value_counts(), index=False)

            with st.expander("Distribución por clase"):
                st.write(df_clean['class'].map({1: 'Positivo', 0: 'Negativo'}).value_counts(), index=False)

    elif submenu == "Gráfico":
        st.subheader("Análisis Gráfico")
        col3, col4 = st.columns(2)

        with col3:
            with st.expander("Distribución por género (gráfico)"):

                fig = px.histogram(df_clean, x='gender', color='gender', 
                                   category_orders={'gender': [0, 1]}, 
                                   labels={'gender': 'Gender'}, 
                                   title='Distribución por Género')
                st.plotly_chart(fig)

            with st.expander("Distribución por clase (gráfico)"):

                fig = px.histogram(df_clean, x='class', color='class', 
                                   labels={'class': 'Class'}, 
                                   title='Distribución por Clase')
                st.plotly_chart(fig)

        with col4:
            with st.expander("Detección de Outliers"):
                fig = px.box(df_clean, x='gender', y='age', 
                             title="Detección de Outliers (Edad por Género)")
                st.plotly_chart(fig)

        with st.expander("Gráfico de correlación"):
            corr_matrix = df_clean.corr()
            fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='Viridis',
                            title="Matriz de Correlación", 
                            width=900,
                            height=600) 
            st.plotly_chart(fig)
