import pandas as pd
from datetime import datetime 


machines = pd.read_csv('machine_power.csv')

# transformar as horas em um int 
def time_to_hour(time_str):
    hour = int(''.join(map(str, map(int, time_str.replace(':', '')))))
    return hour

# aplicar a transformação para todos os valores
machines['inicio_uso_tipico'] = machines['inicio_uso_tipico'].apply(time_to_hour)
machines['fim_uso_tipico'] = machines['fim_uso_tipico'].apply(time_to_hour)

priorities = machines['prioridade']
print(priorities)
machines = machines.drop(['prioridade'], axis=1)

print(machines)