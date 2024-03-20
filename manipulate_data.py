import pandas as pd
from priority_queue import PriorityQueue

machines = pd.read_csv('machine_power.csv')

# transformar as horas em um int 
def time_to_hour(time_str):
    hour = int(''.join(filter(str.isdigit, time_str)))   #Aplicando o a função filter. Retornará uma lista com apenas str de digitos e depois serão unidos pelo join
    return hour

# aplicar a transformação de datas em valores
machines['inicio_uso_tipico'] = machines['inicio_uso_tipico'].apply(time_to_hour)
machines['fim_uso_tipico'] = machines['fim_uso_tipico'].apply(time_to_hour)

# separar prioridades dos items
priorities = machines['prioridade']

# tratar itens para ficarem em formato correto para lista
machines_values = machines.values
machines = [list(row) for row in machines_values]        


# Alimentar itens para a lista (pode ser feita uma classe ou função para isso)
organizer = PriorityQueue()

organizer.add_list(machines, priorities)

# print(organizer.get_queue())

organizer.print_queue()
print("testando")





