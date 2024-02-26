#Laboratorio 1

"""
Joan Carlos Monfil Huitle
id: 172820
Diseño de sistemas roboticos 
"""



#Problema 1 

print (         )

def problema1():

    print ("Problema1")

    n = int(input("Intoduce un numero n:"))

    suma = (n*(n+1)/2)

    print ("La suma es: ")
    print (suma)

    return

problema1 ()
print (         )
print (         )
print (         )
print (         )
print (         )



#Problema 2

print (         )

def problema2():

    print ("Problema2")

    Horas = int(input("¿Cuantas horas trabajo?"))

    Costo = int(input("¿Cuanto cuesta la hora]?"))

    Paga = Horas * Costo
    print ("Su paga es:" + str(Paga) + "$")

    return

problema2 ()
print (         )
print (         )
print (         )
print (         )
print (         )



#Problema 3

print (         )

def problema3():

    print ("Problema3")

    #Lista[NOmbre,sueldo,horas]

    Lista = [
        ["Aldo0", 10, 40],
        ["Aldo1", 12, 35],
        ["Aldo2", 31, 45],
        ["Aldo3", 41, 38],
        ["Aldo4", 17, 42],
        ["Aldo5", 15, 37],
        ]

     # Calculando sueldo
    for Listax in Lista:

        nombre = Listax[0]

        sueldo_por_hora = Listax[1]

        horas_trabajadas = Listax[2]

        sueldo_total = sueldo_por_hora * horas_trabajadas

        print(f"Nombre: {nombre}, Sueldo a pagar: ${sueldo_total}")


    return

problema3 ()
print (         )
print (         )
print (         )
print (         )
print (         )



#Problema 4

print (         )

def problema4():

    print ("Problema4")

    # Crear una lista de al menos 10 números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



    # Calcular el promedio de los números pares
    numeros_pares = [num for num in numeros if num % 2 == 0]
    promedio_pares = sum(numeros_pares) / len(numeros_pares) if numeros_pares else 0



    # Calcular el producto de los números impares
    numeros_impares = [num for num in numeros if num % 2 != 0]
    producto_impares = 1
    for num in numeros_impares:
        producto_impares *= num



    # Imprimir los resultados
    print("Lista de números:", numeros)
    print("Promedio de los números pares:", promedio_pares)
    print("Producto de los números impares:", producto_impares)


    return

problema4 ()
print (         )
print (         )
print (         )
print (         )
print (         )



#Problema 5

print (         )

def problema5 ():
    
    print ("Problema5")

    import random
    
    # Generar un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)

    # Inicializar contador de intentos
    intentos = 0

    # Bucle hasta que el usuario adivine el número secreto
    while True:
        # Solicitar al usuario que ingrese un número
        guess = int(input("Adivina el número secreto (entre 1 y 10): "))
        intentos += 1

        # Verificar si el número ingresado es igual al número secreto
        if guess == numero_secreto:
            print("Número secreto encontrado en", intentos, "intentos")
            break
        # Proporcionar pistas si el número es demasiado alto o bajo
        elif guess < numero_secreto:
            print("El número es demasiado bajo. Inténtalo de nuevo.")
        else:
            print("El número es demasiado alto. Inténtalo de nuevo.")
            
            return

problema5()
print (         )
print (         )
print (         )
print (         )
print (         )



#Problema 6

print (         )

def problema6 ():

    import random

    # Función para imprimir la matriz
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(" ".join(fila))

    # Función para imprimir la ruta
    def imprimir_ruta(ruta):
        for movimiento in ruta:
            if movimiento == "Arriba":
                print("↑", end=" ")
            elif movimiento == "Abajo":
                print("↓", end=" ")
            elif movimiento == "Izquierda":
                print("←", end=" ")
            elif movimiento == "Derecha":
             print("→", end=" ")
        print()

    # Función para encontrar el camino
    def encontrar_camino(matriz, x, y, ruta):
        # Verificar si el robot llegó al destino
        if x == len(matriz) - 1 and y == len(matriz[0]) - 1:
            matriz[x][y] = "X"
            imprimir_matriz(matriz)
            print("Ruta:")
            imprimir_ruta(ruta)
            return True
        
        # Verificar si las coordenadas están dentro de la matriz
        if x < 0 or y < 0 or x >= len(matriz) or y >= len(matriz[0]):
            return False

        # Verificar si la casilla está libre
        if matriz[x][y] == "X":
            return False

        # Marcar la casilla como visitada
        matriz[x][y] = "X"

        # Intentar moverse hacia arriba, abajo, izquierda y derecha
        if encontrar_camino(matriz, x - 1, y, ruta + ["Arriba"]):
            return True
        if encontrar_camino(matriz, x + 1, y, ruta + ["Abajo"]):
         return True
        if encontrar_camino(matriz, x, y - 1, ruta + ["Izquierda"]):
            return True
        if encontrar_camino(matriz, x, y + 1, ruta + ["Derecha"]):
            return True

        # Si no se puede mover en ninguna dirección, desmarcar la casilla y retroceder
        matriz[x][y] = "O"
        return False

    # Tamaño de la matriz
    filas = 5
    columnas = 5

    # Crear la matriz con obstáculos aleatorios
    matriz = [["O" for _ in range(columnas)] for _ in range(filas)]
    for _ in range(filas * columnas // 4):  # aproximadamente 1/4 de la matriz tendrá obstáculos
        obstaculo_fila = random.randint(0, filas - 1)
        obstaculo_columna = random.randint(0, columnas - 1)
        matriz[obstaculo_fila][obstaculo_columna] = "X"
    
    # Imprimir la matriz inicial
    print("Mapa inicial:")
    imprimir_matriz(matriz)

    # Buscar el camino
    print("\nBuscando camino...")
    if not encontrar_camino(matriz, 0, 0, []):
        print("Imposible llegar al destino")

    
    return 

problema6()


