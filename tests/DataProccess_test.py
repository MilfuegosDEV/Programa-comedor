import pandas as pd
import unittest
from src.DataProccess import ReadData


class ReadData_test(unittest.TestCase):
    def setUp(self):
        self.obj = ReadData('tests/sample.csv')

    def test_df(self):
        esperado = type(pd.DataFrame([])) # -> DataFrame
        actual = type(self.obj.df) # -> DataFrame | None
        self.assertEqual(actual, esperado)
    

