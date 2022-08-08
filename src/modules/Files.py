# - @author: Juan Daniel Luna Cienfuegos
# - @Github: MilfuegosxDD
# - @version: 3.1.4

from datetime import datetime
import os, pandas as pd, shutil, platform, json, time
from openpyxl import Workbook, load_workbook
from tkinter import messagebox, filedialog as fd

class xlFiles:

    """
    Verificación del archivo xlsx del cuál se alojan los datos del estudiante y generación
    del reporte mensual de los estudiantes que asistieron al comedor
    """

    cache = '' # Carpeta de los registros diarios.
    info = {}  
    filename = '' # Base de datos
    foldername = '' # Reportes

    def __init__(self, dir: str, Archivo: str) -> None:
        """
        Creación de la carpeta donde se alojarán los archivos de los estudiantes
        - dir: Carpeta con los archivos requeridos por el programa y proporcionados por este mismo.
        - cache: Carpeta de los registros diarios.
        AMBAS CARPETAS EN EL CASO DE EXISTIR NO SE MODIFICAN.
        """

        self.__dir = dir
        self.filename = self.__dir + f"\\{Archivo}"
        self.foldername = self.__dir +"\\Reports"
        if platform.system() == 'Windows':
            self.cache = self.foldername + '\\Cache'
            os.makedirs(self.cache, exist_ok= True)
            os.system(f'attrib +h {self.cache}')
        elif platform.system() == 'Linux':
            # No ha sido probado.
            self.__dir = '/home' + "/" + dir
            self.filename = self.__dir + f"/{Archivo}"
            self.foldername = self.__dir +"/Reports"
            self.cache = self.foldername + '/.Cache'
            os.makedirs(self.cache, exist_ok= True)

    def VerificacionDeDatos(self) -> bool:
        """
        Verifica los datos del archivo los cuales deben estan en el siguente formato:
        
            | Cédula | Nombre completo | Sección | Grupo |
        
        - info: diccionario con todos los datos de las personas que están en ese archivo.

        En el caso de que de que el archivo no este en la carpeta indicada este abrirá el administrador de archivos 
        para que podamos movamos el archivo a la carpeta solicitada.

        En el caso de que haya una fila con menos datos de los solicitados el programa o que en esta fila
        hayan datos que no esten en el formato correcto. El programa mostrará una ventana de dialogo donde se mostrará la fila
        en la cual se encuentra el error, de igual forma si el archivo esta vacio mostrara otra ventana de dialogo indicando el error.
        """
        try:
            df = pd.read_excel(self.filename)
            # Tomando los datos del archivo
            
            for row in df.itertuples(index = True):
                # si hay menos datos en la fila de los cuales son requeridos el programa indicará la fila en la cual hay un error.
                if 'nan' in str(row[0:5]) or str(row[1]).isalpha() == True or str(row[1]).isalnum() == False or str(row[2]).isnumeric() == True:
                    # Bug: Cuando hay celdas extras con datos extras en otras filas el programa las ignora.
                    self.__fila = row[0] + 2
                    messagebox.showerror('Error en fila', f'Revise la fila {self.__fila}\nEl formato del archivo debe ser\n | Cédula | Nombre completo | Sección | Grupo |')
                    os.startfile(self.filename)
                    return False
                else:
                    try:
                        self.info[str(row[1].upper())] = row[2:5]
                    except AttributeError:
                        self.info[str(row[1])] = row[2:5] 
            if df.empty == True:
                # En el caso de que el archivo este vacio
                messagebox.showerror('Archivo vacio', f'El archivo no puede estar vacio.\nEl formato del archivo debe ser\n\n| Cédula | Nombre completo | Sección | Grupo |')
                os.startfile(self.filename)
                return False
            # En el caso de que se realice todo con normalidad.
            return True

        except FileNotFoundError as e:
            messagebox.showerror('FileNotFoundError', f'{e}\nPor favor presione abrir para mover el archivo.')
            source = fd.askopenfilename(title = 'Mover',filetypes=(('Excel files', '.xlsx'), ('All', '.')))
            destination = self.__dir
            try:
                shutil.move(source, destination)
            except shutil.Error:
                pass
            return False

        except Exception as e:
            messagebox.showerror('Error Inesperado', f'{e}')
            return False




    def GuardarRegistro(self, data: dict):
        """
        Crea y guarda a las personas que han ingresado al comedor durante un mes.
        
        - data: Los datos de las personas que han usado el comedor durante el dia.

        En el caso de que no este el archivo del mes, este lo crea y finalmente ingresa los datos.
        """
        __hoy = pd.to_datetime(datetime.today().strftime('%d-%m-%y %H:%M:%S'), dayfirst=True)
        __actual = datetime.today().strftime('%m-%y')
        while True:
            try:
                archivo = load_workbook(self.foldername +f"\\{__actual}.xlsx")
                ws = archivo.active
                i = ws.max_row; i += 1; # encuentra la última linea del archivo
                for k, v in data.items():
                    """
                    Cédula         | Nombre completo              | Sección | Grupo                 | Fecha
                    1111111111       Roberto Robles Gomez           11-1    Estudiante Regular       1-7-2022    
                    """
                    try:
                        ws[f'A{i}'] = int(k) # Número de cédula
                    except ValueError:
                        ws[f'A{i}'] = k # Número de cédula
                    ws[f'B{i}'] = v[0] # Nombre completo 
                    ws[f'C{i}'] = v[1] # Sección
                    ws[f'D{i}'] = v[2] # Grupo
                    ws[f'E{i}'] = __hoy # Fecha con hora
                    i += 1 # avanza a la siguiente linea.
                archivo.save(self.foldername + f'\\{__actual}.xlsx')
                break
            except FileNotFoundError:
                wb = Workbook()
                ws = wb.active
                ws.title = 'Registro'
                ws.append({1:'Cédula',
                           2:'Nombre completo', 
                           3: 'Sección',
                           4: 'Grupo',
                           5: 'Fecha'})
                ws.column_dimensions['A'].width = 20
                ws.column_dimensions['B'].width = 50
                ws.column_dimensions['C'].width = 20
                ws.column_dimensions['D'].width = 20
                ws.column_dimensions['E'].width = 20
                wb.save(self.foldername +f"\\{__actual}.xlsx")
                continue
            except PermissionError as e:
                messagebox.askretrycancel(f'PermissionError', f'{e}\nPor favor cierre el archivo antes de continuar')
                continue
            except ValueError:
                messagebox.showwarning(f'Formato incorrecto', 'El archivo debe tener el siguiente formato\nCédula, Nombre completo, Sección, Grupo')
                os.startfile(self.filename)
                continue      





