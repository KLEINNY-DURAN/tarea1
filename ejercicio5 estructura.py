#Dado un número entero N que representa una contraseña y asumiendo que una
#contraseña debe tener al menos 10 dígitos para ser segura, determine si la
#contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
#nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
#mostrar un mensaje de éxito al usuario, por salida estándar.
def ejercicio5ei (self):
        print("\n")
        contraseña_kmdt = int(input("Ingresar una contraseña de 10 digitos:"))
        m_kmdt = 0
        while contraseña_kmdt > 0:
            contraseña_kmdt //= 10
            m_kmdt = m_kmdt + 1
        if m_kmdt == 10:
            print("la contraseña es correcta")
        else:
            print("La contraseña es incorrecta")