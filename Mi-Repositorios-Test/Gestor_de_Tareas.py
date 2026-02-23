import os

NOMBRE_ARCHIVO = "mis_tareas.txt" 

def cargar_tareas():
    """Lee las tareas desde el archivo .txt"""
    tareas = []
    
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "r") as archivo:
            for linea in archivo:
                
                tareas.append(linea.strip())
    return tareas

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo .txt"""
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def mostrar_menu():
    print("\n--- Gestor de tareas Profesional ---")
    print("1.- Ver tareas")
    print("2.- Agregar tarea")
    print("3.- Eliminar tarea")
    print("4.- Salir")

def main():
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción 1/4 :")
        
        if opcion == "1":
            print("\n📋 TAREAS PENDIENTES:")
            if not tareas:
                print("No hay tareas en la lista.")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

        elif opcion == "2":
            nueva_tarea = input("Escribe la nueva tarea: ")
            tareas.append(nueva_tarea)
            guardar_tareas(tareas)
            print("✅ Tarea agregada y guardada.")

        elif opcion == "3":
            if not tareas:
                print("No hay nada que eliminar.")
                continue
        
            try:
                indice = int(input("Número de tarea a eliminar: ")) - 1
                tarea_eliminada = tareas.pop(indice)
                guardar_tareas(tareas)
                print(f"🗑️ Eliminada: {tarea_eliminada}")
            except (ValueError, IndexError):
                print("❌ Número inválido.")

        elif opcion == "4":
            print("¡Adiós! Tus tareas quedaron guardadas.")
            break
        else:
            print("Opción no válida.")
            
if __name__ == "__main__":
    main()
    
