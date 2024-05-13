'''
Module contains attributes of information from '.config'.
'''

import configparser

def load_config(config_file: str) -> configparser.ConfigParser:
    '''
    Returns a ConfigParser object that can be use
    to return information from the 'config.ini' file.    
    '''
    
    config = configparser.ConfigParser()
    config.read(config_file)
    
    return config

# parser object
config = load_config('.config')

# database info
host = config.get('database', 'host')
user = config.get('database', 'user')
password = config.get('database', 'password')
database = config.get('database', 'database')

# url info
url = config.get('url', 'endpoint')