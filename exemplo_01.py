from time import sleep
from loguru import logger 

# Pegando log da aplicação
logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

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

def pipeline():
    primera_atividades()
    minha_segunda_atividade()
    minha_terceira_atividade()
    logger.info("pipeline finalizou")

# Chamamdo a pipeline para executar 
while True:
    pipeline()
    sleep(5)
