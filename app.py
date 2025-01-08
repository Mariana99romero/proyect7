import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv("vehicles_us.csv")
st.header("conjunto de datos de anuncios de ventas de coches")

build_histogram = st.checkbox('Construir histograma')  # crear un botón

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
disp_button = st.button("Construir un gráfico de dispersión")
if disp_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, user_container_width=True)
