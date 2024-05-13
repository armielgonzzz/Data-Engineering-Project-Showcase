from pipeline.nba_games_pipeline import nba_games_pipeline
from pipeline.upload_to_blob_pipeline import azure_container_pipeline
from datetime import date

if __name__ == '__main__':
    path = nba_games_pipeline(date.today())
    azure_container_pipeline(path)