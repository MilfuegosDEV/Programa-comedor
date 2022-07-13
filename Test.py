from tkinter import messagebox
from src.modules import xlFiles, Temp, resource_path


class App:
    Registradas = []
    def __init__(self) -> None:
        self.xlF = xlFiles('Test') # Dirección del directorio donde van a parar tdoos los datos
        self.Temp = Temp() 
    
    def sacando_informacion(self):
        while True:
            if self.xlF.VerificacionDeDatos('Comedor.xlsx') == True: # Nombre del archivo, puede ser modificado
                self.info = self.xlF.info
                break
            else:
                continue

    def registrandoInformación(self, DNI: str):
        try:
            DNI = DNI.upper()
        except:
            pass
        Ingresos = {}
        self.Temp.Cargar_info(self.xlF.cache)
        self.Registradas.clear();self.Registradas.extend(self.Temp.tempfiles)
        if type(DNI) != str:
            DNI = str(DNI)
        if DNI.isalpha() == True or DNI.isalnum() == False:
            print("Error")
        else:
            if DNI not in self.Registradas:
                self.Registradas.append(DNI)
                if DNI in self.info:
                    Datos = self.info[DNI]
                    Ingresos[DNI] = Datos
                else:
                    Ingresos[DNI] = ('NA', 'NA', 'Estudiante Regular')
                self.Temp.Editar_info(self.xlF.cache, self.Registradas)
                self.xlF.GuardarRegistro(Ingresos); Ingresos.clear()
            else:
                print('La cédula ya fue registrada.')

if __name__ == '__main__':
    Application = App()
    Application.sacando_informacion()
    contador = 0
    while True: 
        contador += 1
        Cedula = input('Inserte un número de cédula: ')
        Application.registrandoInformación(Cedula)
        if contador % 5 == 0:
            ask = messagebox.askyesno('Salir', '¿Desea salir?')
            if ask == True:
                break
            else:
                continue