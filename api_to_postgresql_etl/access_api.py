'''
This module is used for passing GET Request to the public API.
'''

import requests


def get_request(url: str) -> list[dict]:
    '''
    This function returns the extracted data in form of JSON from Dota 2 API.
    '''
    
    # GET request to the API
    response = requests.get(url)
    
    # return data if successful
    if response.status_code == 200:
        
        data = response.json()
        print('Extracting data successful!')
        
        return data

    # return status_code if failed
    else:
        print(f'Transaction FAILED. Status code: {response.status_code}')
        return None
    
if __name__ == "__main__":
    get_request()