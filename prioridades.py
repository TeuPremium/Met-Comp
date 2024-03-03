from datetime import datetime
import pandas as pd

#Pegando um valor específico
"""
now = datetime(2022, 12, 31, 15, 30, 0)               # ano, mês, dia, hora, minutos, segundos.
agora = now.replace(second=0, microsecond=0).time()   #Valor de teste de um horário específico.
"""

#Pegando valor atual do horário
now = datetime.now()
agora = now.replace(second=0, microsecond=0).time()    #Valor de teste do horário atual

#Leitura do arquivo do ambiente e tornando em formato pandas
data = pd.read_csv("machine_power.csv")

#Tornando as colunas de tempo em formato de datetime
data['inicio_uso_tipico'] = pd.to_datetime(data['inicio_uso_tipico'], format='%H:%M').dt.time
data['fim_uso_tipico'] = pd.to_datetime(data['fim_uso_tipico'], format='%H:%M').dt.time

#Loop para verificar os horários típicos e alterar sua prioridade
for i, linha in data.iterrows():

    if not (linha['inicio_uso_tipico'] <= agora <= linha['fim_uso_tipico']): #Verificação se a sala está dentro do horário típico de funcionamento.
        if linha['prioridade'] < 4 and linha['fixo'] == 0:                   #Verifica o nível atual da prioridade e se a sala tem prioridade fixa
            data.at[i, 'prioridade'] += 1                                    #Alterando diretamente o valor da prioridade na linha e coluna especificada
            print(f"Prioridade da sala {linha['local']} modificada!")        #Print ilustrativo de qual sala teve prioridade modificada
 
