import json
from typing import Dict

d=[]
m=[]
f=[]
mes1_max=0
mes2_max=0



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
            print(fatura)
    
    for i in range (59):
        
        if fatura[i] == int:  
            print()
            if m[1]:      
                   
                        
                if fatura[i] > mes1_max:
                    mes1_max = fatura[i]
                    print(mes1_max)
                    print("\nFatura do mes 1, dia",d[i],":",fatura[i])

            if m[2]:     
                   
                   
                        
                if fatura[i] > mes2_max:
                    mes2_max = fatura[i]
     


                
                
        else: fatura[i] == 'Nulo'
   
 