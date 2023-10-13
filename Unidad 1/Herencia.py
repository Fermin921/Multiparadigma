
from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo) -> None:
        super().__init__(nombre,edad)
        self._sueldo=sueldo
    
    def __str__(self) -> str:
        return f"{super().__str__()} Suedlo: {self._sueldo}"
    
miempleado = Empleado("Fermin",25,8000)
print (miempleado)