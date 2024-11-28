import logging
import yaml
from src.loaders import CSVDataLoader
from src.data_cleaners import DropMissingValuesCleaner
from src.data_processor import ProcessTopNByGroup
from src.exporters import CSVDataExporter

def main():

    # Get all pathes from yaml
    with open('params.yml', 'r') as f:
        params = yaml.safe_load(f)

    # Set logger
    log_file = params["pathes"]["log_file"]
    data_file = params["pathes"]["data_path"]
    save_path = params["pathes"]["save_path"]

    logger = logging.getLogger("transaction_logger")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)

    log_file_handler = logging.FileHandler(log_file)
    log_file_handler.setFormatter(formatter)

    logger.addHandler(log_file_handler)

    # Read data
    data_loader = CSVDataLoader(file_path=data_file, logger=logger)
    df= data_loader.load()
    print(df['customer_id'].nunique())

    # Clean data
    dtype_dict = {
        "transaction_id":str,
        "customer_id": str,
        "transaction_date": 'datetime64[ns]',
        "amount": 'float64',
        "payment_method": str
    }

    data_cleaner = DropMissingValuesCleaner()
    corrected_types_df = data_cleaner.change_dtypes(df=df, col_dtype_dict=dtype_dict)
    cleaned_df = data_cleaner.clean_missing_values(df=corrected_types_df)

    # Process data
    n = params["n"]
    print(f'$$$$$$$$$$$$$$$$$$$${n}$$$$$$$$$$$$$$$$$$')
    data_processor = ProcessTopNByGroup(cleaned_df, groupby="customer_id", col_to_sum="amount", n = params["n"])
    precessed_df = data_processor.process_data()

    # Export data
    data_exporter = CSVDataExporter(save_path)
    data_exporter.export_data(precessed_df)

main()