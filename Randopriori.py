from random import randrange

def randopriori(machines):
  e=[]
  for i in range(0,len(machines)):
    e.append(randrange(2)) #cria um array binario aletorio
  for x in range(1,len(machines)):
    machines.loc[x,3] = e[x] #atribui o array ao em uso
