from configs.info_config import BUCKET_NAME
from etl.aws_etl import connect_to_s3, upload_file

def aws_etl_pipeline(ti) -> None:

    file_path = ti.xcom_pull(task_ids='nba_games_extraction', key='return_value')

    if file_path:
        s3 = connect_to_s3()
        upload_file(s3, file_path, BUCKET_NAME, file_path.split('/')[-1])
    
    else:
        print('No NBA Games today. No files will be uploaded to the bucket.')