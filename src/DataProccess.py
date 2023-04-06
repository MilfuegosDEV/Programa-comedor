import pandas as pd
import os.path

class ReadData:

    def __init__(self, Archivo: str) -> None:
        self.filename = Archivo
    

    @property
    def df(self) -> None | pd.DataFrame:
        """
        Returns a pandas DataFrame

        Returns:
        -------
        None or pd.DataFrame
            If the DataFrame is not empty and the `ID` and `FULLNAME` columns are not empty, the function
            checks that the `ID` column contains only alphanumeric characters and that the `FULLNAME` column
            only contains letters and spaces. If these conditions are met, the function returns a DataFrame. If not, the function returns None.
        """

        if not self.__df.empty and not self.__df[['ID', 'FULLNAME']].isnull().values.any():
            if self.__df['ID'].str.match(r'^(?=.*[0-9])[a-zA-Z0-9]+$').all():
                if self.__df['FULLNAME'].str.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$').all():
                    return self.__df
                else:
                    return None
            else:
                return None
        else:
            return None

    @property
    def __df(self) -> pd.DataFrame:
        path, ext = os.path.splitext(self.filename) 
        match (ext):
            case '.csv':
                return pd.read_csv(self.filename)
            case '.xlsx':
                return pd.read_excel(self.filename)
            case '.json':
                return pd.read_json(self.filename)
            case _:
                return pd.DataFrame([])


