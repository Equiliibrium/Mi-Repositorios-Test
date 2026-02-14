Viajes = "Qué lugares has visitado?, "
Viajes += "Presiona 'quit' cuando quieras salir de la consulta\n"

while True:
    lugar = input(Viajes)
    
    if lugar == 'quit':
        break
else:
    print("Son lugares preciosos!")