# AIA: practica-04.py
# Modelos de Markov
# Dpto. de C. de la Computación e I.A. (Univ. de Sevilla)
#=====================================================================

# ********************************************************************
# Nombre:
# Apellidos:
# ********************************************************************

#   En esta práctica vamos a programar el algoritmo de avance para
# modelos ocultos de Markov (ver tema 4 de teoría). Al final se deja
# para entregar la implementación del algoritmo de Viterbi y un
# ejercicio de representación de un modelo ocultos de Markov

#=====================================================================
# Parte I: Representación: modelos ocultos de Markov
#=====================================================================

#---------------------------------------------------------------------
# Ejercicio 1.1
#---------------------------------------------------------------------

# Definir en primer lugar la clase HMM para la representación en
# Python de los modelos ocultos de Markov.

# La clase ha de constar de los siguientes atributos:

# Atributos:
# * eOcultos: Una lista con los estados que definen la variable oculta
#             del modelo.
#             [s_1, ..., s_n]
# * eObservables: Una lista con los estados que definen la variable
#                 observable del modelo.
#                 [v_1, ..., v_m]
# * pi: Un diccionario, cuyas claves son los estados, y cuyos valores
#       son las probabilidades iniciales:
#                pi[s_i] = P(X_1 = s_i)
# * a: Un diccionario cuyas claves son parejas (tuplas) de estados y
#      cuyos valores son las correspondientes probabilidades de la
#      matriz de transición:
#      a[(s_i, s_j)] = P(X_t = s_j | X_{t-1} = s_i)
# * b: Un diccionario cuyas claves son parejas (tuplas) de estado y
#      observable, y cuyos valores son las correspondientes
#      probabilidades de la matriz de observación:
#      b[(s_i,v_j)] = P(E_t = v_j | X_{t-1} = s_i)

# El constructor de la clase ha de recibir los siguientes datos:

# * Una lista con los estados de la variable oculta.
#   [s_1, ..., s_n]
# * Una lista con las correspondiente probabilidades a priori
#   [P(X_1 = s_1), ..., P(X_1 = s_n)]
# * Una lista de listas representando la matriz de transición
#   [[P(X_t = s_1 | X_{t-1} = s_1), ..., P(X_t = s_n | X_{t-1} = s_1)],
#    ...
#    [P(X_t = s_1 | X_{t-1} = s_n), ..., P(X_t = s_n | X_{t-1} = s_n)]]
# * Una lista con los estados de la variable observable.
#   [v_1, ..., v_m]
# * Un lista de listas representando la matriz de observación
#   [[P(E_t = v_1 | X_t = s_1), ..., P(E_t = v_m | X_t = s_1)],
#    ...
#    [P(E_t = v_1 | X_t = s_n), ..., P(E_t = v_m | X_t = s_n)]]








#---------------------------------------------------------------------
# Ejercicio 1.2
#---------------------------------------------------------------------

# Comprobar a partir de los dos ejemplos de modelo oculto de Markov
# vistos en teoría la correcta definición de la clase anterior.







#=====================================================================
# Parte II: Algoritmo de avance
#=====================================================================

# El algoritmo de avance se define como sigue:

# Entrada: un modelo oculto de Markov y una secuencia
#          de observaciones, o_1, ..., o_t, 
# Salida: probabilidades P(X_t = s_i, E_1 = o_1, ..., E_t = o_t), 
#         1 <= i <= n 

# Inicio: alpha(1,si) = b(i)(o1)pi(i) para 1 <= i <= n
# Para k desde 2 a t:
#    Para j desde 1 a n:
#         alpha(k,sj) = b(j)(ok) * sum([a(i,j) * alpha(k-1, si) 
#                                       para 1 <= i <= n]) 
# Devolver los alpha(t, si) para 1 <= i <= n

# Una vez que se tienen los alpha(t,si), se puede calcular tanto 
# P(E_1 = o_1, ..., E_t = o_t) como  
# P(X_t = s_i | E_1 = o_1, ..., E_t = o_t)
# (respectivamente, sumando y normalizando para i=1,...,n).   

#---------------------------------------------------------------------
# Ejercicio 2.1
#---------------------------------------------------------------------

# Definir la función "avance", que a partir de un modelo oculto de
# Markov y una secuencia de observaciones o_1, ..., o_t, calcule tanto
# la probabilidad de la secuencia de observaciones P(E_1 = o_1,...,
# E_t = o_t), como la lista con las probabilidades P(X_t = s_i | E_1 =
# o_1, ...,E_t = o_t), 1 <= i <= n utilizando adecuadamente el
# algoritmo de avance anteriormente descrito.