class Temp:
    """
    Registro de los números de cédulas que han usado el comedor durante el dia
    - tempinfo: una lista con los números de cédula de las personas que utilizaron el comedor
    durante el día.
    """
    tempinfo = [] # info dentro del archivo json.
    __hoy = time.strftime('%d-%m-%y')
    def Cargar_info(self, CacheFolder):
        """
        Extrae la información que hay en el archivo de tipo .json
        en y la guarda en una lista.
        """
        try:
            with open(f'{CacheFolder}\\{self.__hoy}.json', 'r') as File:
                self.tempinfo = json.load(File)
        except FileNotFoundError:
            self.Editar_info(CacheFolder, self.tempinfo)

    def Editar_info(self, CacheFolder: str, data: list):
        """
        Edita el archivo de tipo .json con los números de cédula recolectados.

        - data: lista de números de cedulas.
        """
        try:
            with open(f'{CacheFolder}\\{self.__hoy}.json', 'w') as File:
                json.dump(data, File, indent=4)
                File.close()
        except FileNotFoundError:
            ask = messagebox.askokcancel('FileNotFoundError', 'Se supone que esto no debia suceder. Reinicie el programa, pero la información que fue recolectada durante el día ha sido perdida.')
            if ask == True:
                exit()
            else:
                pass


if __name__ == "__main__": 
    # Test
    __xlF = xlFiles("SistemaComedor") # Se especifica la carpeta en la cual se quiere trabajar
    __xlF.VerificacionDeDatos('Comedor.xlsx') # se especifica el nombre del archivo con el cual se quiere trabajar
    __xlF.GuardarRegistro({11111111: ('Roberto Robles Gomez', '11-1', 'Regular')}) # Prueba de guardado de registro.
    print(__xlF.info) # datos recolectados
