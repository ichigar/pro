# PRO-UT1-AR2-Repaso/refuerzo-Funciones-listas-cadenas

## Actividades

1. Función se le pasa una letra y una secuencia de palabras y 

a) devuelve el número de palabras que empiezan por dicha letra

```python
def num_palabras_letra(letra, *nombres):
    cont = 0
    for i in nombres:
        if i[0] == letra:
            cont += 1
    return cont



resultado = num_palabras_letra("a", "pepe", "juan", "antonio", "aluisa", "ana")
print(resultado)
```

b) devuelve una lista con todas las palabras que empiezan por dicha letra

```python
def num_palabras_letra(letra, *nombres):
    l = len(nombres)
    resultado = []
    for i in range(l):
        aux = nombres[i]
        if aux[0] == letra:
            resultado.append(aux)
    return resultado


c = "a"

resultado = num_palabras_letra(c, "pepe", "juan", "antonio", "aluisa", "ana")
print(resultado)
```

c) muestra las palabras que empiezan por dicha letra

```python
def num_palabras_letra(letra, *nombres):
    l = len(nombres)
    for i in range(l):
        aux = nombres[i]
        if aux[0] == letra:
            print(aux)

c = "a"

num_palabras_letra(c, "pepe", "juan", "antonio", "aluisa", "ana")
```



3. El "L3N6U4J3 H4CK3R" (o "lenguaje hacker") se originó por la necesidad de los internautas de escribir palabras que estaban censuradas en los motores de búsqueda. Para emplear este lenguaje debemos reemplazar la mayor cantidad de letras por números basándonos en su parecido físico, tal y como se detalla a continuación:

    La 'O' es un 0 (cero).
    La 'A' es un 4 (cuatro).
    La 'E' es un 3 (tres).
    La 'I' es un 1 (uno).
    La 'S' es un 5 (cinco).
    La 'T' es un 7 (siete).
    La 'G' es un 6 (seis).
    La 'B' es un 8 (ocho).

Función que recibe un mensaje de texto y lo devuelve:
* transformado a mayúsculas 
* cifrado empleando para ello el Lenguaje del Hacker.

```python
def to_hacker(texto):
    texto = texto.upper()
    texto = texto.replace("O", "0")
    texto = texto.replace("A", "4")
    texto = texto.replace("E", "3")
    texto = texto.replace("I", "1")
    texto = texto.replace("S", "5")
    texto = texto.replace("T", "7")
    texto = texto.replace("G", "6")
    texto = texto.replace("B", "8")
    return texto

prueba = "este texto contiene varias letras convertibles"
print(to_hacker(prueba))
```

4. Función se le pasa una lista de valores y genera lista HTML de la misma

```python
def lista_html(nombres):
    html = "<ul>\n"
    for i in nombres:
        html += f"\t<li>{i}</li>\n"
    html += "</ul>"
    return html

nombres = ["pepe", "juan", "antonio", "aluisa", "ana"]

resultado = lista_html(nombres)
print(resultado)
```
5. Función se le pasa lista de listas y genera lista y sublista en HML

* La lista será del tipo:
```python
items = ["compra", ["agua", "leche", "jamón", "agua"], "limpieza", ["baño", "salón"], "estudiar", ["dpl", "ets", "fol - nóminas", "ets"]]
```
* Todos los elementos tendrán la primera letra en mayúscula y el resto en minúscula
* Si algún elemento de la sublista está repetido se eliminará y solo aparecerá una vez
```python
def eliminar_repetidos_l(items):
    aux = []
    for i in items:
        if i not in aux:
            aux.append(i)
    return aux

def lista_html(ull):
    l = len(ull)
    html = "<ul>\n"

    for i in range(l):
    
        if i % 2 == 0:
    
            html += f"\t<li>{ull[i].title()}\n"
    
        else:
    
            sublista = eliminar_repetidos_l(ull[i])
        
            html += "\t\t<ul>\n"
    
            for j in sublista:
    
                html += f"\t\t\t<li>{j.title()}</li>\n "
    
            html += "\t\t</ul>\n"
            html += "\t</li>\n"
    html += "</ul>"
    return html

items = [
    "compra", 
    ["agua", "leche", "jamón", "agua"], 
    "limpieza", 
    ["baño", "salón"], 
    "estudiar", 
    ["bae", "ets", "fol - nóminas", "ets"]
    ]

resultado = lista_html(items)
print(resultado)

```
6. Lista y sublista en lenguaje hacker

Modifica el apartado anterior de forma que las palabras de la lista se muestren usando el lenguaje hacker

Resultado:

```python

```

7. Escribe una función en Python que recibe como argumentos dos listas y devuelva `True` si tienen, al menos, un elemento en común.

Resultado:

```python

```

8. Escribe una función en Python a la que le pasemos una lista de elementos y devuelva una lista con los mismos elementos, pero ordenados al azar

Resultado:

```python

```
9. Escribe una función en a la que le pasemos dos listas y devuelva una lista con los elementos que no tienen ambas en común

Resultado:

```python

```

10. Diseña una función en Python que genere contraseñas seguras. Como parámetro recibirá el número de caracteres de la contraseña. La contraseña debe contener:

* Caracteres en minúscula
* Caracteres en mayúscula
* Números
* Caracteres especiales (",", ".", "#", "-", "_", "=", "+", "*")

Cada caracter se elaborará de forma aleatoria

Ejemplo:
```
10 -> "Ui4l+w*-as"
```

```python

```

11. Escribe una función a la que le pasemos un número y devuelva el número de dígitos que contiene

Ejemplo

```python
num_digitos(98) -> 2
num_digitos(5000) -> 4
```
Inserta aquí el código

```python
```

12. Escribe una función que compruebe si un PIN que se le pasa como cadena de caracteres es válido o no (devuelve True o False).

Un PIN es válido si tiene contiene 4 números. Sin espacios nin ningún otro tipo de caracter que no sean los números del 0 al 9

```python
valid_pin("3321") -> True
valid_pin("a345") -> False
valid_pin("67443") -> False
```

 Inserta aquí el código

```python
```



###### tags: `pro` `ut1` `actividad` `refuerzo` `funciones` `listas` `cadenas`