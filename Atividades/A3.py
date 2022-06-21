import json

with open("Fatura.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


# para cada item do arquivo json
for i in dados:

    # imprimindo nome e idade formatados
    print(i['dia'], i['mes'],i['faturamento'])