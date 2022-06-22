import json
from typing import Dict

d=[]
m=[]
f=[]
mes1_max=0
mes1_min=99999
diam1_max=0
diam1_min=0

mes2_max=0
mes2_min=99999
diam3_max=0
diam3_min=0

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
    fatura=[]
    for element in f:
        if element == '':
           
            fatura.append('Nulo')
            
        else:
            fatura.append(int(element))
            
    for i in range (59):

        if m[i]=='1':
            if fatura[i]=='Nulo':
                pass
            else:
                
                
                
                
                
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
                
                
                
           
                
                
                if mes2_max < fatura[i]:
                    mes2_max = fatura[i]
                    diam2_max = d[i] 
                if  mes2_min > fatura[i]:
                    mes2_min = fatura[i]
                    diam2_max = d[i]       
        else:
            print("Invalido")

     


                
                
    
   
 