"""
Docstring for LOGINBASICO
"""


def login_basico(usuario, contrasena):
    """
    Función para validar el inicio de sesión básico.

    Parámetros:
    usuario (str): El nombre de usuario.
    contrasena (str): La contraseña del usuario.

    Retorna:
    bool: True si las credenciales son correctas, False en caso contrario.
    """
    usuario_correcto = "admin"
    contrasena_correcta = "1234"

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        return True
    else:
        return False
    
def solicitar_credenciales():
    """
    Función para solicitar las credenciales al usuario.

    Retorna:
    tuple: Una tupla que contiene el nombre de usuario y la contraseña.
    """
    print("Ingrese su nombre de usuario:")
    usuario = input()
    print("Ingrese su contraseña:")
    contrasena = input()
    return usuario, contrasena

