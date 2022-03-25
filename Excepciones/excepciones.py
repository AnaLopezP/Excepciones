import re

'''class web:
    def __init__(self, correo):
        self.correo = correo
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo'''



def introduzca_correo(contador):
    print(contador)
    print("Introduzca la direccion de correo electronico")
    correo = input()
    correcto = re.search(". * @. * ", correo)
    if correcto == None:
        print("no es valido. Le quedan " + str(contador) + "intentos")
        contador = contador - 1
        introduzca_correo(contador)
        if contador == 0:
            print("La sesion ha sido bloqueada por demasiados fallos")
    else:
        print("bienvenido")

contador = 3
introduzca_correo(contador)