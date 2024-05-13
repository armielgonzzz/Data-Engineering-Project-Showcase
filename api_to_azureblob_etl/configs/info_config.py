'''
This module will extract all the sensitive information inside the `config.cfg` file.
'''

import configparser, os

def extract_config_info():

    # Define path to config.cfg
    file_path = os.path.join('configs', 'config.cfg')

    # Parse the config file to extract sensitive information
    reader = configparser.ConfigParser()
    reader.read(file_path)

    return reader

# reader object
reader = extract_config_info()

# extract info and assing to variables
API_KEY = reader['API']['API_KEY']
URL = reader['URL']['URL']
OUTPUT_PATH = reader['PATH']['output']
AZURE_CONNECTION_STRING = reader['AZURE']['connection_string']
CONTAINER_NAME = reader['AZURE']['container']

print(API_KEY, URL, OUTPUT_PATH, AZURE_CONNECTION_STRING, CONTAINER_NAME)