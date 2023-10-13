from Figura import Figura
from Color import Color

class Cuadrado(Figura,Color): #Manera de hacer herencia multiple
    def __init__(self, color, lado):
        Figura.__init__(ancho, lzz)
        Color.__init__(self, color) #Mandar llamar los contructores de las clases padre

    def CalcularArea(self):
        return self._lado * self._ancho
    
    def __str__(self,color) -> str:
        return f"{Figura.__str__(self)} {Color.__str__(self)} AREA: {self.CalcularArea()}"
Cuadrado1 = Cuadrado("Verde",5)
print(Cuadrado1)
