import socket
from datetime import datetime

def port_scanner(target, ports):
    print("-" * 50)
    print(f"Escaneando objetivo: {target}")
    print(f"Inicio: {datetime.now()}")
    print("-" * 50)

    try:
        for port in ports:
            # Creamos el socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            
            # Intentamos la conexión
            resultado = s.connect_ex((target, port))
            
            # LA MEJORA: El if/else va aquí adentro para que se repita por cada puerto
            if resultado == 0:
                print(f"🟢 Puerto {port}: ABIERTO")
            else:
                print(f"🔴 Puerto {port}: CERRADO (Código {resultado})")
            
            s.close()

    except KeyboardInterrupt:
        print("\n🛑 Escaneo detenido por el usuario.")
    except socket.gaierror:
        print("\n❌ No se pudo resolver el host.")
    except socket.error:
        print("\n❌ Error de conexión.")

if __name__ == "__main__":
    objetivo = input("Introduce la IP o dominio (ej: 127.0.0.1): ")
    # Puertos comunes para probar
    puertos_comunes = [21, 22, 80, 443, 8000]
    
    port_scanner(objetivo, puertos_comunes)