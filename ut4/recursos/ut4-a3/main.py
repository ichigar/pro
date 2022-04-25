import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class MainApplication():
    def __init__(self, parent):
        self.parent = parent

        self.parent.title("Widgets Tkinter")
        self.parent.minsize(600,400)
        self.parent.resizable(width=False, height=False)

        # Fila 0
        self.etiqueta = tk.Label(self.parent, text="Etiqueta: ", font=("Arial", 12))
        self.entrada = tk.Entry(self.parent, width=10)
        self.etiqueta.grid(padx=5, pady=5, column=0, row=0, sticky="w")
        self.entrada.grid(padx=5, pady=5, column=1, row=0, sticky="w")

        # Fila 1
        self.comboetiqueta = tk.Label(self.parent, text="Combobox: ", font=("Arial", 12))
        self.combo = ttk.Combobox(self.parent)

        self.combo['values'] = ("primer elemento", 2, 3, 4, 5, "Texto")
        self.combo.current(5)  # set the selected item

        self.comboetiqueta.grid(padx=5, pady=5, column=0, row=1, sticky="w")
        self.combo.grid(padx=5, pady=5, column=1, row=1, sticky="w")

        # Fila 2
        self.radetiqueta = tk.Label(self.parent, text="Radiobuttons: ", font=("Arial", 12))
        
        self.radetiqueta.grid(padx=5, pady=5, column=0, row=2, sticky="w")
        
        # Fila 3
        self.v1 = tk.StringVar()
        self.rad1 = ttk.Radiobutton(self.parent, text='First', value=1, var=self.v1)
        self.rad2 = ttk.Radiobutton(self.parent, text='Second', value=2, var=self.v1)
        self.rad3 = ttk.Radiobutton(self.parent, text='Third', value=3, var=self.v1)
        
        self.rad1.grid(padx=5, pady=5, column=0, row=3, sticky="w")
        self.rad2.grid(padx=5, pady=5, column=1, row=3, sticky="w")
        self.rad3.grid(padx=5, pady=5, column=2, row=3, sticky="w")        
        
        # Fila 4
        self.v2 = tk.StringVar()
        self.rad4 = ttk.Radiobutton(self.parent, text='First', value=4, var=self.v2)
        self.rad5 = ttk.Radiobutton(self.parent, text='Second', value=5, var=self.v2)
        self.rad6 = ttk.Radiobutton(self.parent, text='Third', value=6, var=self.v2)

        self.rad4.grid(padx=5, pady=5, column=0, row=4, sticky="w")
        self.rad5.grid(padx=5, pady=5, column=1, row=4, sticky="w")
        self.rad6.grid(padx=5, pady=5, column=2, row=4, sticky="w")

        # Fila 5
        self.cuadro = scrolledtext.ScrolledText(self.parent, width=40, height=5)
        self.cuadro.insert(tk.INSERT, 'You text goes here')
        self.cuadro.grid(padx=5, pady=5, column=0, columnspan=3, row=5, sticky="w")

        # Fila 6
        self.spin = ttk.Spinbox(self.parent, values=(1, 2, 3, 4, 5, 6), width=5 )
        self.spin.set(3)
        self.spin.grid(padx=5, pady=5, column=0, row=6, sticky="w")

        # Fila 7
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("red.Horizontal.TProgressbar", background='red')
        self.bar = ttk.Progressbar(self.parent, length=200, style='red.Horizontal.TProgressbar')
        self.bar['value'] = 0
        self.bar.grid(padx=5, pady=5, column=0, row=7, sticky="w")

if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
