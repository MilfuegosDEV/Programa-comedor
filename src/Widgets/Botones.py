from tkinter import Button, Tk

class Boton:
    """
    Configuración y posicionamiento de los botones en la ventana.""" 
    def __init__(self, master, text: str, width: int , 
                 x: int, y: int, command: '()', fontTuple = ("Comic Sans MS", 20)) -> None:
        self.Boton = Button(master)
        self.Boton.config(
            text= text,
            font= fontTuple,  
            width= width, 
            background='#ffffff',
            activebackground='#ffffff', 
            foreground='black', 
            activeforeground='black', 
            borderwidth= 0, 
            relief='raised', 
            overrelief='sunken',
            command = command
        )
        
        self.Boton.place(x= x, y = y)
if __name__ == '__main__':
    __app = Tk()
    Boton(__app, 'Hola', 7, 5, 4, lambda: print('Hola'), ('ARIAL', 8))
    __app.mainloop()