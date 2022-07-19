from tkinter import Entry, Toplevel, PhotoImage, Label
from Widgets import CentrarVentana
from modules import resource_path
class IngresoMenú:
    def __init__(self, master):
        
        self.RegistraCedulas = Toplevel(master)
        # ----- Background ----- #
        imagen = PhotoImage(file = resource_path(r'src\resources\images\IngresoMenú.png'))
        Label(self.RegistraCedulas, image=imagen, bd=0).pack()
        
        # ----- Entrada de datos ----- #
        self.entry = Entry(self.RegistraCedulas)
        
        self.entry = Entry(self.RegistraCedulas, justify='center', font = ('Comic Sans Ms', 40),width= 21, borderwidth=0)
        self.entry.bind('<Return>', self.enter) # cuando se presione la tecla enter el programa ejecutará la función Enter
        self.entry.place(x = 195, y = 266)
        
        CentrarVentana(self.RegistraCedulas)
        self.RegistraCedulas.mainloop()

    def enter (self, event):
        print('Hola')