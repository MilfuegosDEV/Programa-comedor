from tkinter import Label, PhotoImage, Tk, messagebox
from Widgets import Boton, CentrarVentanas
from modules import resource_path, xlFiles
from Menus import RevisarArchivos, IngresoMenú

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
        Boton(master = self.root, 
                text = "Revisar\narchivos", 
                width = 15,
                x = 200, 
                y = 270, 
                command = lambda: self.validacion("RevisarArchivos"))
        
        Boton(master = self.root, 
                text = 'Ingresar\nCédulas.',
                width = 15,
                x = 627,
                y = 270, 
                command = lambda: self.validacion(""))
        # ----- Cerrando la ventana ----- #
        self.root.protocol('WM_DELETE_WINDOW', self.cerrar)
        # Centra la ventana.
        CentrarVentanas(self.root)
        self.root.mainloop()

    def cerrar(self):
        question = messagebox.askyesno('¿Salir?', '¿Esta seguro/a que desea salir del programa?')
        if question == True:
            self.root.destroy()
        else:
            pass

    def validacion(self, text):
        """
        Cuando alguien presiona un botón verifica la información.
        """
        if self.xlF.VerificacionDeDatos() == True:
            if text == 'RevisarArchivos':
                RevisarArchivos(self.root, self.xlF.filename, self.xlF.foldername)
            else:
                IngresoMenú(self.root, self.xlF.cache, self.xlF.info, self.xlF)
        else:
            pass
    

if __name__ == '__main__':
    app = App()