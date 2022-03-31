
import excepciones

if __name__ == "__main__":
    print("Introduzca la direccion de correo electronico")
    correo = str(input())
    try:
        excepciones.validar_formato(correo)
    except excepciones.formato_excepcion as e:
        print(e.get_mensaje())
    else:
        print("formato correcto")
    
    try:
        excepciones.reconocer_correo(correo)
    except excepciones.formato_excepcion as e:
        print(e.get_mensaje())
    else:
        print("Bienvenid@")