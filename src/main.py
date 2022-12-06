from tkinter \
    import END, Label, Tk, Canvas, Entry, Button, PhotoImage, Label, filedialog, messagebox

from ManejoDeArchivos \
    import xlFiles, Temp

from datetime \
    import datetime

import os, sys

xLF = xlFiles('C:\\SistemaComedor', 'Comedor.xlsx')
temp = Temp()


def resource_path(relative_path) -> str:
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# def FreeTrial() -> None:
#    """Indica la duración del periodo de prueba del programa."""
#     if datetime.today().strftime("%d-%m-%Y") < "30-10-2022":
#         messagebox.showinfo("","Tu prueba gratuita del programa terminará pronto...\n¡Por favor comuniquese con el desarrollador!\nCorreo: milfuegosdev@gmail.com\nGitHub: MilfuegosxD")
    
#     else:
#         messagebox.showinfo("","Tu prueba gratuita del programa terminó...\n¡Por favor comuniquese con el desarrollador!\nCorreo: milfuegosdev@gmail.com\nGitHub: MilfuegosxD")
#         window.destroy()

def enter (event):
    """Registra a los estudiantes"""
    def __wait():
        STATUS.config(image=BLANK)
        ENTRY.delete(0, END)
    """
    Cuando alguien presiona enter se verifica que una personas este dentro del archivo
    excel que fue proporcionado anteriormente."""
    __ingresos = {}
    __hoy = []
    if  info == False:
        if type(refresarInformacion()) == bool:
            ENTRY.delete(0, END)

    else:
        try:
            DNI = ((ENTRY.get()).upper()).strip()
        except:
            DNI = (ENTRY.get()).strip()
        
        finally:
            temp.Cargar_info(xLF.cache) # Carga la información que esta dentro del archivo json
            __hoy.clear() # se edita la lista para que no se duplique la información
            __hoy.extend(temp.tempinfo) # se vuelven a cargar los datos de la lista.
            
            if DNI.isalpha() == True or DNI.isalnum() == False:
                messagebox.showerror('Error', 'Cédula con caracteres no admitidos.')
                ENTRY.delete(0, END)
            else:
                if DNI not in __hoy:
                    __hoy.append(DNI) # Si la cédula no estaba registrada, se registra.
                    if DNI in info:
                        __ingresos[DNI] = info[DNI] # Si la cédula estaba en el archivo excel 
                        temp.Editar_info(xLF.cache, __hoy) # modifica el archivo json con la cédula que recién fue insertada.
                        xLF.actual = "ReporteDelMes"
                        xLF.GuardarRegistro(__ingresos)
                        xLF.actual = f"ReporteNúmero{datetime.today().strftime('%d')}"
                        xLF.GuardarRegistro(__ingresos); __ingresos.clear() # Guarda el registro y se borra la información para que no se dupliquen
                        STATUS.config(image= BECADO)
                        STATUS.after(1000, __wait)
                    else:
                        STATUS.config(image=NOBECADO)
                        STATUS.after(1000, __wait)
                else:
                    STATUS.config(image=REGISTRADOS)
                    STATUS.after(1000, __wait)

def refresarInformacion() -> bool | dict:
    """actualiza los datos de la base de datos."""
    global info
    info = xLF.VerificacionDeDatos
    if info == False:
        AbrirBaseDeDatos()
        return info
    else:
        return info

def AbrirBaseDeDatos():
    try:
        while True:
            os.startfile(xLF.filename)
            messagebox.showinfo("","Por favor guarda los cambios y presiona recargar.")
            break
    except FileNotFoundError:
        refresarInformacion()

def AbrirReportes():
    try:
        os.stat(xLF.Reports)
        Directories = filedialog.askopenfilenames(initialdir=xLF.Reports, filetypes=(('Excel files', '.xlsx'), ('All', '.')))
        for files in Directories:
            os.startfile(files)
        del Directories
    except FileNotFoundError:
        messagebox.showerror("", "No se ha generado ni un solo reporte. :(")

