
import excepciones

if __name__ == "__main__":
    print("Introduzca la direccion de correo electronico")
    correo = str(input())
    try:
        excepciones.validar_formato(correo)
    except excepciones.formato_excepcion:
        print("Esta mal el correo")
    else:
        print("todo bien")
