import random


def CrearMatriz(Lista):
    a = 1
    b = 1
    if (len(Lista) % 2) <= 0:
        print("No se puede hacer una x")
    else:
        for i in range(3, 100):
            Tmatriz = i * i
            T = Tmatriz - len(Lista)
            if Tmatriz % (len(Lista) + T) == 0:
                Matriz = []
        for i in Lista:
            if b == 1:
                Matriz.append(Lista[b])
                b + 1
            elif b == Tmatriz:
                Matriz.append(Lista[b])
                a + 1
                b + 1
            else:
                Matriz.append(0)
                b + 1
        print(Matriz)


Tamaño = int(input("Favor de ingresar el tamaño"))

if Tamaño < 4 | Tamaño > 100:
    print("Favor de ingresar un numero valido")
else:
    Lista2 = []
    for i in range(0, Tamaño):
        Lista2.append(random.randint(4, 100))
    print(CrearMatriz(Lista2))
