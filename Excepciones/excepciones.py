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
    correcto = "@"
    correcto2 = "."
    print(correcto)
    print(correcto2)
    if correcto in correo:
        print("no es valido. Le quedan " + str(contador - 1) + " intentos")
        if contador != 1:
            contador = contador - 1
            introduzca_correo(contador)
        else:
            print("La sesion ha sido bloqueada por demasiados intentos")

    elif correcto2 in correo:
        print("no es valido. Le quedan " + str(contador - 1) + " intentos")
        if contador != 1:
            contador = contador - 1
            introduzca_correo(contador)
        else:
            print("La sesion ha sido bloqueada por demasiados intentos")  
    else:
        print("bienvenido")

contador = 3
introduzca_correo(contador)