#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from mostrar import *

class Main:
    
    def __init__(self):
        self.__iniciar()
    
    def __iniciar(self):
        self.main_w = Tk()
        self.main_w.title("Gestión de recetas")
        self.main_w.geometry('350x200')

        self.lbl1 = Label(self.main_w, text="Gestión de recetas", font=("Arial Bold", 20))
        self.lbl1.grid(column=0, row=0)
        

        self.btn_1 = Button(self.main_w, text="Mostrar receta", font=("Arial Bold", 12), command = self.__btn_1_click)
        self.btn_1.grid(column=0, row=2)

        self.main_w.mainloop()
        
    def __btn_1_click(self):
        mostrar = MostrarReceta()
    
    # def __btn_2_click(self):
    #     self.lbl_r.configure(text = "Seleccionada opción 2")
    #     messagebox.showwarning("showwarning", "Warning")
    #     messagebox.showinfo("showinfo", "Information")
    #     messagebox.showerror("showerror", "Error")
        
if __name__ == '__main__':
    main = Main()