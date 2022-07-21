from tkinter import Toplevel, Label, PhotoImage
from Widgets import CentrarVentanas
class VentanaColores:
    def __init__(self, master, img) -> None:
        self.colores = Toplevel(master)
        # ----- Background ----- #
        imagen = PhotoImage(file = img)
        Label(self.colores, image=imagen, bd=0).pack()
        # ---- Centra la ventana ----  #
        CentrarVentanas(self.colores)
        # ----- Despueés de 2 segundos destruye la ventana. ----- #
        self.colores.after(2000, self.destroyer)
        self.colores.mainloop() # para que no se destruya la imagen del fondo

    def destroyer(self):
        self.colores.destroy()