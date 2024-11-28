from abc import ABC, abstractmethod
import pandas as pd

class DataProcessor(ABC):
    def __init__(self, df:pd.DataFrame):
        super().__init__()

        self.df = df

    @abstractmethod
    def process_data(self) -> pd.DataFrame:
        pass

class ProcessTotalSumPerGroup(DataProcessor):
    '''This class process the data by summing col_to_sum by the groupby'''
    def __init__(self, df:pd.DataFrame, col_to_sum:str, groupby:str):
        super().__init__(df)

        self.col_to_sum = col_to_sum
        self.groupby = groupby

    def process_data(self) -> pd.DataFrame:
        processed_df = self.df.groupby(self.groupby)[self.col_to_sum].sum().reset_index()
        return processed_df
    
class ProcessTopNByGroup(DataProcessor):
    '''This class returns the top n from the groupby coll by the total sum of col_to_sum
    it uses ProcessTotalSumPerGroup for preprocessing the total sum by group'''
    def __init__(self, df:pd.DataFrame, col_to_sum:str, groupby:str, n:int):
        super().__init__(df)

        self.col_to_sum = col_to_sum
        self.groupby = groupby
        self.n = n
        self.sum_by_group_processor = ProcessTotalSumPerGroup(self.df, self.col_to_sum, self.groupby)

    def process_data(self) -> pd.DataFrame:
        total_by_group_df = self.sum_by_group_processor.process_data()
        sorted_df = total_by_group_df.sort_values(self.col_to_sum, ascending=False)
        return sorted_df.head(self.n)