m = float(input("Favor de ingresar dividendo"))
n = float(input("Favor de ingresar el divisor"))
Lista = list()
div = m / n
while div > 1:
    div = m / n
    m = div
    Lista.append(div)
    print(Lista)
    if div <= 1:
        print(f"{Lista}  El valor es correcto")
        break
    else:
        # print(Lista + "El valor es incorrecto")
        # break
        print(f"{Lista}  El valor es incorrecto")
