def matriz_a_diccionario(matriz):
    diccionario = {}
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            diccionario[(i, j)] = elemento
    return diccionario


def tupla_a_matriz(tupla, num_filas, num_columnas):
    if num_filas * num_columnas != len(tupla):
        raise ValueError(
            "El tamaño de la tupla no coincide con el número de filas y columnas especificados."
        )

    matriz = []
    indice = 0

    for i in range(num_filas):
        fila = []
        for j in range(num_columnas):
            fila.append(tupla[indice])
            indice += 1
        matriz.append(fila)

    return matriz


def SetListas(set):
    se = list(set)
    print(se)
