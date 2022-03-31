correos_registrados = ["vicente@eni.com", "pepecasas@eni.com", "doloresbarriga@eni.com"]
class web:
    def __init__(self, listcorreo):
        self.listcorreo = listcorreo
    def get_listcorreo(self):
        return self.listcorreo
    def set_listcorreo(self, listcorreo):
        self.listcorreo = listcorreo



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