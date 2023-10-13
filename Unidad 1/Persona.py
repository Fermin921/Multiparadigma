
class Persona:
    def __init__(self, nombre, edad)-> None:
        self._nombre = nombre
        self._edad = edad
    def __str__(self) -> str:
        return f"Persona: {self._nombre} Edad: {self._edad}"