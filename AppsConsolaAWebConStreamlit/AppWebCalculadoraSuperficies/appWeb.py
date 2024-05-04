import streamlit as st
import funciones

st.title("Calculadora de Superficies de Figuras Geométricas")

st.write("***MENÚ CALCULADORA DE SUPERFICIES****")
st.write("1- CUADRADO")
st.write("2- RECTÁNGULO")
st.write("3- TRIÁNGULO")
st.write("0- SALIR")

opcion = st.number_input("Ingrese una opción", min_value=0, step=1, key="menu")

if opcion == 1:
    lado = st.number_input("Ingrese el lado del cuadrado", min_value=0, key="lado_cuadrado")
    if st.button("Calcular"):
        resultado = funciones.superficieCuadrado(lado)
        st.write(f"La superficie del cuadrado es: {resultado}")

elif opcion == 2:
    base = st.number_input("Ingrese la base del rectángulo", min_value=0, key="base_rectangulo")
    altura = st.number_input("Ingrese la altura del rectángulo", min_value=0, key="altura_rectangulo")
    if st.button("Calcular"):
        resultado = funciones.superficieRectangulo(base, altura)
        st.write(f"La superficie del rectángulo es: {resultado}")

elif opcion == 3:
    base = st.number_input("Ingrese la base del triángulo", min_value=0, key="base_triangulo")
    altura = st.number_input("Ingrese la altura del triángulo", min_value=0, key="altura_triangulo")
    if st.button("Calcular"):
        resultado = funciones.superficieTriangulo(base, altura)
        st.write(f"La superficie del triángulo es: {resultado}")

elif opcion == 0:
    st.write("Gracias por utilizar nuestra app!")
    pass

else:
    st.write("¡Opción incorrecta. Vuelva a intentarlo!")
