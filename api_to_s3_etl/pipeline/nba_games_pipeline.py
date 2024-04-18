'''
ETL Pipeline for extracting data from API, converting it to Pandas.DataFrame and loading it to CSV Format
'''
import sys, os

# This line will enable us to import python scripts from other folders
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


# import ETL Functions and config info
from etl.nba_games_etl import extract_data, transform_data, load_data
from configs.info_config import API_KEY, URL, OUTPUT_PATH


def nba_games_pipeline(file_name: str):
    '''
    Main driver function for ETL Pipeline
    
    :param `file_name`: file name should be the date of the execution of the pipeline
    '''

    # extract data
    games = extract_data(API_KEY, URL)

    # if there are games today, perform the rest of the ETL
    if len(games['data']) > 0:
        # transform
        games_data = transform_data(games)

        # load data to CSV
        csv_path = f'{OUTPUT_PATH}/{file_name}_games.csv'
        load_data(games_data, csv_path)

        return csv_path

    # if there are no games for today, return None
    return None