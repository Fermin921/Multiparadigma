# Lista1 = ["1", "2", "3", "4", "5"]
# Lista2 = ["1,", "6", "2", "7"]
# print(Lista2|)


Entrada = int(input("Ingrese le cantida de segmentos"))
TamañoBarra = 1

while TamañoBarra <= Entrada:
    TamañoBarra = TamañoBarra * 2

if TamañoBarra == Entrada:
    print(TamañoBarra, (TamañoBarra / Entrada))
elif TamañoBarra < Entrada:
    Diferencia = Entrada - TamañoBarra
    TamañoBarra * 2
    denon = 0
    while Diferencia != denon:
        denon = TamañoBarra / 2
        partes = partes + 1
        if denon == Diferencia:
            break
