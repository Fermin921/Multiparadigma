Producto = input("Ingrese el nombre del producto: ")
Precio = input("Ingrese el precio del producto: ")
Existencias = input("Ingrese el numero de unidades del producto: ")
float(Precio) 
float(Existencias)
Datos = f"El nombre del producto es: '{Producto}' end='\n' Cantidad de Precio unitario: '{Precio:.2f}' end='\n' Cantidad de existencias: {Existencias:.2f} end='\n' Precio total= {(Precio*Existencias):.2f}."
print(Datos)
#ZFill(8) para agregar los 0 a la izquierda

# producto = input('Introduce el nombre del producto: ')
# precio = float(input('Introducde el precio unitario: '))
# unidades = int(input('Introduce el número de unidades: '))
# print('{producto}: {unidades:3d} unidades x {precio:6.2f} = {total:8.2f}'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))