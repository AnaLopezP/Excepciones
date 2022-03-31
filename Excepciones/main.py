
import excepciones

if __name__ == "__main__":
    contador = 0
    try:
        while contador < 3:
            print("Introduzca la direccion de correo electronico")
            correo = str(input())
            try:
                excepciones.validar_formato(correo)
                excepciones.reconocer_correo(correo)
                contador = contador + 1
            except excepciones.formato_excepcion as e:
                print(e.get_mensaje())
            except excepciones.correo_excepcion as err:
                raise err
            else:
                print("Todo correcto")
    except excepciones.correo_excepcion as ki:
        print(ki.get_mensaje())  



'''
try:
    excepciones.reconocer_correo(correo)
except excepciones.formato_excepcion as e:
    print(e.get_mensaje())
else:
    print("Bienvenid@")
    except excepciones.correo_excepcion as err:
                print(err.get_mensaje())'''