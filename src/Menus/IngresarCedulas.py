from tkinter import Entry, Toplevel, PhotoImage, Label, messagebox, END
from modules import resource_path, Temp
from Widgets import CentrarVentanas, Boton
from Menus import VentanaColores

class IngresoMenú:
    temp = Temp()
    __hoy = []
    __ingresos = {}
    def __init__(self, master, cache, info, xlF):
        self.master = master
        self.cache = cache
        self.info = info
        self.xlF = xlF

        self.master.withdraw()
        self.RegistraCedulas = Toplevel(master)

        # ----- Background ----- #
        imagen = PhotoImage(file = resource_path(r'src\resources\images\IngresoMenú.png'))
        Label(self.RegistraCedulas, image=imagen, bd=0).pack()

        # ----- Entrada de datos ----- #
        self.entry = Entry(self.RegistraCedulas)
        self.entry = Entry(self.RegistraCedulas, justify='center', font = ('Comic Sans Ms', 40),width= 21, borderwidth=0)
        self.entry.bind('<Return>', self.enter) # cuando se presione la tecla enter el programa ejecutará la función Enter
        self.entry.place(x = 195, y = 266)

        # ----- Botón de navegación ----- #
        Boton(master = self.RegistraCedulas, 
                text = 'Atrás', 
                width = 20, 
                x = 20, 
                y = 570, 
                command= lambda: self.atras(self.master, self.RegistraCedulas),
                fontTuple = ('Comic Sans Ms', 9))

        # ----- Cerrando ventana ----- #
        self.RegistraCedulas.protocol('WM_DELETE_WINDOW', self.cerrar)
        CentrarVentanas(self.RegistraCedulas)
        self.RegistraCedulas.mainloop()
    
    def atras(self, master, toplevel):
        master.deiconify()
        toplevel.destroy()

    def cerrar(self):
        question = messagebox.askyesno('¿Salir?', '¿Esta seguro/a que desea salir del programa?')
        if question == True:
            self.master.destroy()
        else:
            pass
    
    def enter (self, event):
        """
        Cuando alguien presiona enter se verifica que una personas este dentro del archivo
        excel que fue proporcionado anteriormente."""
        try:
            self.DNI = self.entry.get().upper()
        except:
            self.DNI = self.entry.get()

        self.temp.Cargar_info(self.cache) # Carga la información que esta dentro del archivo json
        self.__hoy.clear() # se edita la lista para que no se duplique la información
        self.__hoy.extend(self.temp.tempinfo) # se vuelven a cargar los datos de la lista.
        
        if self.DNI.isalpha() == True or self.DNI.isalnum() == False:
            messagebox.showerror('Error', 'Cédula con caracteres no admitidos.')
            self.entry.delete(0, END)
        else:
            if self.DNI not in self.__hoy:
                self.__hoy.append(self.DNI) # Si la cédula no estaba registrada, se registra.
                if self.DNI in self.info.keys():
                    self.__ingresos[self.DNI] = self.info[self.DNI] # Si la cédula estaba en el archivo excel 
                    self.temp.Editar_info(self.cache, self.__hoy) # modifica el archivo json con la cédula que recién fue insertada.
                    self.xlF.GuardarRegistro(self.__ingresos); self.__ingresos.clear() # Guarda el registro y se borra la información para que no se dupliquen
                    self.entry.delete(0, END) # se borra lo que esta en el campo de texto.
                    VentanaColores(self.RegistraCedulas, r'src\resources\images\PantallaPuedePasar.png')
                else:
                    self.__ingresos[self.DNI] = ('NA', 'NA', 'Estudiante regular') # Si la cédula no esta en el archivo.
                    self.temp.Editar_info(self.cache, self.__hoy)
                    self.xlF.GuardarRegistro(self.__ingresos); self.__ingresos.clear()
                    self.entry.delete(0, END)
                    VentanaColores(self.RegistraCedulas, r'src\resources\images\PantallaTiquete.png')

            else:
                self.entry.delete(0, END)
                VentanaColores(self.RegistraCedulas, r'src\resources\images\PantallaYaComió.png')

