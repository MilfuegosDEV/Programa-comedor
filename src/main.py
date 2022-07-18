
from tkinter import Label, PhotoImage, Tk
from Widgets import Botones, CentrarVentana
from modules import resource_path
from ArchivosMenú import RevisarArchivos

class App:

    def __init__(self) -> None:
        self.root = Tk()
        
        self.root.title('Comedor') 
        # ----- Icono ----- #
        self.root.wm_iconbitmap(True, resource_path(r'src\resources\icon\icono.ico')) # icono de la app
        # ----- Background  ----- #
        imagen = PhotoImage(file = resource_path(r'src\resources\images\MenúPrincipal.png'))
        Label(self.root, image=imagen, bd=0).pack()
        # ----- Botones ----- #
        Botones(self.root, "Ingresar\nCédulas", 15, 200, 270).Boton.config(command= lambda: RevisarArchivos(self.root))
        Botones(self.root, 'Revisar\nArchivos', 15, 627, 270)
        
        # Centra la ventana.
        CentrarVentana(self.root)
        
        self.root.mainloop()
        
        
if __name__ == '__main__':
    app = App()