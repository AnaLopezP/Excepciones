
class web:
    def __init__(self, correo):
        self.correo = correo
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo



def introduzca_correo(contador):
    print("Introduzca la direccion de correo electronico")
    print(contador)
    correo = str(input())
    arroba = "@"
    punto = "."
    if punto and arroba in correo:
        print("bienvenido")
    else:
        print("no es valido. Le quedan " + str(contador - 1) + " intentos")
        if contador != 1:
            contador = contador - 1
            introduzca_correo(contador)
        else:
            print("La sesion ha sido bloqueada por demasiados intentos")

contador = 3
introduzca_correo(contador)