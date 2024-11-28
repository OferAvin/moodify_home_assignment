from abc import ABC, abstractmethod
import pandas as pd

class MissingValueCleaner(ABC):
    '''This is an abstract class for handling missing values
        the only method gets a DF clean the missing values and
        return a DF without NAs
    '''
    @abstractmethod
    def clean_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def change_dtypes(self, df: pd.DataFrame, col_dtype_dict: dict) -> pd.DataFrame:
        '''change df cols types according to col_dtype_dict '''
        cols_names = list(col_dtype_dict.keys())
        dtypes = list(col_dtype_dict.values())
        for col_name, dtype in zip(cols_names, dtypes):
            try:
                if col_name not in df.columns:
                    raise KeyError(f"Column '{col_name}' doesnt exist")
                df[col_name] = df[col_name].astype(dtype)
            except KeyError as ke:
                print(ke)
            except ValueError as ve:
                print(ve)
        return df
    
class DropMissingValuesCleaner(MissingValueCleaner):
    def clean_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna()
    
# Another example for implementation
class FillMeanCleaner(MissingValueCleaner):
    def clean_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.fillna(df.mean())