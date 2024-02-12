import random

#funcion para generar el mazo
def mazo():
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
