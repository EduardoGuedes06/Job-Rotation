import json

from numpy import append
from collections import defaultdict

with open("Fatura.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

Ldias_mes = []
Lfaturamento_mes = []

Ldias_mesT = []
Lfaturamento_mesT = []

Ldias_mesT = []
Lfaturamento_mesT = []

Faturamento_max = 0
aux = 0


# para cada item do arquivo 
def Inserir():
    for i in dados:
     
        Ldias_mes.append(i['dia'])
        Lfaturamento_mes.append(i['faturamento'])


if __name__ == "__main__":
    Inserir()
    
    print(Lfaturamento_mes)



    
    
    
    
    

    
    
    
    
    
    
    
    
    