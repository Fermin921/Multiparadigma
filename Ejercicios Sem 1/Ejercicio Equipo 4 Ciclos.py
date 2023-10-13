# frase = input("Ingresa una frase: ")
# letra = input("Ingresa la letra que deseas contar: ")
# Cant = frase.count(letra)
# Aparece = f"La letra '{letra}' aparece {Cant} veces en la frase."
# print(Aparece)

Frase = input("Ingresa una frase: ")
for i in range(len(Frase)):
    if Frase[i] != " ":
        Palabra = Palabra + Frase[i]
    if Frase[i] == " ":
        Cant = Frase.count(Palabra)
        Dic = {Palabra, Cant}
        Palabra = ""
print(Dic)
