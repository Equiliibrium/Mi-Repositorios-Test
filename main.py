import string    
import secrets

def generar_password(longitud = 16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    return password

if __name__ == "__main__":
    print("|---- Generador de contraseñas seguras ----|")
    entrada = input("De cuántos caractéres quieres tu contraseña? \n (Presiona 'ENTER' para asignar 16 ctres.):")
    try:
        largo = int(entrada if entrada else 16)
        nueva_pass = generar_password(largo)
        print(f"\n Tu nueva contraseña es {nueva_pass}")
        print(f"Se recomienda no compartirla con nadie")
    except ValueError:
        print("Error: Por favor, ingresa un número válido")
        

    

                