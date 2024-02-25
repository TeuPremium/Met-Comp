import os
import json
import pandas as pd
from datetime import datetime 
from app.functions.priority_queue import PriorityQueue
#rom priority_queue import PriorityQueue

# transformar as horas em um int 
def time_to_hour(time_str):
    hour = int(''.join(filter(str.isdigit, time_str)))   #Aplicando o a função filter. Retornará uma lista com apenas str de digitos e depois serão unidos pelo join
    return hour

def data_processing(filename):

    #print(os.path.join(os.getcwd(), 'machine_power.csv')) Usados por fins de debug caso o arquivo esteja no diretório errado
    machines = pd.read_csv(filename)

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
    dict_style = organizer.on_off_state()
    return dict_style

if __name__ == '__main__':
    print(data_processing('machine_power.csv'))





