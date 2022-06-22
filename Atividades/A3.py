import json
from typing import Dict

d=[]
m=[]
f=[]
meu_json=open("Fatura.json", encoding='utf-8')
dados = json.load(meu_json)


# para cada item do arquivo 
def Inserir():
    for i in dados:
     
        #print(i["dia"])
        m.append(i['mes'])
        d.append(i["dia"])
        f.append(i['faturamento'])
        

if __name__ == "__main__":
    Inserir()
    mes1_max=0
    mes1_min=99999
    diam1_max=0
    diam1_min=0
    total_mes1=0
    media_mes1=0


    mes2_max=0
    mes2_min=99999
    diam3_max=0
    diam3_min=0
    total_mes2=0
    media_mes2=0
    fatura=[]
    for element in f:
        if element == '':
           
            fatura.append('Nulo')
            
        else:
            fatura.append(int(element))
    count1=1
    count2=1
    for i in range (59):

        if m[i]=='1':
            if fatura[i]=='Nulo':
                pass
            else:
                total_mes1 = total_mes1 + fatura[i]
                count1=count1 + 1
                          
                if mes1_max < fatura[i]:
                    mes1_max = fatura[i]
                    diam1_max = d[i]
                if   mes1_min > fatura[i]:
                    mes1_min = fatura[i]
                    diam1_min = d[i]   
                
        elif m[i]=='2':
            if fatura[i]=='Nulo':
                pass
            else:
                
                total_mes2 = total_mes2 + fatura[i]
                count2=count2 + 1
            
                if mes2_max < fatura[i]:
                    mes2_max = fatura[i]
                    diam2_max = d[i] 
                if  mes2_min > fatura[i]:
                    mes2_min = fatura[i]
                    diam2_max = d[i]       
        else:
            print("Invalido")
    media_mes1 = (total_mes1/count1)
    media_mes2 = (total_mes2/count2)
    print("No Primeiro mes, a fatura minima foi de :",'R${:.2f}'.format(mes1_min),"e a maxima de:",'R${:.2f}'.format(mes1_max),"Tambem obtivemos uma média de :",'R${:.2f}'.format(media_mes1),"e um total de :",'R${:.2f}'.format(total_mes1),)
    print("\nNo Segundo mes, a fatura minima foi de :",'R${:.2f}'.format(mes2_min),"e a maxima de:",'R${:.2f}'.format(mes2_max),"Tambem obtivemos uma média de :",'R${:.2f}'.format(media_mes2),"e um total de :",'R${:.2f}'.format(total_mes2),)