#---------------------------------------------------------------------
# Ejercicio 2.2
#---------------------------------------------------------------------

# Definir la función avance_norm que implementa la versión modificada
# del algoritmo de avance, en el que en cada iteración se normalizan
# las probabilidades calculadas. Igual que en el apartado anterior, se
# deben calcular tanto la probabilidad de la secuencia de
# observaciones P(E_1 = o_1,..., E_t = o_t), como la lista con las
# probabilidades P(X_t = s_i | E_1 = o_1, ...,E_t = o_t), 1 <= i <= n.







#---------------------------------------------------------------------
# Ejercicio 2.3
#---------------------------------------------------------------------
    
# Utilizar la función anterior para, en el problema 4 del boletín,
# comprobar la convergencia de la probabilidad de que haya dormido lo
# suficiente la noche anterior para un estudiante muestra todos los
# días los ojos rojos y se duerme en clase,








# Los ejercicios que siguen se proponen como ejercicios entregables.
# El plazo de entrega se anuncia en la página web de la asignatura.

# **************************** IMPORTANTE ****************************
# - PARA LA ENTREGA, NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS
# FUNCIONES QUE SE PIDEN IMPLEMENTAR (si se usa un nombre distinto al
# que se pide en el ejercicio, éste NO se evaluará).
# - Recordar escribir el nombre en la cabecera de este fichero.
# ********************************************************************

# ********************************************************************
# HONESTIDAD ACADÉMICA Y COPIAS: la realización de los ejercicios es
# un trabajo personal, por lo que deben completarse por cada
# estudiante de manera individual.  La discusión y el intercambio de
# información de carácter general con los compañeros se permite (e
# incluso se recomienda), pero NO AL NIVEL DE CÓDIGO. Igualmente el
# remitir código de terceros, obtenido a través de la red o cualquier
# otro medio, se considerará plagio.

# Cualquier plagio o compartición de código que se detecte significará
# automáticamente la calificación de CERO EN LA ASIGNATURA para TODOS
# los alumnos involucrados. Por tanto a estos alumnos NO se les
# conservará, para futuras convocatorias, ninguna nota que hubiesen
# obtenido hasta el momento.
# ********************************************************************

#=====================================================================
# Parte III: Algoritmo de Viterbi
#=====================================================================

# El algoritmo de Viterbi se define como sigue:

# Entrada: un modelo oculto de Markov y una secuencia
#          de observaciones, o_1, ..., o_t, 
# Salida: La secuencia de estados más probable, dadas las
#         observaciones. 

# Este algoritmo está explicado en el tema 4 de teoría:

# Inicio: nu(1,si) = b(i)(o1)pi(i) para 1 <= i <= n
#         pr(1,si) = null
# Para k desde 2 a t:
#    Para j desde 1 a n:
#         nu(k,sj) = b(j)(ok) * max([a(i,j) * nu(k-1, si) 
#                                    para 1 <= i <= n]) 
#         pr(k,sj) = argmax([a(i,j) * nu(k-1, si) para 1 <= i <= n])
# Hacer s = argmax([nu(t,si) para 1 <= i <= n])
# Devolver la secuencia de estados que lleva hasta s

#---------------------------------------------------------------------
# Ejercicio 3.1
#---------------------------------------------------------------------

# Implementar la función viterbi que use el algoritmo anterior a
# partir de un modelo oculto de Markov y una lista de observaciones,
# calcule la lista: [s_1, ..., s_t] con la sucesión de estados más
# probables usando adecuadamente el algoritmo de Viterbi.






#---------------------------------------------------------------------
# Ejercicio 3.2
#---------------------------------------------------------------------

# Utilizar los ejemplos vistos en la teoría para comprobar la correcta
# definición de la función anterior.









#=====================================================================
# Parte II: Problemas de localización
#=====================================================================

# En este apartado se pide aplicar las implementaciones anteriores a
# un problema simple de localización de la posición de un robot que se
# mueve por una cuadrícula.

# Consideremos la siguiente cuadrícula, por la que un robot se
# desplaza (las casillas marcadas con N están bloquedas y no son
# transitables):

#                    Norte
#            1   2   3   4   5   6   7
#          +---+---+---+---+---+---+---+
#        1 | B | R | A | N | B | R | A |
#          +---+---+---+---+---+---+---+
# Oeste  2 | N | N | B | N | R | N | R | Este
#          +---+---+---+---+---+---+---+
#        3 | N | A | B | R | A | N | A |
#          +---+---+---+---+---+---+---+
#                    Sur

# En cada instante, el robot se encuentra en una de las casillas
# (obviamente, excluyendo las casillas bloqueadas), y mirando en una
# dirección (norte, sur, este u oeste).

