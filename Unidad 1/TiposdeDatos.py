# #Tipos de datos numericoss
# x = 1 #Enteros
# y = 2.2 #Flotantes
# z = 3j + 2 #Complejos

# print(type(x), type(y), type(z)) #Para verificar que tipo de dato es una variables
# print (id(x), id(y), id(z)) #Sirve para verificar la direccion de memoria que tienen las variables

# #La es una manera de parse o convertir una variable a otro tipo de dato
# xflotante = float(x) 
# ycomplejo = complex(y)
# #zentero = int(z)
# print(type(xflotante), type(ycomplejo))

# #Tipos de datos booleanos 
# x = True
# y = False
# if (x ):        #No se utilizan llaves, tiene que estar identado debajo del if, para saber que esta dentro de el
#     print('1')

# if not(y) :
#     print ('2')

# #Se puede utilizar para validad estructuras si estan vacias

# #Datos de tipo string o cadena
# x = "Que rollo prrioo"
# y = "Adios Prrio"
# print(x)

# saludo =f'Saludo: {x}', 'Despedida:{y}' #Interpolacion sirve para juntar o anteponer cadenas o numeros juntos
# print(saludo)

# saludo2 = 'Saludo:'+x+', Despedida:'+str(y) #Es la concatenacion, el str se refiere al tostring
# print("Saludo 2") 

# texto = """  
#  Que rollo prrio
#    adios prrio 
#    como vas """
# print (texto) #Sirve para el salto de linea entre cadenas


# print(x,y,z,sep='-', end='\n') #Sep es para separar al momento de imprimir varios datos y la sentencia end es para agregar un salto de linea

nombre = "Fermin Martinez"
print(str(nombre))
print(nombre[::-1])