from azure.storage.blob import BlobServiceClient



def connect_to_azure_container(connection_string: str, container_name: str) -> str:
    '''
    Create a Blob Container Reference

    :connection_string: A unique string from Azure Storage Account that acts as a key
    :container_name: Name of the container created in Azure Blob Storage
    :return: Container Reference that will be used to upload blobs inside the container
    '''

    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # return reference for blob_service and container_client
        return container_client
    
    except Exception as e:
        print(f'Error in getting the Azure account references: {e}')

def upload_to_container(container_client: str, local_file: str, blob_name: str) -> None:
    '''
    Uploads the file to the pre-defined container in Azure Blob Storage

    :container_client: Name of the container that will store the nba-games file
    :local_file: Filename of the nba-games that is saved in the local directory
    :blob_name: The name to be given to the blob in Azure Blob Storage
    :return: None
    '''

    try:
        with open(local_file, 'rb') as read_data:
            blob_client = container_client.upload_blob(name=blob_name, data=read_data)
            print(f'Successfully uploaded the file to the container with filename {blob_name}')
    
    except Exception as e:
        print(f'Error while uploading the file to container: {e}')