# El robot puede iniciar su movimiento en cualquiera de las casillas
# libres, con igual probabilidad. En cada instante, el robot puede
# girar (giros de 90, 180, o 270 grados sobre sí mismo) o bien moverse
# hacia el frente (sólo si no está bloqueda la casilla contigua hacia
# la que mira el robot).

# El robot tiene cierta tendencia a moverse hacia el norte. Esto se
# traduce al siguiente modelo probabilístico, que rige las
# transiciones:

# - Si el robot está mirando al norte y la casilla contigua que está
#   al norte no está bloqueada, entonces la probabilidad de avanzar es
#   más del doble que la de cualquier otro movimiento que pueda hacer
#   en esa situación.

# - Si el robot está mirando al norte y la casilla contigua que está
#   al norte está bloqueada, entonces todos los giros son
#   equiprobables.

# - En cucalquier otro caso la probabilidad de girar para mirar al
#   norte es más del doble que la probabilidad de cada una de las
#   otras cosas que pudiera hacer en esa situación. Además, en este
#   caso, la probabilidad de avanzar ha de ser (si la casilla situada
#   frente al robot en la dirección en la que esté mirando no está
#   bloqueada) superior a la del resto de los giros.

# El robot no conoce exactamente ni la casilla en la que está ni hacia
# donde mira. Pero tiene sensores que indican, en cada momento, el
# color de la casilla en la que está y si la casilla siguiente en la
# dirección que está mirando está bloqueda. Lamentablemente, estos
# sensores no son perfectos, y pueden transmitir información errónea.

# El modelo probabilístico que rige lo que detectan los sensores se
# puede describir como sigue:

# - Para cada casilla y dirección hacia la que mira el robot, las
#   observaciones del color y de si hay casilla contigua bloqueada,
#   son independientes.

# - Si una casilla es blanca, la probabilidad de observar "blanca" es
#   de, al menos, 0.8.

# - El robot se confunde bastante entre rojo y azul. Esto quiere decir
#   que si la casilla es roja, observa "roja" con probabilidad 0.5 y
#   "azul" con una probabilidad ligeramente inferior (como mucho un 1
#   por ciento menos). De manera análoga (cambiando rojo por azul) se
#   comportan las observaciones de color cuando la casilla es azul.

# - La observación de obstáculos también funciona mal cuando las
#   casillas son rojas o azules. En ese caso se equivoca, al menos, el
#   35 por ciento de las veces (es decir, de observar que hay
#   obstáculo cuando no lo hay o viceversa). Si la casilla es blanca,
#   el sensor de obstáculos funciona mejor, como mucho se equivoca el
#   5 por ciento de las veces.

#---------------------------------------------------------------------
# Ejercicio 4.1
#---------------------------------------------------------------------

# Representar el laberinto anterior con alguna estructura de datos
# adecuada.


#---------------------------------------------------------------------
# Ejercicio 4.2
#---------------------------------------------------------------------

# Definir una función que recibiendo como entrada el laberinto
# anterior (es decir, la estructura de datos que lo representa),
# devuelva el modelo oculto de Markov (es decir, un objeto de la clase
# HMM) que modela la descripción anterior de transiciones y
# observaciones.





    
    
#---------------------------------------------------------------------
# Ejercicio 4.3
#---------------------------------------------------------------------

# Supongamos la siguiente secuencia de observaciones: azul y libre,
# azul y bloqueado, rojo y bloqueado, azul y libre; y blanco y
# bloqueado.

# a) Proporcionar una estimación de la casilla final más probable en
# la que se encuentra el robot en el momento final.


# b) Proporcionar el camino más probable recorrido.







#---------------------------------------------------------------------
# Ejercicio 4.4
#---------------------------------------------------------------------

# Generar una secuencia de, al menos, cinco estados y su respectiva
# secuencia de observaciones, siguiendo el modelo probabilístico que
# indican las matrices de transición.

# Es decir: elegir la casilla y orientación inicial aleatoriamente,
# según indican las probabilidades de pi. Para cada situación, dar la
# siguiente situación aleatoriamente, pero sujeto a las probabilidades
# de la matriz de transición. Y además en cada estado dar el
# observable igualmente aleatoriamente, pero siguiendo las
# probabilidades de la matriz de observaciones.

# Una vez hecho esto, obtener (con los algoritmos de avance y Viterbi)
# el estado final más probable y la secuencia de estados más probable,
# respecto de la secuencia de observaciones obtenidas.

# Compararla con la verdadera secuencia de estados que ha generado las
# observaciones.
