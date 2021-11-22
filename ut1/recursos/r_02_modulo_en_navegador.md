# Módulo para mostrar en navegador salida de programas

## Creando un módulo

Un módulo en python se crea, básicamente, incluyendo en un fichero `.py` los elementos de código que constituyen el módulo. En este caso, si queremos que el módulo se llame **browser_output** creamos un fichero de nombre `browser_output.py` e inserta en el mismo el siguiente contenido:

```python
import webbrowser
def show_in_tab(contenido, estilos = "", titulo = "", nombre_fichero = "test.html"):
    # Creamos el HTML que queremos mostrar
    
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
    # Abrimos el fichero en una nueva pestaña del navegador predeterminado del sistema
    webbrowser.open_new_tab(nombre_fichero)
```

Para poder utilizar la función `show_in_tab()` definida en la librería anterior debemos crear un un fichero `.py` en la misma carpeta en la que está el fichero de la librería. Por ejemplo:

```python
from browser_output import show_in_tab # Importamos la función de la librería
content = "<h1>hola</h1>"
styles = '''
    h1 {
        color: red;
    }
'''
title  = "p prueba"
aux_file = "test.html"
show_in_tab(content, styles, title, aux_file)
```

Salvo el primer parámetro, el resto son opcionales, por tanto es suficiente llamar a la función con el primer argumento (el html a mostrar) como parámetro.
