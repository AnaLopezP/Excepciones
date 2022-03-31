from traceback import format_exception
import excepciones

if __name__ == "__main__":
    print("Introduzca la direccion de correo electronico")
    correo = str(input())
    try:
        excepciones.validar_formato(correo)
    except format_exception:
        print("Esta mal el correo")
    else:
        print("todo bien")
