import re

'''class web:
    def __init__(self, correo):
        self.correo = correo
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo'''


contador = 3
def introduzca_correo():
    print("Introduzca la direccion de correo electronico")
    correo = input()
    correcto = re.search(". * @. * ", correo)
    if correcto == None:
        if "." not in correo:
            print("Correo no válido, le falta el punto")
        else:
            print("Le falta el @. Vuelve a intentar")
        contador = contador - 1
        introduzca_correo()
    else:
        print("bienvenido")
introduzca_correo()