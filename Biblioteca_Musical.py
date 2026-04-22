import json # permite leer y guardar archivos de texto
import os # verificará si el archivo existe

ARCHIVO = "canciones.json"

def cargar_datos ():
    if os.path.exists(ARCHIVO):
        with open (ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_datos(canciones):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(canciones, f, ensure_ascii=False, indent=4)
        
def mostrar_menu():
    print("\n" + "═" * 34)
    print("   🎵  MI BIBLIOTECA MUSICAL")
    print("═" * 34)
