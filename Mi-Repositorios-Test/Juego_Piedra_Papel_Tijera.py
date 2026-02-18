import random

movimientos = ("Piedra", "Papel", "Tijera")
mov_aut = random.choice(movimientos)

print("Selecciona una jugada:")
print("1: Piedra | 2: Papel | 3: Tijera")
opcion = input("Elige el numero de tu jugada\n")

if opcion not in ("1", "2", "3"):
    print("Opcion no encontrada, reintente")
    quit()

mov_usuario = movimientos[int(opcion)-1]

print(f"Tú elegiste {mov_usuario}")
print(f"La máquina escogió {mov_aut}\n")

if mov_usuario == mov_aut:
    print("Empate :0")
    
elif (mov_usuario == "Piedra" and mov_aut == "Tijera") or \
     (mov_usuario == "Papel" and mov_aut == "Piedra") or \
     (mov_usuario == "Tijera" and mov_aut == "Papel"):
         print("Ganaste!!:O")
else:
    print("Perdiste :c")

