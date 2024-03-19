
import time
import EmonLib 
import machine

EnergyMonitor = emon1
 
#Tensao da rede eletrica
rede = 220.0
 
#Pinos do sensor SCT
pino_sct=[]
pino_sct[0] = machine.Pin(1, machine.Pin.OUT)
pino_sct[1] = machine.Pin(2, machine.Pin.OUT)
pino_sct[2] = machine.Pin(3, machine.Pin.OUT)
pino_sct[3] = machine.Pin(4, machine.Pin.OUT)
pino_sct[4] = machine.Pin(5, machine.Pin.OUT)
pino_sct[5] = machine.Pin(6, machine.Pin.OUT)
pino_sct[6] = machine.Pin(7, machine.Pin.OUT)
pino_sct[7] = machine.Pin(8, machine.Pin.OUT)
pino_sct[8] = machine.Pin(9, machine.Pin.OUT)
pino_sct[9] = machine.Pin(10, machine.Pin.OUT)

#Pino, calibracao - Cur Const= Ratio/BurdenR. 1800/62 = 29. 
corrente=[]
for x in range(0,9);
    corrente[x]= emon1.current(pino_sct[x], 29)
Irms=[]
kwh=[]
while True: 
  #Calcula a corrente
  for y in range(0,9):  
    Irms[y] = corrente[y].calcIrms(1480);
  #Mostra o valor da corrente
    #print("Corrente : ")
    #print(Irms)
   
  #Calcula e mostra o valor da potencia e manda para a main
  def mudkwh(machines):
    for i in range(0,9):
        kwh[i]=(Irms[i]*rede)
        for x in range(1,len(machines)):
            machines.loc[x,2] = kwh[x] #atribui o array ao kwh

  time.sleep(1000)