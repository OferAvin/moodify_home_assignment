from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    '''This is an abstract class for loading data files
        This class gets the data file_path and
        have 1 method load() which loads the data from the  
        file_path and returns a pd.DataFrame 
    '''
    def __init__(self, file_path:str, logger = None):
        super().__init__()
        
        self.file_path = file_path
        self.logger = logger
        self.df = None

    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass
    
    def dataset_summary(self) -> str:
        '''This functios summarizes the df (this function is a function I use in every work I do with tabolar data)'''
        summary = (
            f"Dataset Summary:\n"
            f"{'-' * 80}\n"
            f"Number of Rows: {self.df.shape[0]}\n"
            f"Number of Columns: {self.df.shape[1]}\n\n"
            f"Column Names:\n" +
            "\n".join([f"  - {col}" for col in self.df.columns]) +
            "\nMissing Values per Column:\n" +
            "\n".join([f"  - {col}: {missing} missing" for col, missing in self.df.isna().sum().items()]) +
            f"\nAre there duplicate rows? {'Yes' if self.df.duplicated().sum() > 0 else 'No'}\n\n"
            f"Data Types:\n" +
            "\n".join([f"  - {col}: {self.df[col].dtype}" for col in self.df.columns]) +
            f"\n{'-' * 80}"
        )
        return summary


class CSVDataLoader(DataLoader):
    '''this class implements DataLoader for loading CSV files'''
    def __init__(self, file_path:str, logger=None):
        super().__init__(file_path, logger)
        
    def load(self) -> pd.DataFrame:
        try:
            self.df = df = pd.read_csv(self.file_path)
            self.logger.info(f"CSV was read successfully")
            self.logger.info(self.dataset_summary())
            return self.df
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.file_path}")
        except Exception as e:
            self.logger.error(f"An error occurred while reading {self.file_path}: {e}")
        