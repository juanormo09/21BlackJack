import random

#funcion para generar el mazo
def generar_mazo():
    cartas = ["Corazones", "Diamantes", "Treboles", "Picas"]
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    mazo = [{"valor": valor, 'carta': carta} for valor in valores for carta in cartas]
    random.shuffle(mazo)
    return mazo


#funcion para calcular puntos
def calcular_puntos(mano):
    puntos = 0
    ases = 0
    
    for carta in mano:
        valor = carta['valor']
        if valor.isdigit():
            puntos += int(valor)
        elif valor in ["J", "Q", "K"]:
            puntos += 10
        elif valor in ["A"]:
            ases += 1
            puntos += 11
    
    while ases > 0 and puntos > 21:
        puntos -= 10
        ases -= 1
        
    return puntos

def mostrar_mano(mano, oculta=False):
    if oculta:
        print(f"Cartas del dealer: [{mano[1]['valor']} de {mano[1]['carta']}] y [Carta Oculta]")
    else:
        print("Cartas:")
        for carta in mano:
            print(f"[{carta['valor']} de {carta['carta']}]")


def blackjack():
    mazo = generar_mazo()
    mano_jugador = [mazo.pop(), mazo.pop()]
    mano_dealer = [mazo.pop(), mazo.pop()]
    
    #Turno del Jugador
    while True:
        mostrar_mano(mano_jugador)
        puntuacion_jugador = calcular_puntos(mano_jugador)
        print(f"Puntuación Jugador: {puntuacion_jugador}")
        
        if puntuacion_jugador == 21:
            print("BlackJack ! Has ganado.")
            break
        elif puntuacion_jugador > 21:
            print("Perdiste!! te has pasado de 21!!")
            break
        
        opcion = input("¿Quieres tomar otra carta? (s/n): ").lower()
        if opcion == 's':
            mano_jugador.append(mazo.pop())
        else:
            break
        
    
    # Turno del Dealer
    mostrar_mano(mano_dealer, oculta = True) 
    puntuacion_dealer = calcular_puntos(mano_dealer)
    
    while puntuacion_dealer < 17:
        print("El dealer toma otra carta.")
        mano_dealer.append(mazo.pop())
        puntuacion_dealer = calcular_puntos(mano_dealer)
        
    print("\n Puntuacion del dealer: ", puntuacion_dealer)
    mostrar_mano(mano_dealer)
    
    #definir ganador
    if puntuacion_dealer > 21:
        print("El dealer se ha pasado de 21. ¡Has Ganado!")
    elif puntuacion_jugador > puntuacion_dealer:
        print("ganaste!!")
    elif puntuacion_jugador < puntuacion_dealer:
        print("perdiste!!")
    else:
        print("Empate!")
        
if __name__ == "__main__":
    print("Bienvenido al juego de 21 BlackJack")
    blackjack()