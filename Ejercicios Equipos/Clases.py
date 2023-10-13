class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.__titular)
        print("Saldo:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def esTitularValido(self):
        edad = self.__titular.get_edad()
        return 18 <= edad <= 24

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print(
                "No puedes retirar dinero de una cuenta joven si no eres un titular válido."
            )


# titular_joven = Persona("Juan", 20)  # Supongamos que tienes una clase Persona con nombre y edad.
# cuenta_joven = CuentaJoven(titular_joven, 1000.0, 0.05)
# cuenta_joven.mostrar()  # Mostrará los datos de la cuenta joven y la bonificación.
# cuenta_joven.ingresar(500)
# cuenta_joven.retirar(200)
# cuenta_joven.mostrar()
