
correos_registrados = ["vicente@eni.com", "pepecasas@eni.com", "doloresbarriga@eni.com"]

class formato_excepcion(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje

class correo_excepcion(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje

class web:
    def __init__(self, listcorreo):
        self.listcorreo = listcorreo
    def get_listcorreo(self):
        return self.listcorreo
    def set_listcorreo(self, listcorreo):
        self.listcorreo = listcorreo

def validar_formato(correo):
    arroba = "@"
    punto = "."
    if punto not in correo: 
        raise formato_excepcion("Formato incorrecto")
    if arroba not in correo:
        raise formato_excepcion("Formato incorrecto")

def reconocer_correo(correo):
    if correo not in correos_registrados:
        raise correo_excepcion("Este correo no esta registrado")


