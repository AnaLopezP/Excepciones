import re

class web:
    def __init__(self, correo):
        self.correo = correo
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo


def introduzca_correo():
    print("Introduzca la direccion de correo electronico")
    correo = input()
    correcto = re.search("@", correo)
    if correcto == None:
        print("no es valido")
    else:
        print("bienvenido")

print(introduzca_correo())