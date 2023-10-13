#Ciclo while
x=5
y=6
# while True:     #Se declara
#     print(x)

# while x > 0 and y < 5 :
#     y+=1
#     x+=1
#     print(x,y)
# else : #Esta sentencia se va a ejecutar al terminar todas las iteraciones principales de la condicion
#     print("Ya cerro el ciclo")

# try :       #Forma de declarar una exception
#     s={1,2,3}
#     s[2] = 10
# except Exception as e:
#     print(e)

def Resta():        #Declaracion de una funcion, recuerda crear primero la funcion y lueg mandarla llamar, que luego no lo reconoce
    a = 9
    b = 10 
    c = a - b
    return c    
# end def

def multiplicacion(a,b,c): #Funcion con parametros
    """
    Sirve para mostar mensaje de ayuda para las funciones
    """
    return (a*b*c)
print(multiplicacion(2,3,4))
print(Resta())

def prubea(*x): #Sirve para mandar una tupla, o bien lo convierte en una tupla los datos que se madnaran y para recibir varios parametros
    print(type(x))
    suma = 0
    for i in x:
        suma+1
    return suma

