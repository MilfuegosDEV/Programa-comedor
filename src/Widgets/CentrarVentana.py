
class CentrarVentana:
    """
    Establece el tamaño de la ventana en la cual se esta trabajando y la posiciona en el centro
    de la pantalla.
    """
    __size = ('1066x600') # Tamaño de la ventana.
    def __init__(self, window):
        window.geometry(self.__size) # Fija el tamaño de la ventana
        window.resizable(False, False) # indica que la ventana no se puede redimensionar
        window.update_idletasks() 

        w = window.winfo_width() # obtiene el ancho de la pantalla
        h = window.winfo_height() # obtiene el alto de la pantalla

        extraW = window.winfo_screenwidth() - w
        extraH = window.winfo_screenheight() - h

        window.geometry("%dx%d%+d+%d" % (w, h, extraW/2, extraH/2)) # Posiciona la ventana.


        