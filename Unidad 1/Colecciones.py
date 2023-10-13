
# #Tuplas son ordenadas e inmutable y permite datos duplicados, todos los elementos que se les agrega no se pueden modificar
# tupla = (1,2,3,3)
# print(tupla)
# print(type(tupla))

# tupla2 =(1,2('e','o',5),4) #Tupla dentro de otra duplas

# #Agregar datos a una tupla
# lista = list(tupla)
# lista.append(4)
# tupla3 = tuple(lista)
# print(tupla3)

# for t in tupla:
#     print (t)

# x,y,z,a = tupla3
# print(x,y,z,a)

#Como saber cuantos datos existen dentro de la tupla
# tupla = (2,)
# print(tupla)
# print(type(tupla))
# print(tupla.count(2))
# print(tupla.index(0)) #Sirve para sacar el index dentro de una tupla


#Lista ordenada, mutable y permite duplicados

# lista = [1,2,3,4]

# lista2 = list("4567") #Imprime o cuenta cada uno por separado

Lista3 = [1,"2","3",["4",4,5]]

lista4 = [1,2,3,4]
# print[Lista3[2]]

# print(Lista3[2:6])  #Rango para buscar datos entre las posiciones
# Lista3+=lista4 #Sumar listas directamente
# print(Lista3) 

# #Ciclo for con valor de i
# for i in range(0,len[Lista3]):
#     print(i)



# #metodos de las listas
# Lista3.append(2) #Agregar un nunevo dato a la lista
# Lista3.extend(3)
# Lista3.insert(1,4)
# Lista3.pop(1) #Eliminar datos
# Lista3.reverse() #Voltea la informacion
# Lista3.sort()


#Set ordena los numeros y no permite duplicados
#Sirve para ordenar y eliminar duplicados de una lista
set1 = {1,2,3,4} #Se declara 

# set[0] = 3 #No se pueden modificar los elementos, data error

# set.add(6) #Pero agregar y eliminar datos si dejara

set2 = set([2,3,4,5])
print(set2)

#| Union
#Exponencial es la interseccion

# for s in set2: Manera de recorrer un set
#     print(set2)

set2.add(1) #Agregar elementos
set2.remove(3) #Sirve para eliminar si esque existe directamente el valor dado
set2.discard(3) #Si no existe el elemento no elimina nada, al no existe el valor
set2.pop() #Elimina al azar un numero o elemento
set2.clear() #Para limpiar todo el set

set2.intersection() 
set2.union()
set2.difference()

#Caracteristica general, para ordenar y eliminar duplicados, se pueden convertir a diferentes tipos de colleciones para modificar,
# y para ordenar