import pandas as pd

from tkinter import messagebox, filedialog as fd
import os,shutil
from openpyxl import load_workbook, Workbook
from datetime import datetime
class ExcelFiles:
    """import ExcelFiles as xlF"""
    fecha = str(datetime.today().strftime('%m-%y')) # mes-año
    file_tuples = ('Excel files', '.xlsx'), ('All files', '.')
    PersonasDelComedor = {}
    foldername = ''
    def __init__(self, dir: str) -> None:
        """directorio donde se guardarán todos los datos de las personas del comedor."""
        if dir.endswith('\\') or dir.endswith('/'):
            dir = dir[::-2]
        self.dir = dir
        os.makedirs(self.dir, exist_ok=True)

    def reportsdir(self, foldername: str):
        if foldername.endswith('\\') or foldername.endswith('/'):
            foldername = foldername[::-2]
        self.foldername = self.dir+ "\\" +foldername
        os.makedirs(self.foldername, exist_ok=True)

    def VerificacióndeArchivos(self, Archivo):
        datos = [] 
        info = [] 
        self.filename = self.dir+'\\'+Archivo
        try:
            self.df = pd.read_excel(self.filename)
            for values in self.df.itertuples(index= False, name= None):
                datos.append(values) # Toma todos los datos que están en el archivo.
        
            for cedula, nombre, seccion, grupo in datos: 
                if str(cedula).isalnum() == True:
                    info.append(nombre); info.append(seccion); info.append(grupo)
                    self.PersonasDelComedor[str(cedula).upper()] = tuple(info)
                    info.clear()
                elif str(cedula).isnumeric():
                    info.append(nombre); info.append(seccion); info.append(grupo)
                    self.PersonasDelComedor[str(cedula)] = tuple(info)
                    info.clear()
            datos.clear()

            for clave, valor0 in self.PersonasDelComedor.items():
                if str(clave).isalpha() == True or str(valor0[0]).isalpha() == False:
                    self.PersonasDelComedor.clear()
                    break
            if self.isnotEmpty(self.PersonasDelComedor) == True:
                return True

        except FileNotFoundError:
            self.Archivo_no_encontrado(Archivo)
        except ValueError:
            messagebox.showwarning('FORMATO INCORRECTO', 'EL ARCHIVO DEBE IR EN EL SIGUIENTE FORMATO\nCedula, Nombre, Sección, Grupo')
            os.startfiles(self.filename)
            return False

    def isnotEmpty(self, data_structure): 
        if (len(data_structure) > 0):
            return True
        else:
            messagebox.showwarning('FORMATO INCORRECTO', 'EL ARCHIVO DEBE IR EN EL SIGUIENTE FORMATO\nCedula, Nombre, Sección, Grupo')
            os.startfile(self.filename)
            return False

    def Archivo_no_encontrado(self,Archivo): 
        messagebox.showerror('ERROR ARCHIVO NO ENCONTRADO', f'PRESIONE ABRIR PARA MOVER EL ARCHIVO {Archivo} al diretorio {self.dir}')
        source = fd.askopenfilenames(title = 'Mover',filetypes=(self.file_tuples))
        destination = self.dir
        for files in source:
            try:
                shutil.move(files, destination)
            except shutil.Error:
                pass
        return False


    def openfiles(self, pressed):
        if pressed == 'abrirbase':
            os.startfile(self.filename)
        else:
            self.open_reports()

    def open_reports(self):
        source = fd.askopenfilenames(initialdir= self.foldername, filetypes=(self.file_tuples)) # se toma el directorio donde se 
        for files in source:
            os.startfile(files)
    
    def GuardarRegistro(self, UsaronElComedor:dict):
        """Guarda el registro de las personas que utilizaron el comedor."""
        
        hoy = pd.to_datetime(datetime.today().strftime('%d/%m/%y %H:%M:%S'), dayfirst= True) # dia-mes-año hora-minutos-segundos 
        while True:
            try:
                archivo = load_workbook(self.foldername+"\\"+'Reporte '+ self.fecha+'.xlsx')
                ws = archivo.active # worksheet 
                i = ws.max_row; i += 1 # busca la ultima celda sin datos.

                for cedula, datos in UsaronElComedor.items():
                    # si la persona esta en la base de datos la guarda con sus datos los cuales son 
                    #| Numero de cédula | Nombre | Sección |  Grupo | Fecha
                    ws[f'A{i}'] = cedula # cedula 
                    ws[f'B{i}'] = datos[0] # Nombre
                    ws[f'C{i}'] = datos[1] # Seccion
                    ws[f'D{i}'] = datos[2] # Grupo
                    ws[f'E{i}'] = hoy # fecha
                    i += 1 # avanza una linea.

                archivo.save(self.foldername+'\\'+'Reporte '+ self.fecha +'.xlsx')
                break

            except FileNotFoundError:
                # si no esta el archivo lo genera y le introduce los encabezados
                wb = Workbook()
                ws = wb.active
                ws.title = 'Registro'
                ws.append({1:'\tCEDULA', 2:'\tNOMBRE', 3: "\tSECCIÓN", 4:'\tGRUPO', 5:'\tFECHA'})
                ws.column_dimensions['A'].width = 15
                ws.column_dimensions['B'].width = 50
                ws.column_dimensions['C'].width = 20
                ws.column_dimensions['D'].width = 20
                ws.column_dimensions['E'].width = 20
                wb.save(self.foldername+"\\"+'Reporte '+self.fecha +'.xlsx')
                continue

            except PermissionError:
                # Solo si el archivo de reportes esta abierto.
                messagebox.showwarning('Reporte abierto',f"Por Favor cierre el archivo antes de continuar 'Reporte {self.fecha}.xlsx'")
                continue

            except ValueError:
                # en
                messagebox.showwarning('FORMATO INCORRECTO', 'EL ARCHIVO DEBE IR EN EL SIGUIENTE FORMATO\nCedula, Nombre, Sección, Grupo')
                os.startfiles(self.filename)
                return False


#test

# ef = ExcelFiles('Test')
# ef.reportsdir('reports')
# ef.GuardarRegistro({1:['asdf','asdf','dsaf']})