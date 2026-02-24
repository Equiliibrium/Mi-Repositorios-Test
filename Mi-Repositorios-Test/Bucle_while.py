Viajes = "Qué lugares has visitado?, "
Viajes += "Presiona 'quit' cuando quieras salir de la consulta\n"

while True:
    lugar = input(Viajes)
    
    if lugar == 'quit':
        break
#else:
    #print("Son lugares preciosos!")
    
    
"""
Para evitar bucles infinitos debe haber una forma de "detención":
"""

x=1
while x <= 5:
    print(x)
    x += 1  # <----- Cabe mencionar que si no se considera esta linea de código, se ejecuta permanentemente