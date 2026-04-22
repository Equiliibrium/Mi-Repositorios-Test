import json # permite leer y guardar archivos de texto
import os # verificará si el archivo existe

# Es una interfaz de mis gustos musicales

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
    print("  1. Agregar canción")
    print("  2. Ver todas las canciones")
    print("  3. Buscar por artista")
    print("  4. Marcar como favorita ⭐")
    print("  5. Ver mis favoritas")
    print("  6. Eliminar canción")
    print("  7. Estadísticas")
    print("  0. Salir")
    print("═" * 34)

# ── FUNCIONES DEL MENÚ ───────────────────────────────────────
def agregar_cancion(canciones):
    print("\n── Agregar canción ──")
    titulo  = input("Título:  ").strip()
    artista = input("Artista: ").strip()
    genero  = input("Género:  ").strip()
    anio    = input("Año:     ").strip()

    cancion = {
        "id":        len(canciones) + 1,
        "titulo":    titulo,
        "artista":   artista,
        "genero":    genero,
        "anio":      anio,
        "favorita":  False
    }
    canciones.append(cancion)
    guardar_datos(canciones)
    print(f"\n✔ '{titulo}' agregada correctamente 🎶")


def ver_canciones(canciones):
    print("\n── Todas las canciones ──")
    if not canciones:
        print("No hay canciones aún. ¡Agrega una!")
        return
    for c in canciones:
        fav = "⭐" if c["favorita"] else "  "
        print(f"  [{c['id']}] {fav} {c['titulo']} — {c['artista']} ({c['anio']}) | {c['genero']}")


def buscar_por_artista(canciones):
    print("\n── Buscar por artista ──")
    busqueda = input("Nombre del artista: ").strip().lower()
    resultados = [c for c in canciones if busqueda in c["artista"].lower()]

    if not resultados:
        print("No se encontraron canciones de ese artista.")
        return
    print(f"\n{len(resultados)} resultado(s):")
    for c in resultados:
        print(f"  🎵 {c['titulo']} ({c['anio']}) | {c['genero']}")


def marcar_favorita(canciones):
    print("\n── Marcar como favorita ──")
    ver_canciones(canciones)
    if not canciones:
        return
    try:
        id_cancion = int(input("\nID de la canción: "))
        for c in canciones:
            if c["id"] == id_cancion:
                c["favorita"] = not c["favorita"]   # alterna entre True y False
                estado = "marcada como favorita ⭐" if c["favorita"] else "quitada de favoritas"
                guardar_datos(canciones)
                print(f"✔ '{c['titulo']}' {estado}")
                return
        print("No se encontró esa ID.")
    except ValueError:
        print("Por favor ingresa un número válido.")


def ver_favoritas(canciones):
    print("\n── Mis favoritas ⭐ ──")
    favoritas = [c for c in canciones if c["favorita"]]
    if not favoritas:
        print("No tienes favoritas aún.")
        return
    for c in favoritas:
        print(f"  ⭐ {c['titulo']} — {c['artista']} ({c['anio']})")


def eliminar_cancion(canciones):
    print("\n── Eliminar canción ──")
    ver_canciones(canciones)
    if not canciones:
        return
    try:
        id_cancion = int(input("\nID a eliminar: "))
        for c in canciones:
            if c["id"] == id_cancion:
                canciones.remove(c)
                guardar_datos(canciones)
                print(f"✔ '{c['titulo']}' eliminada correctamente.")
                return
        print("No se encontró esa ID.")
    except ValueError:
        print("Por favor ingresa un número válido.")


def ver_estadisticas(canciones):
    print("\n── Estadísticas ──")
    if not canciones:
        print("No hay canciones para mostrar estadísticas.")
        return

    total      = len(canciones)
    favoritas  = sum(1 for c in canciones if c["favorita"])

    # género más repetido
    generos = [c["genero"].lower() for c in canciones]
    genero_top = max(set(generos), key=generos.count)

    # artista más repetido
    artistas   = [c["artista"].lower() for c in canciones]
    artista_top = max(set(artistas), key=artistas.count)

    print(f"  🎵 Total de canciones:  {total}")
    print(f"  ⭐ Favoritas:           {favoritas}")
    print(f"  🎸 Género más común:    {genero_top.capitalize()}")
    print(f"  🧑‍🎤 Artista más agregado: {artista_top.capitalize()}")


# ── PROGRAMA PRINCIPAL ───────────────────────────────────────
def main():
    canciones = cargar_datos()
    print("\n¡Bienvenido a tu Biblioteca Musical! 🎶")

    while True:                          # el menú se repite hasta que elijas 0
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if   opcion == "1": agregar_cancion(canciones)
        elif opcion == "2": ver_canciones(canciones)
        elif opcion == "3": buscar_por_artista(canciones)
        elif opcion == "4": marcar_favorita(canciones)
        elif opcion == "5": ver_favoritas(canciones)
        elif opcion == "6": eliminar_cancion(canciones)
        elif opcion == "7": ver_estadisticas(canciones)
        elif opcion == "0":
            print("\n¡Hasta luego! Sigue escuchando buena música 🎵\n")
            break
        else:
            print("Opción no válida. Elige entre 0 y 7.")


# ── PUNTO DE ENTRADA ─────────────────────────────────────────
if __name__ == "__main__":
    main()

