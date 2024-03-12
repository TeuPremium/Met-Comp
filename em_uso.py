def em_uso(machines):
    for i in range (1,len(machines)):
        if (int(machines.loc[i,3])==0) and (int(machines.loc[i,4])==0):#checa se o em uso e fixo estao desligado
            a=int(machines.loc[i,1])#caso esteja reduz a prioridade
            #print(a)
            a+=1
            machines.loc[i,1] = a
