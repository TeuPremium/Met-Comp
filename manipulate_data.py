import pandas as pd
from datetime import datetime 
from priority_queue import PriorityQueue

machines = pd.read_csv('machine_power.csv')

# transformar as horas em um int 
def time_to_hour(time_str):
    hour = int(''.join(map(str, map(int, time_str.replace(':', '')))))
    return hour

# aplicar a transformação para todos os valores
machines['inicio_uso_tipico'] = machines['inicio_uso_tipico'].apply(time_to_hour)
machines['fim_uso_tipico'] = machines['fim_uso_tipico'].apply(time_to_hour)

priorities = machines['prioridade']
machines = machines.drop(['prioridade'], axis=1)

# Get the values of the DataFrame as a NumPy array
machines_values = machines.values

# Convert each row into a list and store them in a list
machines = [list(row) for row in machines_values]



organizer = PriorityQueue()

organizer.add_list(machines, priorities)

organizer.print_queue()

# print(organizer.get_queue())



