import random
IMÁGENES_AHORCADO = ['''
   +-----+
    |       |
            |
            |
            |
            |
========''', '''
    +-----+
    |        |
   0       |
            |
            |
            |
========''', '''
    +-----+
    |        |
    0       |
   / |       |
             |
             |
========''', '''
    +-----+
    |        |
    0       |
    /|\      |
             |
             |
========''', '''
    +------+
    |          |
    0         |
   /|\         |
   /           |
               |
 ========''', '''
    +------+
    |          |
    0         |
    /|\         |
    / \         |
                |
========= ''' ]

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganzo halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigueña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split() 

def obtenerPalabraAlAzar(listaDePalabras):
    #Esta funcion devuelve una cadena al azar de la lista de cadenas pasada como argumento
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas :', end = ' ')
    for letra in letrasIncorrectas:
        print(letra, end = ' ' )
    print()

    espaciosVacios = '_'  *  len(palabraSecreta)

    for i in range(len(palabraSecreta)):    #Completar los espacios vacios con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] +palabraSecreta[i] + espaciosVacios[i + 1:]

            for letra in espaciosVacios:  # mostrar la palabra secreta con espacios entre cada letra
                print(letra, end = ' ')
        print()

def obtenerIntento(letrasProbadas):
    #Devuelve la letra ingresada por el jugador, verifica que el jugador ha ingresado solo una letra y no otra cosa
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor introdice una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa un LETRA.')
        else:
            return intento

def jugarDeNuevo():
    #Esta funcion devuelve true si el jugador quiere volver a jugar, en caso contrario devuelve false.
    print('¿Quieres jugar de nuevo?(si o no)')
    return input().lower().startswith('s')

print('\t======A H O R C A D O======')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    #Permite al jugador escribir una letra
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        #Verifica si el jugador ha ganado
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras =  False
                break
        if encontradoTodasLasLetras:
            print('¡si! ¡La palabra secreta es ! " ' + palabraSecreta + ' " ¡Has ganado!')
            juegoTerminado = True

    else:
        letrasIncorrectas = letrasIncorrectas + intento

        #comprobar si el jugador ha agotado sus intentos y ha perdido
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespues de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' +str(len(letrasCorrectas)) + ' aciertos, la palabra era " '+  palabraSecreta + ' " ')

            juegoTerminado = True

    #preguntar al jugador si quiere volver a jugar(pero solo si el juego ha terminado)

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
