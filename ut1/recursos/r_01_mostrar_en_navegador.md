# Mostrar HTML en el navegador

## Introducción

Dado que este ciclo está enfocado en el desarrollo de aplicaciones web es interesante que dispongamos de formas de mostrar la salida de nuestros programas en Python en el navegador.

Una forma de hacerlo es utilizando el módulo `webbrowser` de Python que nos permite desde Python abrir el navegador y mostrar una web.

La web la podemos generar a partir de una **URL** o podemos abrir directamente un fichero que contenga HTML.

## Hola mundo en el navegador

El siguiente programa nos muestra como usar la librería `webbrowser` como salida de nuestros programas.

```python
import webbrowser    # Importamos la librería

# Generamos el HTML a mostrar
html = "<h1>Hola mundo</h1>"

# Creamos un fichero con permiso de escritura y guardamos en él el HTML que queremos mostrar
file = open("hola.html", "w")
file.write(resultado)
file.close()

# Abrimos el fichero en una nueva pestaña del navegador predeterminado del sisema
webbrowser.open_new_tab("hola.html")
```

Veremos más adelante con mayor detalle cómo guardar y leer información en archivos, pero este programa lo que hace es guardar en un archivo el HTML que queremos mostrar y posteriormente, usando el método `open_new_tab` del módulo `webbroser` abrimos en una nueva pestaña del navegador el fichero que le pasemos como parámetro.

## Dando estructura a nuestra web

Si queremos mostrar una web con los elementos básicos de HTML5 podemos utilizar una variable que haga de plantilla con el armazón de nuestro HTML e insertar en la misma el contenido a mostrar.

Una forma de hacerlo podría ser:

```python
import webbrowser

# Creamos el HTML que queremos mostrar
titulo = "Página de ejemplo"
nombre_fichero = "hola.html"
contenido = "<h1>Hola. Esto es un ejemplo de página web</h1>"


# Definimos la plantilla de nuestra web
plantilla = f''' 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo}</title>
</head>
<body>
   {contenido}
</body>
</html>
'''
# Creamos fichero con permiso de escritura, le insertamos el contenido y lo cerramos
file = open(nombre_fichero, "w")
file.write(plantilla)
file.close()

# Abrimos el fichero en una nueva pestaña del navegador predeterminado del sisema
webbrowser.open_new_tab(nombre_fichero)
```

La variable plantilla contiene una cadena con formato con el armazón de un documento en HTML5. En dicha variable se sustituirán `titulo` y `contenido` con el texto que generemos en nuestro programa.

A continuación se almacena el texto en la carpeta actual, en un archivo con el nombre almacenado en la variable `nombre_fichero`

Por último usando `open_new_tab()` del módulo `webbroser` abrimos el fichero en el navegador.

## Aplicando estilos

Si además, queremos modificar la apariencia de la web generada aplicando estilos podríamos hacerlo definiendo en una variable de texto los estilos a aplicar e incluirlos en la plantilla

```python
import webbrowser

# Creamos el HTML que queremos mostrar
titulo = "Página de ejemplo"
nombre_fichero = "hola.html"
estilos = '''
h1 {
	color: red;
	font-size: 32px
}
'''
contenido = "<h1>Hola. Esto es un ejemplo de página web</h1>"


# Definimos la plantilla de nuestra web
plantilla = f''' 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo}</title>
  <style>
  	{estilos}
  </style>
</head>
<body>
   {contenido}
</body>
</html>
'''
# Creamos fichero con permiso de escritura, le insertamos el contenido y lo cerramos
file = open(nombre_fichero, "w")
file.write(plantilla)
file.close()

# Abrimos el fichero en una nueva pestaña del navegador predeterminado del sisema
webbrowser.open_new_tab(nombre_fichero)
```

