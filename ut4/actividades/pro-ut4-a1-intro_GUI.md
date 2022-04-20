# UT4-A1. Interfaces gráficas de usuario. GUI
## Elementos curriculares:

**Resulatado de aprendizaje**:

**5.** Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.

**Criterios de evaluación**:

**f**) Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.
**g**) Se han programado controladores de eventos.
**h**) Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.

**Contenidos**:

* Interfaces.
* Concepto de evento.
* Creación de controladores de eventos.

## Conceptos. sobre GUIs

Investiga y contesta a los siguientes apartador

1. **GUI** (Graphical User Interfaz). Interfáz gráfica de usuario. ¿Qué es?

2. Antecedentes históricos. ¿Dónde, cuándo y quíen desarrollo por primera vez una GUI?¿Qué ordenador fue el primero en incluir una?

3. Qué elementos suele incluir una **GUI**

4. Pon ejemplos de sistemas operativos que no usen una **GUI**

5. Es imprescindible utilizar ratón con una **GUI**. Pon ejemplos de **GUI** que no utilicen ratón.

6. ¿Se puede considerar la libreria de Linux **ncurses** como una gui?

7. ¿Qué son los **widgets**? Enumera algunos

8. Dentro del ámbito de las GUI ¿Qué son los eventos?

## Tkinter

9. Para el desarrollo de interfaces gráficos de usuario la mayoría de lenguajes de programación suelen incluir **frameworks** o **módulos**  que facilitan el desarrollo de programas que utilicen una interfaz gráfica de usuario. Python incluye en su librería estándar el módulo **Tkinter** que permite desarrollar de forma relativamente sencilla aplicaciones con interfaz gráfica de usuario.

¿Qué otros frameworks/módulos existen en Python para desarrollar GUIs?

10. ¿Qué ventajas e inconvenientes presenta **Tkinter?

## Práctica guiada

### Primera aplicación con GUI en Python con Tkinter

Lee atentamente la primera parte del siguiente [Tutorial - Construyendo una primera aplicación con GUI en Python con Tkinter](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter)

**Actividad 1** Escribe un programa que genera una ventana que incluya una etiqueta (Label) cuyo contenido sea "Mi primera ventana" 

Inserta el código:

```python

```

Inserta captura de pantalla en el que se muestre el resultado:

> borrar y poner captura

**Complementario**

Investiga en Internet cómo personalizar el título de la **ventana** y que en la barra del título se incluya un icono (descarga uno de Internet y guárdalo en la misma carpeta que el programa). 

También investiga como conseguir que la ventana se pueda redimensional a lo alto, pero no a lo ancho.

Inserta el código:

```python

```

Inserta captura de pantalla en el que se muestre el resultado:

> borrar y poner captura

### Trabajando con Widgets

[Tutorial](https://realpython.com/python-gui-tkinter/#working-with-widgets)

**Actividad 2** Crea una ventana que tenga la siguiente apariencia:

![](https://i.imgur.com/RKD7YCJ.png)

Tener en cuanta que:

* Todos los elementos de la ventarna están dentro de un **Frame**
* El Frame tiene un borde de valor 10 con `relief` de tipo `

Inserta el código:

```python

```

Inserta captura de pantalla en el que se muestre el resultado:

> borrar y poner captura

**Complementario**

Haz que al pulsar el botón se muestre en un **popup** el valor del usuario y la contraseña. Además al pulsar el botón también se borrará el contenido de los campos de entrada.

En el [siguiente tutorial](https://www.geeksforgeeks.org/how-to-create-a-pop-up-message-when-a-button-is-pressed-in-python-tkinter/) se explica como generar popups con **tkinter**

Inserta el código:

```python

```

Inserta captura de pantalla en el que se muestre el resultado:

> borrar y poner captura



## Recursos

* [hektorfrofe: Interfaces gráficas con TKinter](https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/)
* [Realpython: GUI programming con Python](https://realpython.com/python-gui-tkinter/)

###### tags: `pro` `ut4` `gui` `interfaz` `gráfica` `eventos`