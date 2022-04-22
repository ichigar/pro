from tkinter import *

class Ingredientes:
    def __init__(self):
        self._iniciar()
        
    def _iniciar(self):
        self.op1_w = Tk()
        self.op1_w.title("Lista de ingredientes")
        self.op1_w.geometry("400x300")
        
        self.lbl = Label(self.op1_w, text="Ingredientes", font=("Arial Bold", 12))
        self.lbl.grid(column=0, row=0)

        ingredientes = ["huevos", "sal", "aceite", "arroz"]
        self.chk_values = {}
        i = 0
        for ingrediente in ingredietes:
            self.chk_values[ingrediente] = BooleanVar # Creamos la variable en la que se almacenará el valor enviado
            self.chk_ingrediente[i] = Checkbutton(op1_w, text=ingrediente, var=chk_values[ingrediente]) 
            self.chkExample.grid(column=0, row = i + 1)

        self.btn = Button(self.op1_w, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=i + 2)
        
        self.lbl_r_1 = Label(self.op1_w, text="", font=("Arial", 10))
        self.lbl_r_1.grid(column=0, row=i + 3)    
        
        self.op1_w.mainloop()
        
    def _form1_enviar(self):
        t = f"Ingredientes seleccionados:"
        for ingrediente in self.chk_values:
            if self.chk_values[ingrediente].get():
                t += f"* {ingrediente}"
        self.lbl_r_1.configure(text = t)
