# PRO/ETS UT5-A2-Git Undo

Lo interesante de guardar un historial de cambios es que podemos revertir cambios que hayamos realizado en caso de que nos hayamos equivocado e incluso recuperar archivos completos que hayamos eliminado.

La herramienta `git` ofrece diferentes opción para recuperar/deshacer cambios. Vamos a descubrir algunos de ellos mediante la siguiente práctica.

Para resolver las actividades deberás buscar en Internet en manuales y tutoriales.

Recursos:

* [freecodecamp - git reset y revert](https://www.freecodecamp.org/espanol/news/la-guia-definitiva-para-git-reset-y-git-revert/)
* [atlassian - reescribiendo el historial](https://www.atlassian.com/es/git/tutorials/rewriting-history)

## Práctica 

### git amend

#### Actividad 1
Trabajando en un repositorio hemos ejecutado las siguientes acciones:

```bash
$ git init
$ touch fichero.txt
$ echo primera línea >> fichero.txt
$ git add .
$ git commit -m "primera línea en fichero"
```

Queremos cambiar el mensaje del último `commit` y ponerlo en inglés ("first line in file"). 

Investiga cómo hacerlo con la opción `--amend`. Inserta lo que deberías ejecutar:

```bash

```

**Nota**: el log de git nos debería devolver algo como:

```bash
$ git log --oneline              
d4a662c (HEAD -> master) first line in file
```

#### Actividad 2

A continuación, en la misma carpeta ejecutamos las siguientes acciones:

```bash
$ echo segunda línea >> fichero.txt
$ echo "# Título" > README.md
$ git add fichero.txt
$ git commit -m "new line and create README"
```

Al terminar de ejecutar nos damos cuenta de que nos hemos olvidado de añadir `README.md` al último commit. Lo podemos comprobar ejecutando `git log` con la opción `--stat`:

```bash
git log --stat --oneline
error: cannot run off: No existe el archivo o el directorio
b99aea8 (HEAD -> master) new line and create README
 fichero.txt | 1 +
 1 file changed, 1 insertion(+)
d4a662c first line in file
 fichero.txt | 1 +
```

Investiga cómo añadir el fichero `README.md` al último commit (se pide añadirlo al último commit, no crear uno nuevo) sin modificar el mensaje del commit. Inserta lo que deberías ejecutar:

```bash

```

Ahora `git log` debería mostrar algo cómo:

```bash
git log --stat --oneline  
error: cannot run off: No existe el archivo o el directorio
cc7e319 (HEAD -> master) new line and create README
 README.md   | 1 +
 fichero.txt | 1 +
 2 files changed, 2 insertions(+)
d4a662c first line in file
 fichero.txt | 1 +
```

### git reset

#### Actividad 3

Seguimos trabajando en la carpeta y realiazamos las siguientes acciones.

```bash
$ echo linea con error >> fichero.txt
$ git add .
$ git commit -m "wrong line in file"
$ echo fichero a eliminar > wrong_file.txt
$ git add .
$ git commit -m "added wrong file"
$ git log --oneline --stat        
4d42f11 (HEAD -> master) added wrong file
 wrong_file.txt | 1 +
 1 file changed, 1 insertion(+)
c59b135 wrong line in file
 fichero.txt | 1 +
 1 file changed, 1 insertion(+)
cc7e319 new line and create README
 README.md   | 1 +
 fichero.txt | 1 +
 2 files changed, 2 insertions(+)
d4a662c first line in file
 fichero.txt | 1 +
```

Investiga que debemos ejecutar si queremos eliminar las acciones anteriores y que no quede rastra de las mismas en `git`:

```bash

```

Al ejecutar `git log` deberíamos obtener:

```bash
git log --oneline --stat
error: cannot run off: No existe el archivo o el directorio
cc7e319 (HEAD -> master) new line and create README
 README.md   | 1 +
 fichero.txt | 1 +
 2 files changed, 2 insertions(+)
d4a662c first line in file
 fichero.txt | 1 +
```

Y en `fichero.txt` no debería aparecer la última línea que añadimos:

```bash
$ cat fichero.txt 
primera línea
segunda línea
```

### git revert

#### Actividad 4
Investiga y contesta. ¿Qué diferencias hay entre las opciones de `git` `reset` y `revert`?

```
```

#### Actividad 5

Seguimos trabajando en la carpeta y realiazamos las siguientes acciones.

```bash
$ echo base de datos > database.db
$ git add .
$ git commit -m "added database"
$ echo contenido >> README.md
$ git add .
$ git commit -m "added line to README"
```

Si queremos eliminar la base de datos y no hacer seguimiento de la misma. Investiga cómo usando la opción `revert` podemos deshacer dicho paso (el penúltimo) y que quede constancia en el historial de dicho cambio:

```bash

```

El resultado del log de git debería ser de la forma:

```bash
git log --oneline --stat                

09da0f6 (HEAD -> master) Revert "added database"
 database.db | 1 -
 1 file changed, 1 deletion(-)
d92570c added line to README
 README.md | 1 +
 1 file changed, 1 insertion(+)
c6fa6a3 added database
 database.db | 1 +
 1 file changed, 1 insertion(+)
cc7e319 new line and create README
 README.md   | 1 +
 fichero.txt | 1 +
 2 files changed, 2 insertions(+)
d4a662c first line in file
 fichero.txt | 1 +
```

Fíjate que los cambios anteriores se cambiaron en el historial y que se ha añadido un nuevo commit en el que se deshace dicho cambio eliminado la cción de dicho commit que fue añadir el fichero `database.db`

###### tags: `ets` `git` `undo` `reset` `revert` `amend`