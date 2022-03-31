
from asyncio import exceptions
from traceback import format_exception

correos_registrados = ["vicente@eni.com", "pepecasas@eni.com", "doloresbarriga@eni.com"]
'''class formato_excepcion(exceptions):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje'''

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
    if punto and arroba not in correo:
        raise Exception("Formato incorrecto")


