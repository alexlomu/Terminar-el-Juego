import random
def dificultad():
    while True:
        print("Dificultad 1: Número entre 0 y 100(10 intentos)")
        print("Dificultad 2: Número entre 0 y 1000(20 intentos)")
        print("Dificultad 3: Número entre 0 y 1000000(50 intentos)")
        print("Dificultad 4: Número entre 0 y 1000000000000(100 intentos)")
        dificultad_escogida = input("Escoja la dificultad (1-4)")
        try:
            dificultad_escogida = int(dificultad_escogida)
        except:
            pass
        else:
            if 1 <= dificultad_escogida <= 4:
                break
    return dificultad_escogida        
            
def comparar_numeros():
    jugadas = 0
    while True:
        if numero_jugador < num_min or numero_jugador > num_max:
            print("Por favor, introude un número válido.")
            numero_jugador = int(input("\nIntroduce un número del 0 al ", str(num_max)+": \n"))
        if jugadas == jugadas_max:
            print("Se te han acabado los intentos, el número correcto era", str(numero))
            break
        elif numero_jugador < numero:
            jugadas += 1
            print("Demasiado pequeño, llevas", str(jugadas), "intentos")
            numero_jugador = int(input("\nIntroduce un número del 0 al ", str(num_max)+": \n"))
        elif numero_jugador > numero:
            jugadas += 1
            print("Demasiado grande, llevas", str(jugadas), "intentos")
            numero_jugador = int(input("\nIntroduce un número del 0 al ", str(num_max)+": \n"))
        elif numero_jugador == numero:
            jugadas += 1
            print("Felicidades has ganado, el número era", str(numero))
            print("En total has hecho:", str(jugadas), "intentos.")
            break
    




while True:
    dificultad_escogida = 0
    dificultad()
    if dificultad_escogida == 1:
        numero = random.randint(0,100)
        numero_jugador = int(input("Introduce un número del 0 al 100: "))
        jugadas = 0
        jugadas_max = 10
        num_min = 0
        num_max = 100
        comparar_numeros()
    elif dificultad_escogida == 2:
        numero = random.randint(0,1000)
        numero_jugador = int(input("Introduce un número del 0 al 1000: "))
        jugadas = 0
        jugadas_max = 20
        num_min = 0
        num_max = 1000
        comparar_numeros()
    elif dificultad_escogida == 3:
        numero = random.randint(0,1000000)
        numero_jugador = int(input("Introduce un número del 0 al 1000000: "))
        jugadas = 0
        jugadas_max = 50
        num_min = 0
        num_max = 1000000
        comparar_numeros()    
    elif dificultad_escogida == 4:
        numero = random.randint(0,1000000000000)
        numero_jugador = int(input("Introduce un número del 0 al 1000000000000: "))
        jugadas = 0
        jugadas_max = 100
        num_min = 0
        num_max = 1000000000000
        comparar_numeros() 