# Importar librerías a utilizar
import funciones

# Comienza el bucle while

while True:
    #Paso 1:Menú de la computadora
    print("***MENÚ CALCULADORA DE SUPERFICIES****")
    print("1- CUADRADO")
    print("2- RECTÁNGULO")
    print("3- TRIÁNGULO")
    print("0- SALIR")
    
    #Paso 2:Pedir al usuario que ingrese una opción
    opcion = int(input("ingrese una opcion: "))
    
    #Paso 3: Hacer que la computadora decida
    if opcion == 1:
        lado = int(input("Ingrese el lado del cuadrado: "))
        funciones.superficieCuadrado(lado)
        
    elif opcion == 2:
        base = int(input("Ingrese la base del rectángulo: "))
        altura = int(input("Ingrese la altura del rectángulo: "))
        funciones.superficieRectangulo(base, altura)
        
    elif opcion == 3:
        base = int(input("Ingrese la base del triángulo: "))
        altura = int(input("Ingrese la altura del triángulo: "))
        funciones.superficieTriangulo(base, altura)
        
    elif opcion == 0:
        print("Gracias por utilizar nuestra app!")
        break
            
    else:
        print("¡Opción incorrecta. Vuelva a intentarlo!")    