def cerrar():
    question = messagebox.askyesno('¿Salir?', '¿Esta seguro/a que desea salir del programa?')
    if question == True:
        window.destroy()
    else:
        pass
def centrar_fun():
    wtotal = window.winfo_screenwidth()
    htotal = window.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 1280
    hventana = 720

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    window.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

window = Tk()
centrar_fun()
window.title("Comedor")
window.configure(bg = "#FFFFFF")


# --- ICONO --- #
ICON = PhotoImage(
    file = resource_path("src/assets/ICON.png"))
# --- BACKGROUND --- #
BACKGROUND_IMG = PhotoImage(
    file=resource_path("src/assets/Background.png"))
# --- STATUS --- #
BLANK = PhotoImage(
    file=resource_path("src/assets/Blank.png"))
BECADO = PhotoImage(
    file=resource_path('src/assets/Becados.png'))
NOBECADO = PhotoImage(
    file=resource_path("src/assets/NoBecado.png"))
REGISTRADOS = PhotoImage(
    file= resource_path("src/assets/Registered.png"))

# --- BUTTONS --- #
INGRESAR_BT_IMG = PhotoImage(
    file=resource_path("src/assets/Ingresar_BT.png"))
DATOS_BT_IMG = PhotoImage(
    file=resource_path("src/assets/Datos_BT.png"))
REPORTES_BT_IMG = PhotoImage(
    file=resource_path("src/assets/Reportes_BT.png"))
REFRESCAR_IMG = PhotoImage(
    file=resource_path("src/assets/REFRESCAR_BT.png"))

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# --- ICONO --- #
window.iconphoto(False, ICON)
# --- BACKGROUND --- #
BACKGROUND = canvas.create_image(
    640.0,
    360.0,
    image=BACKGROUND_IMG
)

# --- BUTTONS --- #
INGRESO_BT = Button(
    image=INGRESAR_BT_IMG,
    borderwidth=0,
    activebackground="#FFFFFF", background="#FFFFFF",
    cursor="hand2",
    highlightthickness=0,
    command=lambda: enter(""),
    relief="flat"
)
INGRESO_BT.place(
    x=719.0,
    y=308.0,
    width=297.0,
    height=104.0
)

DATOS_BT = Button(
    image=DATOS_BT_IMG,
    borderwidth=0,
    activebackground="#DCA1B1", background="#DCA1B1",
    cursor="hand2",
    highlightthickness=0,
    command= AbrirBaseDeDatos,
    relief="flat"
)
DATOS_BT.place(
    x=246.0,
    y=494.0,
    width=194.0,
    height=68.0
)

REPORTES_BT = Button(
    image=REPORTES_BT_IMG,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#C8ABC6", background="#C8ABC6",
    cursor="hand2",
    command=AbrirReportes,
    relief="flat"
)
REPORTES_BT.place(
    x=14.0,
    y=494.0,
    width=194.0,
    height=68.0
)

REFRESCAR_BT= Button(
    image=REFRESCAR_IMG,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#C8ABC6", background="#C8ABC6",
    cursor="hand2",
    command=refresarInformacion,
    relief="flat"
)
REFRESCAR_BT.place(
    x=131.0,
    y=578.0,
    width=194.0,
    height=68.0
)

# --- STATUS --- #
STATUS = Label(
    image=BLANK,
    background="#FFFFFF"
)
STATUS.place(
    x = 678.0,
    y = 412.0,
    width= 380,
    height=217)

# --- ENTRY --- #
ENTRY = Entry(
    bd=0,
    bg="#D9D9D9", font="curier 40",
    justify="center",
    highlightthickness=0
)
ENTRY.place(
    x=531.0,
    y=158.0,
    width=675.0,
    height=89.0
)
ENTRY.bind("<Return>", enter)

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", cerrar)
# FreeTrial()
if type(refresarInformacion()) == bool:
    AbrirBaseDeDatos()
window.mainloop()
