from tkinter import Button, Misc, Tk

class Botones:
    def __init__(self, master: Misc | None, text: str, width: int , 
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
        
if __name__ == "__main__":
    App = Tk()
    boton1 = Botones(App, 'HOla', 15, 1, 23)
    boton1.Boton.config(command=lambda: print('Hola'))
    App.mainloop()