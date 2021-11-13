# Terminar-el-Juego

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/alexlomu/Terminar-el-Juego)
https://github.com/alexlomu/Terminar-el-Juego.
Hemos creado un juego de adivinar un número generado al azar dentro de unos parámetros con diferentes niveles de dificultad y dos modos de juego, el primero en el que es el jugador quien intenta adivinar el número y el segundo en el que es la Inteligencia Artificial quien ha de adivinar este número.
El diagrama de flujo que tenemos en nuestro código es el siguiente:
![terminar trabajo figma 1](https://user-images.githubusercontent.com/91721507/141656409-fd150a9c-0701-40be-b3d5-d7e77f071d13.JPG)
![terminar trabajo figma 2](https://user-images.githubusercontent.com/91721507/141656415-d2ebcb91-b3da-4e7a-966e-415283e071aa.JPG)

El código del juego es el siguiente:
```import random
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

def modo():
    print("Modo de juego 1: Juega usted")
    print("Modo de juego2: Juega la IA")
    modo = int(input("Introduce al modo que quieras jugar(1-2)"))
    global modo_escogido
    modo_escogido = modo
    if modo_escogido == 1:
        print("Has escogido el modo de juego 1")
    if modo_escogido == 2:
        print("Has escogido el modo de juego 2")
    if 2 > modo_escogido < 1:
        print("Escoge un modo de juego válido(1-2)")
    return modo_escogido

            
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

def comparar_numeros_ia(num_min, num_max, jugadas_max):
    jugadas = 0
    while jugadas <= jugadas_max:
        x = num_max + num_min
        numero_ia = int(x/2)
        print("La IA ha probado con", str(numero_ia))
        jugadas += 1
        if numero_ia < numero:
            print("El número probado es demasiado pequeño, la IA lleva", str(jugadas), "intentos")
            num_min = numero_ia
        elif numero_ia > numero:
            print("El número probado es demasiado grande, la IA lleva", str(jugadas), "intentos")
            num_max = numero_ia
        elif numero_ia == numero:
            break
    if jugadas == jugadas_max:
        print("Vaya, se le han acabado los intentos a la IA")
    if numero_ia == numero:
        print("La IA ha adivinado el número!, ha usado", str(jugadas), "intentos")


dificultad()    
if nivel == 1:
    numero = random.randint(0,100)
    jugadas_max = 10
    num_min = 0
    num_max = 100
    modo()
    modo = modo_escogido
    if modo == 1:
        comparar_numeros()
    if modo == 2:
        comparar_numeros_ia(0,100, 10)
elif nivel == 2:
    numero = random.randint(0,1000)
    jugadas_max = 20
    num_min = 0
    num_max = 1000
    modo()
    modo = modo_escogido
    if modo == 1:
        comparar_numeros()
    if modo == 2:
        comparar_numeros_ia(0,1000, 20)
elif nivel == 3:
    numero = random.randint(0,1000000)
    jugadas = 0
    jugadas_max = 50
    num_min = 0
    num_max = 1000000
    modo()
    modo = modo_escogido
    if modo == 1:
        comparar_numeros()
    if modo == 2:
        comparar_numeros_ia(0,1000000, 50)    
elif nivel == 4:
    numero = random.randint(0,1000000000000)
    jugadas = 0
    jugadas_max = 100
    num_min = 0
    num_max = 1000000000000
    modo()
    modo = modo_escogido
    if modo == 1:
        comparar_numeros()
    if modo == 2:
        comparar_numeros_ia(0,1000000000000, 100) 
