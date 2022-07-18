from tkinter import Toplevel, Misc, PhotoImage, Label
from Widgets import CentrarVentana, Botones
from modules import resource_path, xlFiles


class RevisarArchivos:
    def __init__(self, master: Misc | None):
        self.Registrar = Toplevel(master)
        # ----- Background  ----- #        
        imagen = PhotoImage(file = resource_path(r'src\resources\images\ArchivosMenú.png'))
        Label(self.Registrar, image=imagen, bd=0).pack()
        # ----- Botones ----- #
        # Todo implementar las funciones de los botones.
        Botones(self.Registrar, "Revisar\nreportes", 15, 200, 270)
        Botones(self.Registrar, 'Archivo\ncon los datos', 15, 627, 270)
        
        # Centra la ventana.
        CentrarVentana(self.Registrar)
        self.Registrar.mainloop() # para que no se destruya la imagen.