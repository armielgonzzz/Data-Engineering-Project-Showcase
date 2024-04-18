import sys, os

# This line will enable us to import python scripts from other folders
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pipeline.nba_games_pipeline import nba_games_pipeline
from pipeline.upload_to_s3_pipeline import aws_etl_pipeline
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta, date



default_args = {
    'owner': 'Armiel',
    'start_date': datetime(2024, 4, 8),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
}


dag = DAG(
    dag_id='nba_games_today_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['nba', 'etl', 'pipeline']
)

extract = PythonOperator(
    task_id='nba_games_extraction',
    python_callable=nba_games_pipeline,
    op_kwargs={'file_name': f'{date.today() - timedelta(days=1)}'},
    dag=dag
)

upload = PythonOperator(
    task_id='upload_to_s3',
    python_callable=aws_etl_pipeline,
    dag=dag
)


extract >> upload