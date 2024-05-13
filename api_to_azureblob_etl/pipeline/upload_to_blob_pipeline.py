import os, sys

# This line will enable us to import python scripts from other folders
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from configs.info_config import CONNECTION_STRING, CONTAINER_NAME, OUTPUT_PATH
from etl.azure_blob_etl import connect_to_azure_container, upload_to_container
from datetime import date


def azure_container_pipeline(path: str) -> None:
    '''
    Creates reference for container and uploads the .csv file to container as a Blob Object

    :path: Reference of the directory of the saved local .csv file
    :return: None
    '''

    # get reference for container_client
    container_client = connect_to_azure_container(CONNECTION_STRING, CONTAINER_NAME)

    # run the upload function
    upload_to_container(container_client, path, f'{date.today()}_games.csv')

if __name__ == '__main__':
    azure_container_pipeline()