# #Los diccionarios son indexados, son mutables, no tienen un orden como las demas estructuras

# dic = {""} #Manera en la que se declara un diccionario
Dic = {
    "nombre": "Rocio",
    "Edad": 24,
    "Promedio": 24,
}  # Manera de agregar datos a un diccionario

print(Dic["Promedio"])  # Manera de imprimir un valor dependiendo de su index

# Dic["nombre"] = "Fermin" #Manera de poder modificar un valor dentro del diccionario
# print (Dic)

# for d in dic: #Manera tradicionala de recorrer un diccionario
#     print(d)

# for k,y in Dic.items(): #Manera de recorrer el diccionario de otra manera, sacando los 2 campos que se encuentran dentro, nombre del campo y el valor del dato
#     print(k,y)

# print(Dic.items())
# li=list(Dic.items()) #Manera de convertir un diccionario a una lista, puede servir para poder ordenar el diccionario de cierta manera
# print(li)

# print(dic.Get("Nombre","No existe el nombre")) #Manera de obtener un campo por su nombre

# print(Dic.keys())  # Para obtener las llaves

# Dic.clear()  # Sirve para limpiar las llaves del diccionario

# Dic.pop(
#     "Nombre"
# )  # Sirve para eliminar un campo en especifico, que al eliminarlo regresa el datos eliminado
# Dic.popitem()
