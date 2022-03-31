
class web:
    def __init__(self, correo):
        self.correo = correo
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo

def esta_arroba(correo):
        arroba = "@"
        if arroba in correo:
            return True
        else:
            return False

def esta_punto(correo):
        punto = "."
        if punto in correo:
            return True
        else:
            return False

def introduzca_correo(contador):
    print("Introduzca la direccion de correo electronico")
    print(contador)
    correo = str(input())
    esta_arroba(correo)
    print(esta_arroba)
    esta_punto(correo)
    print(esta_punto)
    if esta_arroba == True and esta_punto == True:
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