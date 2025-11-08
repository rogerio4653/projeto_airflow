from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Função que você deseja executar
def helloWorld():
    print("Hello World")

# Definir o default_args, incluindo o schedule_interval
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 8),  # Data de início
    'catchup': False,  # Não tentar executar tarefas para datas passadas
}

# Definir o DAG
dag = DAG(
    'hello_world_dag',  # ID da DAG
    default_args=default_args,
    description='Uma DAG de exemplo',
    schedule='* * * * *',  # Rodar a cada minuto
)

# Tarefa que executa a função helloWorld
hello_world_task = PythonOperator(
    task_id='hello_world_task',
    python_callable=helloWorld,
    dag=dag,
)
