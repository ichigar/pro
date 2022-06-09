from tkinter import *

class Opcion1:
    def __init__(self):
        self._iniciar()
        
    def _iniciar(self):
        self.op1_w = Tk()
        self.op1_w.title("Opción 1")
        self.op1_w.geometry("400x300")
        
        self.lbl = Label(self.op1_w, text="Opción 1\n", font=("Arial Bold", 12))
        self.lbl.grid(column=0, row=0)

        self.lbl_n = Label(self.op1_w, text="Nombre:", font=("Arial", 12))    
        self.lbl_n.grid(column=0, row=1)
        
        self.txt_n = Entry(self.op1_w, width=25)
        self.txt_n.grid(column=1, row=1)
        
        self.lbl_e = Label(self.op1_w, text="Email:", font=("Arial", 12))    
        self.lbl_e.grid(column=0, row=2)
        
        self.txt_e = Entry(self.op1_w, width=25)
        self.txt_e.grid(column=1, row=2)
        
        self.btn = Button(self.op1_w, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=3)
        
        self.lbl_r_1 = Label(self.op1_w, text="", font=("Arial", 10))
        self.lbl_r_1.grid(column=0, row=5)    
        
        self.op1_w.mainloop()
        
    def _form1_enviar(self):
        t = f"Nombre: {self.txt_n.get()}\nEmail: {self.txt_e.get()}"
        self.lbl_r_1.configure(text = t)
