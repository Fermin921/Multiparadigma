class Figura:
    def __init__(self, ancho, largo):
        self._ancho = ancho
        self._largo = largo

    def __str__(self, color) -> str:
        return f"{self._ancho} {self._largo}"
