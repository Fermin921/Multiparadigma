# Diccionario Ejercicio
# Escribir un programa que guarde en un diccionario los precios de las frutas de la siguiente manera
# Primero columna, Fruta y la segunda precio
# Frutas: Platano, Manzana, pera y naranja
# Precio: 1.35, 0.80, 0.85, 0.7
# Guardar los nombres de las frutas en mayusculas en el diccionario
# Preguntar al usuario por una fruta y el numero de kilos
# Mostrar en pantalla el calculo y si la fruta no esta en el diccionario, mostrar un mensaje de eso

FrutaPrecio = {"PLATANO": 1.35, "MANZANA": 0.80, "PERA": 0.85, "NARANJA": 0.7}
NFruta = input("Ingrese el nombre de la fruta")
NKg = float(input("Ingrese la cantidad de kilos"))

def CalcularPrecio(NFruta):
    for NFruta in FrutaPrecio.items():
        Total = NKg * 

# end def
# Listas y tuplas
# Escribir un programa que almacene las siguientes matrices
# A= { [1,2,3] [4,5,6]} B= {[-1,1] [0,.1] [1,1]}
# Mostrar en pantalla su producto/multiplicacion almacenado en tuplas

# Matrices
# En una matriz de 5 x 4 pedir al usuario los valores y una segunda matriz de 5 x 4
# Si es multiplo de 3 guardar un 2
# Si es numero es multiplo de 5 guardar un 3
# Y un 4 si es multiplo de 3 y 5 a la vez
# Si no se cumple ninguna regla guardar un 0
