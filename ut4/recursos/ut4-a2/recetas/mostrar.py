from tkinter import *
from tkinter import messagebox

from receta import *

class MostrarReceta:
    def __init__(self):
        self._iniciar()
        
    def _iniciar(self):
        self.op1_w = Tk()
        self.op1_w.title("Mostrar Receta")
        self.op1_w.geometry("400x300")
        
        self.lbl = Label(self.op1_w, text="Mostrar Receta\n", font=("Arial Bold", 12))
        self.lbl.grid(column=0, row=0)

        self.lbl_n = Label(self.op1_w, text="Nombre de la receta:", font=("Arial", 12))    
        self.lbl_n.grid(column=0, row=1)
        
        self.txt_n = Entry(self.op1_w, width=25)
        self.txt_n.grid(column=1, row=1)
        
        self.btn = Button(self.op1_w, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=3)
        
            
        
        self.op1_w.mainloop()
        
    def _form1_enviar(self):
        nombre = self.txt_n.get()
        if nombre == "":
            messagebox.showerror("error", "No se ha introducido ningún valor")
        else:
            receta = Receta()
            text_receta = receta.mostrar_receta(nombre)
            if not text_receta:
                messagebox.showerror("error", "La receta no existe")
            else:
                messagebox.showinfo(nombre, text_receta)