import os
import json
import pandas as pd

from random import randint
from datetime import datetime, time 
from app.functions.priority_queue import PriorityQueue
#rom priority_queue import PriorityQueue

# transformar as horas em um int 
def time_to_hour(dt_time):
    hour = dt_time.strftime('%H:%M')   #Aplicando ao formato de apenas Hora e minutos
    return hour


def random_in_use(filename):
    """Função responsável por deixar o estado de uso da sala de forma aleatória"""
    data = pd.read_csv(filename)

    for i, linha in data.iterrows():
        if linha['fixo'] == 0:                   #Verifico se é alguma sala sem ter uso fixo
            data.at[i, 'em_uso'] = randint(0, 1) #Alterando entre 0 ou 1 para o em uso

    return data 

def priority_check(filename):
    """Função responsável por fazer as devidas alterações de prioridade de acordo com o tempo atual"""

    #Pegando um valor específico
    """
    now = time(15, 30, 0)                                 # hora, minutos, segundos.
    agora = now.replace(second=0, microsecond=0)          #Valor de teste de um horário específico.
    """

    #Pegando valor atual do horário
    now = datetime.now()
    agora = now.replace(second=0, microsecond=0).time()    #Valor de teste do horário atual

    #Leitura do arquivo do ambiente e tornando em formato pandas e trocando o coluna 'em_uso' de forma aleatória
    data = random_in_use(filename)

    #Tornando as colunas de tempo em formato de datetime
    data['inicio_uso_tipico'] = pd.to_datetime(data['inicio_uso_tipico'], format='%H:%M').dt.time
    data['fim_uso_tipico'] = pd.to_datetime(data['fim_uso_tipico'], format='%H:%M').dt.time

    #Loop para verificar os horários típicos e alterar sua prioridade
    for i, linha in data.iterrows():

        if not (linha['inicio_uso_tipico'] <= agora <= linha['fim_uso_tipico']): #Verificação se a sala está dentro do horário típico de funcionamento.
            if linha['prioridade'] < 4 and linha['fixo'] == 0:                   #Verifica o nível atual da prioridade e se a sala tem prioridade fixa
                data.at[i, 'prioridade'] += 1                                    #Alterando diretamente o valor da prioridade na linha e coluna especificada
                #print(f"Prioridade da sala {linha['local']} modificada!")       #Print ilustrativo de qual sala teve prioridade modificada
        if linha['em_uso'] == 0:                                                 #Checando se não está em uso
            if linha['prioridade'] < 4:                                          #Verifica o nível atual da prioridade 
                data.at[i, 'prioridade'] += 1                                    #Alterando diretamente o valor da prioridade na linha e coluna especificada
        
    return data

def data_processing(filename):

    #print(os.path.join(os.getcwd(), 'machine_power.csv')) Usados por fins de debug caso o arquivo esteja no diretório errado
    machines = priority_check(filename)

    # aplicar a transformação de datas em valores
    machines['inicio_uso_tipico'] = machines['inicio_uso_tipico'].apply(time_to_hour)
    machines['fim_uso_tipico'] = machines['fim_uso_tipico'].apply(time_to_hour)

    # separar prioridades dos items
    priorities = machines['prioridade']

    # tratar itens para ficarem em formato correto para lista
    machines_values = machines.values
    machines = [list(row) for row in machines_values]        

    '''
    ============================================= IDEIA PRO PROJETO ===============================================
    a ideia que eu acho mais facil para lidar com nosso programa seria de depois que ler a lista original
    lidar só com listas do python, ao invés de salvar as coisas em um novo csv.
    A gente implementa alguma lógica para ir atualizando os itens corretamente.
    Os itens devem ter um critério baseado em suas caracteristicas para receberem uma nova prioridade
    Podemos usar o horário atual e funções assincronas que contam o tempo para atualizar a lista e retornar ela. 
    Pra fazer isso, temos que atualizar a lista baseado no id de cada item, para não desligar o que não devemos.

    ===============================================================================================================
    '''

    # Alimentar itens para a lista (pode ser feita uma classe ou função para isso)
    organizer = PriorityQueue()

    organizer.add_list(machines, priorities)

    #organizer.print_queue()
    list_style = organizer.on_off_state()
    return list_style

if __name__ == '__main__':
    print(data_processing('machine_power.csv'))





