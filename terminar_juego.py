import random
def dificultad():
    print("Dificultad 1: Número entre 0 y 100(10 intentos)")
    print("Dificultad 2: Número entre 0 y 1000(20 intentos)")
    print("Dificultad 3: Número entre 0 y 1000000(50 intentos)")
    print("Dificultad 4: Número entre 0 y 1000000000000(100 intentos)")        
    dificultad_escogida = int(input("Escoja la dificultad (1-4): "))
    global nivel
    nivel = dificultad_escogida
    if  1 <= nivel <= 4:
        if nivel == 1:
            print("Has escogido el nivel de dificultad simple")
            print("El número esta entre 0 y 100, tienes un total de 10 intentos")
        if nivel == 2:
            print("Has escogido el nivel de dificultad medio")
            print("El número esta entre 0 y 1000, tienes un total de 20 intentos")
        if nivel == 3:
            print("Has escogido el nivel de dificultad avanzado")
            print("El número esta entre 0 y 1000000, tienes un total de 50 intentos")    
        if nivel == 4:
            print("Has escogido el nivel de dificultad experto")
            print("El número esta entre 0 y 1000000000000, tienes un total de 100 intentos")
    else:
        print("Selecciona una dificultad válida")   
          
            
def comparar_numeros():
    jugadas = 0
    while jugadas <= jugadas_max:
        numero_jugador = int(input("Introduce un número: "))
        jugadas += 1
        if numero_jugador < numero:
            print("Demasiado pequeño, llevas", str(jugadas), "intentos")
            
        if numero_jugador > numero:
            print("Demasiado grande, llevas", str(jugadas), "intentos")
            
        if numero_jugador == numero:
            break
    if jugadas == jugadas_max:
        print("Se te han acabado los intentos, el número correcto era", str(numero))
    
    if numero_jugador == numero:
        print("Felicidades has ganado, el número era", str(numero))
        print("En total has hecho:", str(jugadas), "intentos.")


dificultad()    
if nivel == 1:
    numero = random.randint(0,100)
    jugadas_max = 10
    num_min = 0
    num_max = 100
    comparar_numeros()
elif nivel == 2:
    numero = random.randint(0,1000)
    jugadas_max = 20
    num_min = 0
    num_max = 1000
    comparar_numeros()
elif nivel == 3:
    numero = random.randint(0,1000000)
    jugadas = 0
    jugadas_max = 50
    num_min = 0
    num_max = 1000000
    comparar_numeros()    
elif nivel == 4:
    numero = random.randint(0,1000000000000)
    jugadas = 0
    jugadas_max = 100
    num_min = 0
    num_max = 1000000000000
    comparar_numeros() 