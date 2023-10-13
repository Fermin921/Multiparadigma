#Clases 

#Declarar una clase

class Rectangulo:
    def __init__(self) -> None: #Este es el contructor y self es el equivalente al this de C#
        self._ancho = ancho #Estos son los atributos
        self._largo = largo
        pass
    @property  #Esta es una propiedad
    def Ancho(self):
        return self._ancho

    @Ancho.setter   #Metodo de get y set
    def Ancho(self,ancho):
        self._ancho=ancho

    def CalcularArea(self):
        return self._ancho * self._largo
    
    
    def CalcularArea(self):
        return self._ancho + self._largo
    
class Cuadrado:
    def __init__(self) -> None:
        self._Lado = Lado
        pass

    @property
    def Lado (self):
        return self._Lado
    
    @Lado.setter
    def Lado(self,ancho):
        self._lado = Lado
    
    
    def CalcularArea(self):
        return self.Lado * 4
    
    
    def CalcularArea(self):
        return self.Lado + self.Lado +self.Lado +self.Lado
    
        