from Exportador import tupla_a_matriz, matriz_a_diccionario, SetListas

set1 = {1, 2, 3, 4}
SetListas(set1)

t = (1, 2, 3, 4, 5, 6)
matriz_resultante = tupla_a_matriz(t, 2, 3)
print(matriz_resultante)

matriz = [[1, 2, 3], [4, 5, 6]]
diccionario_resultante = matriz_a_diccionario(matriz)
print(diccionario_resultante)
