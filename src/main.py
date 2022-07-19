from tkinter import Label, PhotoImage, Tk
from Widgets import Botones, CentrarVentana, RevisarArchivos, IngresoMenú
from modules import resource_path

from modules.Files import xlFiles

class App:
    xlF = xlFiles(dir=r'\SistemaComedor', Archivo ='Comedor.xlsx')
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Comedor') 
        # ----- Icono ----- #
        self.root.wm_iconbitmap(True, resource_path(r'src\resources\icon\icono.ico')) # icono de la app
        # ----- Background  ----- #
        imagen = PhotoImage(file = resource_path(r'src\resources\images\MenúPrincipal.png'))
        Label(self.root, image=imagen, bd=0).pack()
        # ----- Botones ----- #
        Botones(master = self.root, 
                text = "Revisar\narchivos", 
                width = 15,
                x = 200, 
                y = 270, 
                command = lambda: self.validacion(RevisarArchivos(self.root, self.xlF.filename, self.xlF.foldername)))
        
        Botones(master = self.root, 
                text = 'Ingresar\nCédulas.',
                width = 15,
                x = 627,
                y = 270, 
                command = lambda: self.validacion(IngresoMenú(self.root)))
        
        # Centra la ventana.
        CentrarVentana(self.root)
        self.root.mainloop()

    def validacion(self, action: object):
        """
        Cuando alguien presiona un botón verifica la información.
        """
        if self.xlF.VerificacionDeDatos() == True:
            action
        else:
            pass
if __name__ == '__main__':
    app = App()