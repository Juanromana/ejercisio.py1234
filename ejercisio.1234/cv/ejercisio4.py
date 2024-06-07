# triqui
tri=[ " " for j in range(9)] #tablero
def prin_triqui ():
    # print(tri[0] +'|' + tri[1] +'|' + tri[2]+'|')
    # print(tri[3] +'|' + tri[4] +'|' + tri[5]+'|')
    # print(tri[6] +'|' + tri[7] +'|' + tri[8]+'|')
    for j in range(3):
        fila= f"| {tri[j*3 ]}| {tri[j*3+1 ]}| {tri[j*3+2 ]}|"
        print(fila)
def jugador(turno):
    if turno == "x":
        num=1
    else:
        num=2
    print(f"\nTu turno jugador #{num}")
    while True:
        try:
            validacion=int(input("Ingrese su movimento del (1 - 9)\n").strip())
            if validacion >= 1 and validacion <= 9:
                if tri [validacion-1]==" ":
                    tri[validacion-1]=turno+""
                    break
                else:
                    print("el espacio esta ocupado ingrese nuevamente \n")
            else:
                print("movimiento invalido, Ingrese un numero valido 1 al 9 \n")
        except ValueError:
            print("movimiento invalido \n") 
def ganador(gane):
    if((tri [0] == gane and tri [1]==gane and tri [2]==gane)
        or(tri [3] == gane and tri [4]==gane and tri [5]==gane)
        or(tri [6]==gane and tri [7]==gane and tri [8]==gane)
        or(tri [0] == gane and tri [3]==gane and tri [6]==gane)
        or(tri [1] == gane and tri [4]==gane and tri [7]==gane)
        or(tri [2]==gane and tri [5]==gane and tri [8]==gane)
        or(tri [0] == gane and tri [4]==gane and tri [8]==gane)
        or(tri [2] == gane and tri [4]==gane and tri [6]==gane)
    ):
        return True
    else:
        return False
def empate():
    if " " not in tri:
        return True
    else:
        return False

while True:
    prin_triqui()   
    jugador('x')
    if ganador('x'):
        prin_triqui()
        print("felicidades has ganado jugador 1")
        break
    elif empate():
        prin_triqui()
        print('Es un empate')
        break
    prin_triqui()
    jugador('o')
    if ganador('o'):
        prin_triqui()
        print("felicidades has ganado jugador 2")
        break
    elif empate():
        prin_triqui()
        print("es un empate")
        break