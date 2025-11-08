from time import sleep
from airflow.decorators import dag 
from datetime import datetime 


@dag(
        dag_id="minha_primeira_dag",
        description="minha etl braba" 
        schedule="* * * * *", 
        start_date=datetime(2025,11,8),
        catchup=False #backfill 
)

def pipeline():

    # Definindo as atividades 
    def primera_atividades():
        logger.info("minha primeira atividades")
        sleep(2)

    def minha_segunda_atividade():
        logger.info("minha segunda atividades")
        sleep(2)

    def minha_terceira_atividade():
        logger.info("minha terceira atividades")
        sleep(2)

    def quarta_atividade():
        print("pipeline finalizou")
    
        primera_atividades()
        minha_segunda_atividade()
        minha_terceira_atividade()
        quarta_atividade()