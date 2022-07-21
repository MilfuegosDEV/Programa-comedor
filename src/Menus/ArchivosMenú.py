
from tkinter import Tk, Toplevel, PhotoImage, Label, filedialog
from tkinter.messagebox import askyesno
from modules import resource_path
from Widgets import Boton, CentrarVentanas
import os

class RevisarArchivos:
    """
    Ventana del botón revisar archivos.
    """
    def __init__(self, master, filename: str = '', foldername:str = str):
        self.master = master
        self.master.withdraw()
        self.Archivos = Toplevel(master)
        # ----- Background  ----- #        
        imagen = PhotoImage(file = resource_path(r'src\resources\images\ArchivosMenú.png'))
        Label(self.Archivos, image=imagen, bd=0).pack()
        # ----- Botones ----- #
        Boton(master = self.Archivos, 
                text = "Revisar\nreportes", 
                width = 15, 
                x = 200, 
                y = 270, 
                command= lambda: self.AbrirReportes(foldername))
        
        Boton(master = self.Archivos, 
                text = 'Base\nde datos',
                width = 15,
                x = 627,
                y = 270,
                command= lambda: os.startfile(filename))
        # ----- Botones de navegacíon ------ #
        Boton(master = self.Archivos, 
                text = 'Atrás', 
                width = 20, 
                x = 20, 
                y = 570, 
                command= lambda: self.atras(self.master, self.Archivos),
                fontTuple = ('Comic Sans Ms', 9))

        # ----- Cerrando ventana ----- #
        self.Archivos.wm_protocol('WM_DELETE_WINDOW', (self.cerrar))
        # ----- Posicionando la ventana en la pantalla ----- #
        CentrarVentanas(self.Archivos)
        self.Archivos.mainloop() # para que no se destruya la imagen.
        
        
    def atras(self, master, Toplevel):
        
        master.deiconify()
        Toplevel.destroy()
        
    def cerrar(self):
        
        question = askyesno('¿Salir?', '¿Esta seguro/a que desea salir del programa?')
        if question == True:
            self.master.destroy()
        else:
            pass
    
    def AbrirReportes(self, foldername: str):
        """
        Abre los reportes que estan en la carpeta indicada.
        """
        Reportes = filedialog.askopenfilenames(initialdir=foldername,
                                               title = 'Mover',
                                               filetypes=(('Excel files', '.xlsx'), ('All', '.')))
        
        for files in Reportes:
            try:
                os.startfile(files)
            except:
                pass



# Test
if __name__ == "__main__":
    app = Tk()
    RevisarArchivos(app)
    app.mainloop()