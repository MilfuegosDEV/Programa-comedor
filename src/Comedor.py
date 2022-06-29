# Módulos
from tkinter import END, Entry, PhotoImage, Tk, Label, Button, Toplevel, messagebox
from tkinter.filedialog import askopenfilenames; 
from PIL import Image, ImageTk

from openpyxl import load_workbook, Workbook 
from datetime import datetime


from modules.ExcelFiles import ExcelFiles as xlF
from modules.__resource_path import resource_path


UsaronElComedor = {} # Datos de todas las personas que utilizaron el comedor.
CedulasRegistradas = [] # cedulas que fueron registradas durante la ejecución del programa.

ef = xlF('Test')
Font_tuple = ("Comic Sans MS", 20)
file_tuples = ('Excel files', '.xlsx'), ('All files', '.')

def centrar(ventana):
    """Centra cualquier ventana dependiendo el tamaño de la pantalla."""
    ventana.geometry('1066x600') # fija el tamaño de la ventana
    ventana.resizable(False, False) # indica que la ventana no se puede redimensionar
    ventana.update_idletasks() 
    w = ventana.winfo_width() # obtiene el ancho de la pantalla
    h = ventana.winfo_height() # obtiene el alto de la pantalla
    extraW = ventana.winfo_screenwidth()-w
    extraH = ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2)) # posiciona la ventana

def next(ventana):
    """Minimiza la ventana pasada"""
    ventana.withdraw()


def back(cerrar, abrir):
    """Retrocede a la ventana anterior"""
    # se destruye la ventana anterior
    cerrar.destroy()
    # se abre la ventana anterior
    abrir.deiconify()





def Second_win(selection):
    """Crea un nuevo Toplevel dependiendo el boton que se presione"""
    global entry, CedulasRegistradas, top

    def ventana(img):
        """Muestra la ventana dependiendo del grupo que pertenezca la persona\n
        rojo -> Ya comió\n
        amarrillo -> Tiquete\n
        verde -> Puede Pasar"""
        
        global image2
        
        entry.delete(0, END) # Borra todo el texto que se introduce en el cuadro de texto
        color = Toplevel(top)

        image2 = PhotoImage(file=img); image2 = image2.subsample(1,1) # Inserta la imagen correspondiente
        label = Label(color, image=image2)   
        label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
        
        centrar(color)

        def ocultar():
            """Destruye una ventana de colores."""
            color.destroy()
        color.after(2000,ocultar)






    def Enter(event):
        ef.reportsdir('reports')
        """Registra cada una de las cédulas que se van introduciendo"""
        CedulasRegistradas.clear() # Evita que los datos se dupliquen en el registro

        NumeroDeCedula = (entry.get()).upper() 
        try:
            if NumeroDeCedula.isalpha() == False and NumeroDeCedula.isalnum() == True:
                if NumeroDeCedula not in CedulasRegistradas:
                    if NumeroDeCedula in ef.PersonasDelComedor:
                        # Si la persona está dentro del archivo.
                        UsaronElComedor[NumeroDeCedula] = ef.PersonasDelComedor[NumeroDeCedula]
                        colorw = resource_path(r'src\assets\img\green.png')
                        ventana(colorw)
                    else:
                        # Si la persona no esta dentro del archivo.
                        colorw = resource_path(r'src\assets\img\gold.png')
                        ventana(colorw)

                        UsaronElComedor[NumeroDeCedula] = ('Estudiante Regular', 'NA', 'Ventas')
                    CedulasRegistradas.append(NumeroDeCedula)
                else:
                    # Si la cédula ya fue registrada.
                    colorw = resource_path(r'src\assets\img\red.png')
                    ventana(colorw)

                # Guarda el registro
                ef.GuardarRegistro(UsaronElComedor)
                UsaronElComedor.clear()# se resetea el diccionario
            elif NumeroDeCedula.isalpha() == True:
                messagebox.showerror('Error', 'Tiene que estar en formato alfanúmerico.')
                
            elif '' in NumeroDeCedula:      
                messagebox.showerror('Error', 'No se permiten espacios y otros caracteres que no sean letras o números.')

            entry.delete(0, END)
        except Exception as e:
            messagebox.showerror('Error', f'Ha ocurrido {e}')







    if ef.VerificacióndeArchivos('Comedor.xlsx') is True:
        global top
        next(root)

        if selection == 'InsertarCédulas':
            # ventana secundaria
            top = Toplevel(root)

            # Fondo de la ventana secundaria.
            img = resource_path(r'src\assets\img\INS.png')
            image = Image.open(img)
            tk_image = ImageTk.PhotoImage(image)
            Label(top, image = tk_image ).pack() # establece el fondo de la ventana

            # Cuadro de texto.
            entry = Entry(top, justify='center', font = ('Comic Sans Ms', 40),width= 21, borderwidth=0)
            entry.bind('<Return>', Enter) # cuando se presione la tecla enter el programa ejecutará la función Enter
            entry.place(x = 195, y = 266)

            
        elif selection == 'AbrirBaseDeDatos':
            # Ventana secundaria
            top = Toplevel(root)

            # Fondo de la ventana secundaria.
            img = resource_path(r'src\assets\img\archivos.png')
            imagen = PhotoImage(file = img)
            Label(top, image= imagen, bd = 0).pack() # establece el fondo de la ventana

            # Botones
            Reportes = Button(top)
            Bases = Button(top)

            # Configuración de los botones
            Reportes.config(
                            text= 'Revisar\nreportes', 
                            font = Font_tuple, 
                            width= 15, 
                            background='#ffffff', 
                            activebackground='#ffffff', 
                            foreground='black', 
                            activeforeground='black', 
                            borderwidth= 0, 
                            relief='raised', 
                            overrelief='sunken',
                            command=lambda: ef.openfiles('revisar reportes')
            )

            Bases.config(
                        text= 'Abrir\nbase de datos', 
                        font = Font_tuple, 
                        width= 15, 
                        background='#ffffff', 
                        activebackground='#ffffff', 
                        foreground='black', 
                        activeforeground='black', 
                        borderwidth= 0, 
                        relief='raised', 
                        overrelief='sunken', 
                        command=lambda: ef.openfiles('abrirbase')
            )

            # Poscicionamientos de los botones
            Reportes.place(x = 199, y = 270)
            Bases.place(x = 627, y = 270)

        # Botones
        cerrar = Button(top)
        atras = Button(top)

        # Configuración de los botones
        atras.config(

                    text= 'Atrás', 
                    font = 'Comic_Sans_Ms 9', 
                    width= 20, 
                    background='#f0f0f0', 
                    activebackground='#f0f0f0', 
                    foreground='black', 
                    activeforeground='black', 
                    borderwidth= 2,
                    relief='raised', 
                    overrelief='sunken', 
                    command=lambda: back(top, root)
        )

        cerrar.config(

                    text= 'Cerrar', 
                    font = 'Comic_Sans_Ms 9', 
                    width= 20, 
                    background='#f0f0f0', 
                    activebackground='#f0f0f0', 
                    foreground='black', 
                    activeforeground='black', 
                    borderwidth= 2,
                    relief='raised', 
                    overrelief='sunken', 
                    command=lambda: exit()
        )



        # Poscicionamiento de los botones
        atras.place(x = 20, y = 570 )
        cerrar.place(x = 900, y = 570 )

        
        centrar(top)
        top.protocol('WM_DELETE_WINDOW', lambda: back(top, root))
        top.mainloop()


