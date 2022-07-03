import json,time

class Temp:
    tempfiles = []
    __hoy = time.strftime('%d-%m-%y')
    def Cargar_info(self, CacheFolder):
        try:
            with open(f'{CacheFolder}\\{self.__hoy}.json', 'r') as File:
                self.tempfiles = json.load(File)
        except FileNotFoundError:
            self.Editar_info(CacheFolder, self.tempfiles)

    def Editar_info(self, CacheFolder: str ,data: list):
        with open(f'{CacheFolder}\\{self.__hoy}.json', 'w') as File:
            json.dump(data, File, indent=4)
            File.close()