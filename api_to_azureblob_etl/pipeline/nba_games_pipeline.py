'''
ETL Pipeline for extracting data from API, converting it to Pandas.DataFrame and loading it to CSV Format
'''
import sys, os

# This line will enable us to import python scripts from other folders
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


# import ETL Functions and config info
from etl.nba_games_etl import extract_data, transform_data, load_data
from configs.info_config import API_KEY, URL, OUTPUT_PATH


def nba_games_pipeline(file_name: str) -> str:
    '''
    Extracts data from public API, transform the data and then save it to local directory
    
    :file_name: File name should be the date of the execution of the pipeline
    :return: Directory of the saved .csv file
    '''

    # extract data
    games = extract_data(API_KEY, URL)
   
    # if there are games today, perform the rest of the ETL
    if games['data']:
        try:
            # transform
            games_data = transform_data(games)

            # load data to CSV
            csv_path = f'{OUTPUT_PATH}/{file_name}_games.csv'
            load_data(games_data, csv_path)
            print("Succesfully extracted and transformed the data")

            return csv_path

        except Exception as e:
            print(f'Error occured during extraction of data from API: {e}')
            return None
    
    else:
        print('There are no games today')
        return None