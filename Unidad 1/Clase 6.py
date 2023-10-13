
# #Funcion de varios numeros o parametros
# def resta(*numeros):
#     resta = 0
#     for i in numeros:
#         resta = 1
#         return resta

# print(resta(1,2,3,4,5,6,7))

# def suma(**kwargs):#Van a ser valores con llave utilizando los 2 asteriscos, para colocarles llaves o bien convertirlo en un diccionario
#     suma = 0
#     for key,value in kwargs.items():
#         print(key,value)
#         suma+=value
#     return suma

# # suma(a=10,b=5,c=12,d=20)

# dic = {'a':10,'b':11,'c':12,'d':9}  #Diccionario
# suma(**dic) #Con los doble asteristicos puedo mandar diccionarios o bien ahora si los aceptara

# def funcion():
    # print("Entramos")
    # return  #Regresa o termina el proceso y lo que le sigue no lo 
    # print("No saliii")

# def sumaymedia(*x):
#     suma = 0
#     for i in x:
#         suma+= i
#     media=suma/len(x)
#     return suma,media
# resultadosuma,resultadomedia = sumaymedia(1,2,3,4,5,6,7,8) #Para dar valores a 2 variables, cuando regresa 2 parametros
# resultado=sumaymedia(1,2,3,4,5,6,7,8) #Se unifica y nos regresara los valores de los 2 parametros pero en forma de tupla
# print(resultado)


# def funcionp(a,b,*args,**kwargs):   #Todas las maneras de mandar parametros en una misma funcion
#     print('a',a) 
#     print('b',b)
#     for arg in args:
#         print('arg',arg)
#     for key,value in kwargs.items():
#         print(key,'=',value)

# funcionp(1,6,'k',4,2,4,"Que rollo",e=1,f=4,l=10)

# #funcion que suma todos los numero dentro de un rango
# numeros = list(range(1,101,1))
# def sum(*numeros):
#     sum = 0
#     for n in numeros:
#         sum+=n
#     return sum
# print(sum(*numeros))

# (lambda*n:print(sum(n)))(*list(range(1,101,1))) #Sirve para hacer codigo en una sola linea, tiene que tener los pararentisis al inicio
# #Para utilizarlo solo se agrega el valor 

# suma=None

# try:
#     suma=1+"1"
# except Exception as e:
#     print(e)
# else:
#     print("Que rollo es verdad") #Se ejecuta solo si no hay problemas
# finally:
#     print(suma) #Al salir error como quiera saldra este resultado



                        #Modulos        
from csv import DictReader #Sirve para traer solo la librearia a utilizar
import random   #Te traes todos los archivos que contenga esa libreria
5
numRandom = random.randint(0,50)

while True:
    numero = int(input("Cual sera el numero entre 0 y 50 ")) #Input es el equivalente a console,readline()
    if numero == numRandom:
        break
    if(numero>numRandom):
        print("EL numero es mayor")
    else:
        print("Es menor")
    print(f"El numero era{numRandom}")