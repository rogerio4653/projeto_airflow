from time import sleep
from airflow.decorators import dag, task 
from datetime import datetime

@dag(
    dag_id="minha_primeira_dag",
    description="minha etl braba",
    schedule="* * * * *", 
    start_date=datetime(2025, 11, 8),
    catchup=False
)
def pipeline():
    @task 
    def primera_atividades():
        print("minha primeira atividade")
        sleep(2)

    @task
    def minha_segunda_atividade():
        print("minha segunda atividade")
        sleep(2)

    @task
    def minha_terceira_atividade():
        print("minha terceira atividade")
        sleep(2)

    @task
    def quarta_atividade():
        print("pipeline finalizou")
    
    t1 = primera_atividades()
    t2 = minha_segunda_atividade()
    t3 = minha_terceira_atividade()
    t4 = quarta_atividade()

    # Usa operadores para rodar as tasks
    t1 >> [t2, t3] 
    t3 << t4
    t1.setdownstream([t2,t3])
    t3.set_upstream(t4)

pipeline()  # ← CORRETO: Agora está fora da função, sem indentação