# ¿Qué es Python?
Python es un lengujae de programacion que tiene un extenso uso, por lo cual se ha convertido en una herramienta indispensable en la ingenieria  y la ciencia de datos. La claridad y legibilidad de su estructura, combinadas con la diversidad de bibliotecas y marcos de trabajo disponibles, lo convierten en una opción excelente tanto para aquellos que están comenzando como para programadores con experiencia. Python ha probado ser versátil y eficaz en una amplia gama de aplicaciones, desde el desarrollo web hasta la inteligencia artificial.
## Variables que usa Pyton
Python es un lenguaje de programación de tipado dinámico. Algunos de los tipos de variables de Python son:

	**Enteros (int):** Son números enteros, positivos o negativos, sin decimales 	|(1,2,3...)
   
	- **Flotantes (float):** Son números decimales, positivos o negativos (1.1, -1.1).
   
	- ** Cadenas de caracteres (str): ** Es texto (Robotica).

	- ** Booleanos (bool): ** Son valores de verdad:`True` (verdadero) o `False` (falso).
   
   	- ** Listas: ** Son colecciones ordenadas y modificables de elementos de cualquier tipo (lista = [1, 2, 3, 4]).

	- ** Tuplas: ** Tambien son colecciones ordenadas e inmutables de elementos de cualquier tipo (tupla = (1, 2, 3)).

	 - ** Conjuntos (set): ** Igual sonj colecciones no ordenadas de elementos únicos (conjunto = {1, 2, 3}).

Estos son algunos de los tipos de variables más utilizados en Python.


## BUCLE FOR 

Un bucle 'for' se utiliza para iterar sobre una secuencia (como una lista, tupla, conjunto o cadena de caracteres) o cualquier objeto iterable. Su estructura del 'for' es:

'''
for elemento in secuencia:
    # Codigo dentro del for 
'''

## BUCLE WHILE 

Un bucle 'while' se utiliza para repetir un bloque de código mientras se cumpla una condición específica. Su estructura del 'while' es:

'''
while condicion:
    # Código dentro del while
'''

Listas

Una 'lista' es una colección ordenada y mutable de elementos. Esto significa que puedes almacenar una secuencia de elementos en una lista y modificarla según sea necesario. La estructura de una 'lista' es:

	'''
    nombre_de_lista = [elemento1, elemento2, elemento3, ...]
    '''

## Sentencia if - else 

El 'if-else' se utiliza para tomar decisiones en función de una condición, esto ejecuta un bloque de código si la condición especificada es verdadera y otro bloque de código si la condición es falsa. La estructura de 'if-else' es:

'''
	if condicion:
    # Código a ejecutar si la condición es verdadera
	else:
    # Código a ejecutar si la condición es falsa
'''

## Operadores

Los 'operadores' son símbolos especiales que se utilizan para realizar operaciones en variables y valores. Estos operadores se dividen en diferentes categorías según la función que realizan. Los operadores son:

	- ** Operadores aritmeticos: ** `+`, `-`, `*`, `/`, `//`,`%`
	
	Operadores de comparacion: `==`, `!=`, `<`, `>`, `<=`, `>=`.
	
	Operadores logicos: `and`, `or`, `not`.

	Operadores de asignacion: `=`, `+=`, `-=`.



# Explicacion de codigos

A conticuacion se explicara la funcion de los codigos realizados.

## Codigo 1: 
En este código existe una función llamada `problema1` que calcula la suma de los primeros `n` números naturales, donde `n` es un número proporcionado por el usuario. El usuario es solicitado a introducir un número `n`. Una vez que el usuario proporciona este valor, se calcula la suma de los primeros `n` números naturales utilizando la fórmula de la suma de una progresión aritmética. La suma se imprime en la consola. Finalmente, la función devuelve el control al programa principal. La función `problema1()` es llamada al final del código.

## Codigo 2:
Se calcula la paga de un trabajador multiplicando el número de horas trabajadas por el costo por hora. Primero, se solicita al usuario ingresar el número de horas trabajadas y el costo por hora a través de la entrada estándar. Una vez que el usuario proporciona estos valores, se calcula la paga multiplicando el número de horas trabajadas por el costo por hora. La paga se imprime en la consola junto con un mensaje. Finalmente, la función devuelve el control al programa principal. La función `problema2()` es llamada al final del código.

## Codigo 3:
Se calcula el sueldo total a pagar a varios trabajadores en base a sus sueldos por hora y horas trabajadas. Se define una lista llamada `Lista` que contiene sublistas con el nombre del trabajador, su sueldo por hora y las horas trabajadas respectivamente. Luego, se realiza un bucle `for` que itera sobre cada sublista dentro de `Lista`. Dentro de este bucle, se extraen los valores de nombre, sueldo por hora y horas trabajadas de cada sublista y se calcula el sueldo total multiplicando el sueldo por hora por las horas trabajadas. Finalmente, se imprime el nombre del trabajador y el sueldo total a pagar en la consola para cada trabajador. La función `problema3()` es llamada al final del código.

## Codigo 4:
Se realizan operaciones sobre una lista de números. Primero, se crea una lista llamada `numeros` que contiene números del 1 al 10. Luego, se calcula el promedio de los números pares en la lista utilizando una comprensión de lista y la función `sum()` para sumar los elementos y `len()` para obtener la cantidad de números pares. Si no hay números pares, el promedio se establece en 0. A continuación, se calcula el producto de los números impares en la lista utilizando un bucle `for`. Finalmente, se imprimen en la consola la lista original de números, el promedio de los números pares y el producto de los números impares.

## Codigo 5:
Se genera un número aleatorio entre 1 y 10 utilizando la función `randint()` del módulo `random`. Se inicializa un contador de intentos. Luego, se inicia un bucle `while` que se ejecuta indefinidamente. Dentro de este bucle, se solicita al usuario que ingrese un número y se incrementa el contador de intentos en cada iteración. Se verifica si el número ingresado por el usuario es igual al número secreto. Si es así, se imprime un mensaje indicando el número de intentos y se rompe el bucle. Si el número ingresado es menor que el número secreto, se imprime un mensaje indicando que el número es demasiado bajo. Si el número ingresado es mayor que el número secreto, se imprime un mensaje indicando que el número es demasiado alto. Finalmente, la función `problema5()` es llamada.

## Codigo 6:
Se simula un robot moviéndose en una matriz para encontrar un camino desde la esquina superior izquierda hasta la esquina inferior derecha, evitando obstáculos representados por la letra "X". Primero, se importa el módulo `random`. Después, se definen tres funciones auxiliares: `imprimir_matriz`, `imprimir_ruta` y `encontrar_camino`. La función `imprimir_matriz` imprime la matriz en la consola, la función `imprimir_ruta` imprime la ruta seguida por el robot, y la función `encontrar_camino` busca recursivamente el camino a través de la matriz, evitando obstáculos y marcando las casillas visitadas. 

Despues, se define el tamaño de la matriz y se crea una matriz con obstáculos aleatorios. Posteriormente, se imprime la matriz inicial. Finalmente, se busca el camino a través de la matriz utilizando la función `encontrar_camino`, mostrando la ruta seguida por el robot en caso de encontrarla, o indicando que es imposible llegar al destino si no se encuentra ningún camino válido. La función `problema6()` es llamada al final del código.