# INTERFAZ GRÁFICA.
def main():

    global root, entry, Bases


    root = Tk()
    root.title('Comedor')

    #Icono
    icon = resource_path(r'src\assets\icon\icono.ico') 
    root.wm_iconbitmap(True, icon) # establece el icono de la ventana

    # Imagen de fondo.
    img = resource_path(r'src\assets\img\main.png') 
    imagen = PhotoImage(file = img) 
    Label(root, image= imagen, bd = 0).pack() # establece el fondo de la ventana



    centrar(root)

    # Botones.

    Bases = Button(root)
    Insertar = Button(root)



    # configuración de los botones.
    Bases.config(
        
            text= 'Revisar\narchivos', 
            font = Font_tuple, 
            width= 15, 
            background='#ffffff',
            activebackground='#ffffff', 
            foreground='black', 
            activeforeground='black', 
            borderwidth= 0, 
            relief='raised', 
            overrelief='sunken', 
            command=lambda: Second_win('AbrirBaseDeDatos')
        
    )


    Insertar.config(
        
            text= 'Ingresar\ncédulas', 
            font = Font_tuple, 
            width= 15, 
            background='#ffffff', 
            activebackground='#ffffff', 
            foreground='black', 
            activeforeground='white', 
            borderwidth= 0, 
            relief='raised',
            overrelief='sunken', 
            command=lambda: Second_win('InsertarCédulas'),
            
    )

    # posicionamiento de los botonoes.
    Bases.place(x = 200, y = 270)
    Insertar.place(x = 627, y = 270)

    # TODO: Añadir el manual para que sirva este botón.
    # Manual = resource_path('Manual/Manual.pdf')
    # man = Button(root)
    # man.config(text= 'Manual', font = 'Comic_Sans_Ms 9', width= 20, background='black', activebackground='black', foreground='white', activeforeground='white', borderwidth= 2, relief='raised', overrelief='sunken', command=lambda: os.startfiles(Manual))
    # man.place(x = 20, y = 570 )

    root.mainloop()

if __name__ == "__main__":
    main()