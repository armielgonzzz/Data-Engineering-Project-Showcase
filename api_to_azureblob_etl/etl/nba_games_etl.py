'''
Request for data from Public API, transform the data and load it to and S3 Bucket
'''
import sys, os

# This line will enable us to import python scripts from other folders
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import requests, pandas as pd
from datetime import date, timedelta


def extract_data(key: str, url: str) -> dict:
    '''
    Extract data that we need from the Public API.

    :param `key`: Unique API Key per user.
    :param `url`: URL of Public API.
    :return: A dictionary representing the extracted data in JSON Format.
    '''

    # subtract 1 day from today to account for the timezone difference
    yesterday = date.today() - timedelta(days=1)
    
    header = {"Authorization": key}
    params = {"dates": [date.today(), yesterday]}

    # GET Request to the API
    response = requests.get(url=url, headers=header, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def transform_data(data: list) -> pd.DataFrame:
    '''
    Modify the JSON Data and covert it to CSV Format data

    :param `data`: List of Dictionary that we will convert into CSV Format
    :return: Pandas Dataframe of modifed JSON Data
    '''

    # List comprehension of needed columns from the JSON data
    csv_data = [(game['home_team']['full_name'],
                 game['home_team_score'],
                 game['visitor_team']['full_name'],
                 game['visitor_team_score'],
                 game['period']) for game in data['data']]

    # Declare the columns to be used in Pandas Dataframe
    columns = ['home_team', 'home_team_score', 'visitor_team', 'visitor_team_score', 'period']

    # Creating a Pandas Dataframe
    df = pd.DataFrame(csv_data, columns=columns)

    return df    


def load_data(data: pd.DataFrame, path: str) -> None:
    '''
    Saves the Pandas Dataframe to specifed filepath
    '''

    data.to_csv(path, index=False)