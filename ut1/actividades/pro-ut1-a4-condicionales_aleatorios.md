# UT1-A3. Estructuras de selección

## Elementos curriculares
**RA1** Reconocer la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.

### Criterios de evaluación
1.a) Identificar los bloques que componen la estructura de un programa informático.

1.c) Utilizar entornos integrados de desarrollo.

1.d) Identificar los distintos tipos de variables y la utilidad específica de cada uno.

1.e) Modificar el código de un programa para crear y utilizar variables.

1.g) Clasificar, reconocer y utilizar en expresiones los operadores del lenguaje.

1.h) Comprobar el funcionamiento de las conversiones de tipo explícitas e implícitas.

1.i) Introducir comentarios en el código.

**RA3** Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

**Criterios de evaluación**

3.a) Ha escrito y probado código que haga uso de estructuras de selección.

3.f) Han probado y depurado los programas.

3.g) Ha comentado y documentado el código.

## Tarea

### Juego 1 dado

Escriba un programa que simule un juego en el que dos jugadores (Fran y Natalia) tiran un dado. El que saque el valor más alto, gana. Si la  puntuación coincide, empatan.

Ejemplo de ejecución :

```
JUEGO DE DADOS
Fran ha sacado un 4.
Natalia ha sacado un 4.
Han empatado.
```

Inserta aquí el programa:

```python

```

### Juego 2 dados

Escriba un programa que simule un juego en el que dos jugadores (Carmen y David) tiran dos dados. El que saque mayor puntuación total, gana. Si  la puntuación total coincide, gana quien haya sacado el dado con el  valor más alto. Si el valor más alto también coincide, empatan.

Ejemplos de ejecución 2:

```
JUEGO DE DOS DADOS
Carmen ha sacado un 4 y un 4.
David ha sacado un 1 y un 5.
Ha ganado Carmen.
```
```
JUEGO DE DOS DADOS
Carmen ha sacado un 2 y un 4.
David ha sacado un 1 y un 5.
Ha ganado David.
```
```
JUEGO DE DOS DADOS
Carmen ha sacado un 3 y un 5.
David ha sacado un 5 y un 3.
Han empatado.
```

Inserta aquí el programa:

```python
```

### BlackJack

Escriba un programa que simule un juego en el que dos jugadores (Gloria y Héctor) sacan tres cartas al azar del 1 al 10. Gana el jugador que obtenga la mayor puntuación total, siempre que no se pase de quince, en cuyo caso el jugador pierde.

Ejemplos de ejecución:

```
BLACK JACK
Gloria ha sacado un 1, un 4 y un 8.
Héctor ha sacado un 8, un 2 y un 3.
Han empatado.
```
```
BLACK JACK
Gloria ha sacado un 8, un 2 y un 1.
Héctor ha sacado un 8, un 7 y un 2.
Ha ganado Gloria.
```
```
BLACK JACK
Gloria ha sacado un 3, un 9 y un 5.
Héctor ha sacado un 8, un 2 y un 6.
No ha ganado nadie.
```
```
BLACK JACK
Gloria ha sacado un 7, un 1 y un 1.
Héctor ha sacado un 4, un 1 y un 8.
Ha ganado Héctor.
```

Inserta aquí el programa:

```python

```

### Piedra, papel ... tijera

Escribe un programa en el que jugarás a piedra, papel ...  tijera contra el ordenador. Se mostrará un menú con la siguiente apariencia:
```
Piedra, papel ... tijera
1 - piedra
2 - papel
3 - tijera
Selecciona un número del 1 a 3 para jugar: 
```
Una vez seleccionado el programa generará un número al azar del 1 al 3 con el que jugará el ordenador. A continuación se mostrará si has ganado, perdido o empatado:.

Ejemplo de ejecución:
```
Piedra, papel ... tijera
1 - piedra
2 - papel
3 - tijera
Selecciona un número del 1 a 3 para jugar: 3
Has seleccionado 3 - tijera
El ordenador ha seleccionado: 2 - papel
¡Has ganado!
```
Inserta aquí el programa:

```python

```
### Piedra, papel ... tijera utilizando random.choice
Modifica el programa del apartado anterior de manera que se seleccione un valor entre "piedra", "papel" y "tijera". Al leer el elemento seleccionado por el jugador deberá de escribir "piedra", "papel" y "tijera" en lugar de seleccionar un número del 1 al 3.
Ejemplo de ejecución:
```
Piedra, papel ... tijera
Introduce tu elección: papel
El ordenador ha seleccionado: papel
¡Has empatado!
```
Inserta aquí el programa:

```python

```
## Complementario
### Piedra, papel, tijera, lagarto, Spock
Amplíe el programa anterior para que juegue a **Piedra, papel, tijera, lagarto, Spock**, una variante inventada por **Sam Kass** y que se popularizó al aparecer en la serie de television The **Big Bang Theory**. Esta variante añade dos elementos más, con la ventaja de que no se producen tantos empates, pero obliga a memorizar más combinaciones.

El esquema siguiente muestra los posibles resultados del juego. La punta de la flecha señala al derrotado.

![](https://www.mclibre.org/consultar/python/img/ejercicios/minijuegos/piedra-papel-tijera-lagarto-spock.svg)

Inserta aquí el programa:

```python

```

## 