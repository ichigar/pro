from tkinter import *
from tkinter.ttk import *
from random import randrange
from tkinter import scrolledtext
from tkinter import messagebox
import time
from os import path
from tkinter import filedialog
class Aplicacion(object):

    def __init__(self):
        self.iniciarobjetos()
        self.configurarobjetos()
        self.posicionarobjetos()
        self.ventana.mainloop()

    def iniciarobjetos(self):
        self.ventana = Tk()
        self.texto = StringVar()
        self.texto.set("Examinar....")
        self.etiqueta = Label(self.ventana, text="Etiqueta: ", font=("Arial", 12))
        self.entrada = Entry(self.ventana, width=10)
        self.comboetiqueta = Label(self.ventana, text="Combobox: ", font=("Arial", 12))
        self.combo = Combobox(self.ventana)
        self.boton1etiqueta = Label(self.ventana, text="Abrir ventana nueva: ", font=("Arial", 12))
        self.boton1 = Button(self.ventana, text="Ingresar", command=self.subventana, width=10)
        self.botonexaminaretiqueta = Label(self.ventana, textvariable=self.texto, font=("Arial", 12))
        self.botonexaminar = Button(self.ventana, text="Examinar", command=self.abrir, width=10)
        self.chk_state = BooleanVar()
        self.chk = Checkbutton(self.ventana, text='Apruebo Programación', var=self.chk_state)
        self.v1 = StringVar()
        self.rad1 = Radiobutton(self.ventana, text='First', value=1, var=self.v1)
        self.rad2 = Radiobutton(self.ventana, text='Second', value=2, var=self.v1)
        self.rad3 = Radiobutton(self.ventana, text='Third', value=3, var=self.v1)
        self.v2 = StringVar()
        self.rad4 = Radiobutton(self.ventana, text='First', value=4, var=self.v2)
        self.rad5 = Radiobutton(self.ventana, text='Second', value=5, var=self.v2)
        self.rad6 = Radiobutton(self.ventana, text='Third', value=6, var=self.v2)
        self.msg = Button(self.ventana, text="Mensaje", command=self.mensaje)
        self.cuadro = scrolledtext.ScrolledText(self.ventana, width=40, height=3)
        self.limpiar = Button(self.ventana, text="Limpiar", command=self.eventolimpiar)
        self.spin = Spinbox(self.ventana, values=(4, 3, 6), width=10, )
        self.style = Style()
        self.style.theme_use('default')
        self.style.configure("red.Horizontal.TProgressbar", background='red')
        self.bar = Progressbar(self.ventana, length=200, style='red.Horizontal.TProgressbar')
        self.msg2 = Button(self.ventana, text="Cargar", command=self.carga)

        menu = Menu(self.ventana)
        new_item1 = Menu(menu)
        new_item1.add_command(label='Nuevo')
        new_item1.add_command(label='Abrir', command=self.abrir)
        new_item1.add_command(label='Guardar')
        new_item2 = Menu(menu)
        new_item2.add_command(label='Cortar')
        new_item2.add_command(label='Copiar')
        new_item2.add_command(label='Pegar')
        menu.add_cascade(label='Archivo', menu=new_item1)
        menu.add_cascade(label='Edición', menu=new_item2)
        self.ventana.config(menu=menu)

    def configurarobjetos(self):
        self.ventana.title("Formulario")
        self.ventana.geometry('800x600')
        self.chk_state.set(False)  # set check state
        self.combo['values'] = ("La Laguna", 2, 3, 4, 5, "Texto")
        self.combo.current(5)  # set the selected item
        self.cuadro.insert(INSERT, 'You text goes here')
        self.spin.set(3)
        self.bar['value'] = 0


    def posicionarobjetos(self):
        #Fila 0
        self.etiqueta.grid(padx=5, pady=5, column=0, row=0)
        self.entrada.grid(padx=5, pady=5, column=1, row=0)
        #Fila 1
        self.comboetiqueta.grid(padx=5, pady=5, column=0, row=1)
        self.combo.grid(padx=5, pady=5, column=1, row=1)
        # Fila 2
        self.boton1etiqueta.grid(padx=5, pady=5, column=0, row=2)
        self.boton1.grid(padx=5, pady=5, column=1, row=2)
        # Fila 3
        self.botonexaminaretiqueta.grid(padx=5, pady=5, column=0, row=3)
        self.botonexaminar.grid(padx=5, pady=5, column=1, row=3)
        # Fila 4
        self.chk.grid(padx=5, pady=5, column=0, row=4)
        # Fila 5
        self.rad1.grid(padx=5, pady=5, column=0, row=5)
        self.rad2.grid(padx=5, pady=5, column=1, row=5)
        self.rad3.grid(padx=5, pady=5, column=2, row=5)
        # Fila 6
        self.rad4.grid(padx=5, pady=5, column=0, row=6)
        self.rad5.grid(padx=5, pady=5, column=1, row=6)
        self.rad6.grid(padx=5, pady=5, column=2, row=6)
        # Fila 7
        self.msg.grid(padx=5, pady=5, column=0, row=7)
        # Fila 8
        self.cuadro.grid(padx=5, pady=5, column=0, row=8)
        self.limpiar.grid(padx=5, pady=5, column=0, row=9)

        self.spin.grid(padx=5, pady=5, column=0, row=10)

        self.bar.grid(column=0, row=11)
        self.msg2.grid(column=0, row=12)

    def abrir(self):
        self.files = filedialog.askopenfilenames()
        self.texto.set(self.files)
        #file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

    def mensaje(self):
        messagebox.showinfo('Prueba', 'Hola Mundo')
        messagebox.askquestion('Message title','Message content')
        messagebox.askyesno('Message title','Message content')
        messagebox.askyesnocancel('Message title','Message content')
        messagebox.askokcancel('Message title','Message content')
        messagebox.askretrycancel('Message title','Message content')

    def eventolimpiar(self):
        self.cuadro.delete("1.0", END)

    def carga(self):
        for i in range(100):
            time.sleep(0.01)
            self.bar['value'] = i+1
            self.ventana.update()


    def subventana(self):
        Ventanainterior(self.ventana)

# Clase para otra ventana.

class Ventanainterior(object):
    def __init__(self, v):
        self.ventanaIngresar = Toplevel(v)
        self.ventanaIngresar.title("Ingresar")
        self.ventanaIngresar.geometry("800x600")

        tab_control = Notebook(self.ventanaIngresar)
        self.tab1 = Frame(tab_control)
        self.tab2 = Frame(tab_control)
        tab_control.add(self.tab1, text='Primera')
        tab_control.add(self.tab2, text='Segunda')
        tab_control.pack(expand=1, fill='both')

        self.tabla(self.tab1) # Colocamos tabla en primera pestaña
        v.withdraw() # Ocultar ventana
        self.ventanaPadre = v
        self.ventanaIngresar.protocol("WM_DELETE_WINDOW", self.cerrar)

    def cerrar(self):
        self.ventanaPadre.deiconify() # Recuperar ventana principal
        self.ventanaIngresar.withdraw() # Ocultar ventana interior
        #messagebox.showinfo('Prueba', 'Hola Mundo')

    def tabla(self, tab):
        for r in range(5):
            for c in range(5):
                cell = Entry(tab, width=10)
                cell.grid(padx=5, pady=5, row=r, column=c)
                cell.insert(0, '({}, {})'.format(r, c))

# Programa principal

programa = Aplicacion()

