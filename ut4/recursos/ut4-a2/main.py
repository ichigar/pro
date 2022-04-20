#!/usr/bin/python3

from tkinter import *
from opcion1 import *

class Main:
    
    def __init__(self):
        self.__iniciar()
    
    def __iniciar(self):
        self.main_w = Tk()
        self.main_w.title("programa principal")
        self.main_w.geometry('350x200')

        self.lbl = Label(self.main_w, text="Programa principal", font=("Arial Bold", 20))
        self.lbl.grid(column=0, row=0)

        self.btn_1 = Button(self.main_w, text="Opción 1", font=("Arial Bold", 12), command = self.__btn_1_click)
        self.btn_1.grid(column=0, row=1)

        self.btn_2 = Button(self.main_w, text="Opción 2", font=("Arial Bold", 12), command = self.__btn_2_click)
        self.btn_2.grid(column=0, row=2)

        self.lbl_r = Label(self.main_w, text="", font=("Arial", 12))
        self.lbl_r.grid(column=0, row=3)

        self.main_w.mainloop()
        
    def __btn_1_click(self):
        self.lbl_r.configure(text = "Seleccionada opción 1")
        opcion1 = Opcion1()
    
    def __btn_2_click(self):
        self.lbl_r.configure(text = "Seleccionada opción 2")
        
if __name__ == '__main__':
    main = Main()