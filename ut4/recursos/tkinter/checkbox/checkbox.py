from tkinter import *

class TestChk:
    def __init__(self):
        self._iniciar()
        
    def _iniciar(self):
        self.op1_w = Tk()
        self.op1_w.title("Lista de ingredientes")
        self.op1_w.geometry("400x300")
        
        self.lbl = Label(self.op1_w, text="Ingredientes", font=("Arial Bold", 12))
        self.lbl.grid(column=0, row=0)

        self.chk_example_value = BooleanVar
        self.chk_example = Checkbutton(self.op1_w, text="Ejemplo", var=self.chk_example_value) 
        self.chk_example.grid(column=0, row = 1)

        ingredientes = ["huevos", "sal", "aceite", "arroz"]
        self.chk_values = {}         # Diccionario que almacenará los elementos seleccionados
        self.chk_ingredientes = []   # Almacena checkbuttons
        i = 0
        for ingrediente in ingredientes:
            self.chk_values[ingrediente] = BooleanVar # Creamos la variable en la que se almacenará el valor enviado
            self.chk_ingredientes.append(Checkbutton(self.op1_w, text=ingrediente, var=self.chk_values[ingrediente]))
            self.chk_ingredientes[i].grid(column=0, row = i + 2)
            i += 1

        self.btn = Button(self.op1_w, text="Enviar", font=("Arial", 12), command = self._form1_enviar)
        self.btn.grid(column=1, row=i + 3)
        
        self.lbl_r_1 = Label(self.op1_w, text="", font=("Arial", 10))
        self.lbl_r_1.grid(column=0, row=i + 4)    
        
        self.op1_w.mainloop()
        
    def _form1_enviar(self):
        t = f"Ingredientes seleccionados:"
        if self.chk_example_value.get():
            t += "* Example"
        for ingrediente in self.chk_ingredientes:
            if self.chk_values[ingrediente].get():
                t += f"* {ingrediente}"
        self.lbl_r_1.configure(text = t)

if __name__ == "__main__":
    test_chk = TestChk()
