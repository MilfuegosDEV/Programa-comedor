# Interfaz del programa
from os import startfile
from ProgramaComedor import *
from tkinter import END, Tk, Entry,Label,Button, Toplevel
from shutil import move
from tkinter.filedialog import askopenfilename


















# interfaz
"""Menú principal"""
mkdir()
root = Tk() 
root.geometry('1278x700')# a la ventana no se le podrá cambiar el tamaño
root.config(background='#380106')

msg = Label(root)
msg.config(text='Sistema Comedor', font = "FiraCode 60 underline",background='black',foreground='white', width= 60)
msg.pack(side= 'top', fill='x', pady= 30)

Bases = Button(root)
Bases.config(text= 'Revisar\narchivos', font = 'FiraCode 40 italic overstrike', width= 15, background='black', activebackground='black', foreground='white', activeforeground='white', borderwidth= 6)
Bases.pack(side='left', padx = 90)

BCedulas = Button(root)
BCedulas.config(text= 'Ingresar\ncédulas', 
                font = 'FiraCode 40 italic overstrike', 
                width= 15, background='black', 
                activebackground='black', 
                foreground='white', 
                activeforeground='white', 
                borderwidth= 6, 
                command=lambda: Mcedulas()
                )
BCedulas.pack(side='right', padx = 90)

# ventanas hijas

"""Cuando presionamos el botón de insertar cédula el programa ejecutará las siguientes indicaciones"""


def Mcedulas():
    global VAPN, VAB
    
    
    
    
    
    '''La siguiente función cambia de color dependiendo el grupo en el cual este la persona
    toma como parametros:
    1. color que pueden ser ["light green", "brown2", "gold"]
    2. texto que puede ser ["Es de plan nacional", "Es becado", "Tiene que comprar almuerzo", "Ya comió"]'''
    
    
    def colores (color, text): 
        colores = Toplevel(child)
        colores.geometry('700x400')
        colores.config(bg = color)
        colores.resizable(0,0)

        label = Label(colores)
        label.config(bg = 'black',
                fg = 'white',
                font = 'FiraCode 40',
                text = text,
                width  = 22,
                height= 1
                )
        label.pack(pady = 130)

        def ocultar():
            colores.destroy()
        colores.after(1000,ocultar)






    # Sirve para que cuando presione enter emule el funcionamiento de presionar un botón 
    def enter (event):
        insertar_cedulas()


    # cuando cerremos la ventana se guardarán los datos.
    def on_closing():
        GuardarRegistro()
        ventas.clear()
        PlanUsado.clear()
        BecasUsadas.clear()
        child.destroy()
        root.deiconify()



    '''Cuando las personas inserten el numero de cedula presionando el botón o cuando usen el enter.'''
    def insertar_cedulas():

        '''En esta parte del programa se le pide a las personas que inserten su número de cédulas
        Luego lo que hace es validar si el número de cédulas están en:
        1. Plan Nacional.
        2. Personas becadas.
        3. Personas las cuales deben comprar el almuerzo.'''

        try:
            NumeroDeCedula = int(entry.get())
            

            """En esta parte se verificará si la persona ya a usado el comedor."""

            if NumeroDeCedula in cedulas:
                # se aparecerá una ventana emergente diciendo el que la persona ya usado el comedor
                colores('brown2', 'Ya comió')
                entry.delete(0,END)

            
            else:
                '''En el caso de que la persona no haya comido'''
                if (int(NumeroDeCedula) in PlanNacional.keys()):
                    # se aparecerá una ventana emergente del color verde diciendo que esta persona es de plan nacional
                    PlanUsado[NumeroDeCedula] = PlanNacional[NumeroDeCedula]
                    colores('light green', "Es de plan nacional")
                    cedulas.append(NumeroDeCedula)
                elif (int(NumeroDeCedula) in Becas.keys()):
                    # se aparecera una ventana emergente del color verde diciendo que esta persona es becada.
                    BecasUsadas[NumeroDeCedula] = Becas[NumeroDeCedula]
                    colores('light green', 'Es becado')
                    cedulas.append(NumeroDeCedula)
                else:
                    # Aparecerá una ventana del color dorado diciendo que esta persona debe comprar el almuerzo.
                    ventas.append(NumeroDeCedula)
                    colores('gold', 'Tiene que comprar almuerzo')
                    cedulas.append(NumeroDeCedula)                
                entry.delete(0,END) # se borrará todo lo que este en la zona para ingresar datos.
                GuardarRegistro()
                ventas.clear()
                PlanUsado.clear()
                BecasUsadas.clear()

        # cuando existe un caracter incorrecto aparecerá un mensaje de que hay letras, y el programa solo admite numeros.
        except ValueError:
            messagebox.showinfo('Valores no admitidos', 'Las cédulas no llevan letras.')
            entry.delete(0, END)





    """Interfaz del la ventana del botón insertar cédulas."""

    if VAPN() is False or VAB() is False:
        if VAB() is True and VAPN() is False:
            Archivo = 'PlanNacional.xlsx'
        else:
            Archivo = "Becados.xlsx"

        messagebox.showerror('FileNotFoundError',f'Agregue el archivo {Archivo} al directorio C:\SistemaComedor')
        source = askopenfilename(title = 'Mover',filetypes=(('Excel files', '.xlsx'), ('Excel files', '.xlsx')))
        destination = 'C:\SistemaComedor'
        move(source, destination)

    elif VAPN() is True and VAB() is True:
        root.withdraw()
        child = Toplevel(root) 
        child.geometry('1278x700')# a la ventana no se le podrá cambiar el tamaño
        child.config(background='#380106')

        entry = Entry(child)
        entry.config(justify='center', font = "FiraCode 80 underline",width= 60)
        entry.pack(side= 'top', fill='x', pady= 70)
        entry.bind('<Return>', enter)

        Insertar_Cedulas = Button(child)
        Insertar_Cedulas.config(text= 'Insertar\ncédula', 
                                font = 'FiraCode 40 italic overstrike', 
                                width= 15, background='black', 
                                activebackground='black', 
                                foreground='white', 
                                activeforeground='white', 
                                borderwidth= 6,
                                command = lambda: insertar_cedulas()
                                )
        Insertar_Cedulas.pack()

        child.wm_protocol("WM_DELETE_WINDOW", on_closing)
        









root.mainloop()