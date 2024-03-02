from datetime import datetime
import pandas as pd

agora = datetime(2024, 3, 2, 20, 30)
hora, minutos = agora.hour, agora.minute

print(f"{hora}:{minutos}")

data = pd.read_csv("machine_power.csv")
#print(data)

data['inicio_uso_tipico'] = pd.to_datetime(data['inicio_uso_tipico'])
data['fim_uso_tipico'] = pd.to_datetime(data['fim_uso_tipico'])

data_time  = data.loc[:, ['inicio_uso_tipico', 'fim_uso_tipico']]
print(data_time)

for i , linha in data.iterrows():
    if linha['inicio_uso_tipico'] <= agora and linha['fim_uso_tipico']<=agora:
        if linha['prioridade'] < 5 :
            data.at[i, 'prioridade'] += 1
        print(f"Para a linha {i + 1}: fora")
    else:
        print(f"Para a linha {i + 1}: dentro")
print(data['prioridade'])