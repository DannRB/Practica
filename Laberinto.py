#Comentario de prueba
#Daniiii
#Camacho
<<<<<<< HEAD
#OASES
=======
#SIIII
>>>>>>> 98097d5cbf77244648b2cdc2945e356469d9c132
FILAS = 5 
COLUMNAS = 5 
META_FILA = FILAS - 7
META_COLUMNA = COLUMNAS - 7 
def main(): 
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)] 
    fila_jugador, columna_jugador = 0, 0 
    laberinto[META_FILA][META_COLUMNA] = True  # Meta 
    while True: 
        for i in range(FILAS): 
            for j in range(COLUMNAS): 
                if i == fila_jugador and j == columna_jugador: 
                    print("X ", end="")  # Jugador 
                elif laberinto[i][j]: 
                    print("O ", end="")  # Meta 
                else: 
                    print(". ", end="")  # Espacio vacío 
            print() 
        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA: 
            print("\n¡Has alcanzado la meta! ¡Felicidades!") 
            break 
        movimiento = input("\nIngrese movimiento (w: arriba, s: abajo, a: izq, d: der): ") 
        if movimiento == '2' and fila_jugador > 0: 
            fila_jugador -= 1 
        elif movimiento == '1' and fila_jugador < FILAS - 1: 
            fila_jugador += 1 
        elif movimiento == 'a' and columna_jugador > 0: 
            columna_jugador -= 1 
        elif movimiento == 'd' and columna_jugador < COLUMNAS - 1: 
            columna_jugador += 1 
        else: 
            print("Movimiento no válido.") 
if __name__ == "__main__": 
    main()
    #git add .
    # git commit -m"
    #git push

    #git push origin main