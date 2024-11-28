from abc import ABC, abstractmethod
import pandas as pd

class DataExporter(ABC):
    '''This is an abstract class for export Data from a pd.DataFrame'''
    def __init__(self, path:str):
        super().__init__()

        self.path = path

    @abstractmethod
    def export_data(self, df:pd.DataFrame):
        pass

class CSVDataExporter(DataExporter):
    '''This class inherit from DataExporter and implements export_data to a csv file'''
    def __init__(self, path:str):
        super().__init__(path)

    def export_data(self, df:pd.DataFrame):
        df.to_csv(path_or_buf=self.path, index=False)
