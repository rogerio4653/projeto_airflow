from time import sleep

# Definindo as atividades 
def primera_atividades():
    print("minha primeira atividades")
    sleep(2)

def minha_segunda_atividade():
    print("minha segunda atividades")
    sleep(2)

def minha_terceira_atividade():
    print("minha terceira atividades")
    sleep(2)

def pipeline():
    primera_atividades()
    minha_segunda_atividade()
    minha_terceira_atividade()
    print("pipeline finalizou")

# Chamamdo a pipeline para executar 
pipeline()

