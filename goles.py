import matplotlib.pyplot as plt


jugadores = ['Lean', 'Graña', 'Eze', 'José','Lucio', 'Manu', 'Tincho', 'Mate','Nardo', 'Richard', 'Tello', 'Tobi', 'Tomi', 'Mike', 'Valen', 'Fushi']
goles = [      11,      8,      0,     2,      0,      2,        2,       1,     7,        1,        2,       0,     2,       0,      1,      1]


def actualizar_goles(jugador, cantidad):
    index = jugadores.index(jugador)
    goles[index] = cantidad
    mostrar_estadisticas()

'''
def mostrar_estadisticas():
    plt.pie(goles, labels=jugadores, autopct='%1.1f%%')
    plt.title('Goles de los jugadores')
    plt.show()

'''
    
def mostrar_estadisticas():
    plt.bar(jugadores, goles)
    plt.title('Goles')
    plt.xlabel('Jugadores')
    plt.show()



mostrar_estadisticas()


for i in range(len(jugadores)):
    goles[i] = int(input(f"Ingrese los goles de {jugadores[i]}: "))


mostrar_estadisticas()