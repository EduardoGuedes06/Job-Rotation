import json

from numpy import append
from collections import defaultdict

with open("Fatura.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

Ldias_mes1 = []
Lfaturamento_mes1 = []

Ldias_mes2 = []
Lfaturamento_mes2 = []

Faturamento_max = 0
aux = 0


# para cada item do arquivo 
def Inserir():
    for i in dados:
     
        Ldias_mes1.append(i['dia'])
        Lfaturamento_mes1.append(i['faturamento'])


if __name__ == "__main__":
    Inserir()