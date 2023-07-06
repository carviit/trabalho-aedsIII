import requests
import json

informacoesIDS = requests.get("https://dadosabertos.camara.leg.br/api/v2/votacoes?dataInicio=2022-01-01&ordem=DESC&ordenarPor=dataHoraRegistro")
informacoesIDS = informacoesIDS.json()

for i in range(len(informacoesIDS["dados"])):
    ids = informacoesIDS["dados"][i]

    ids_total = "https://dadosabertos.camara.leg.br/api/v2/votacoes/" +  ids["id"]  + "/votos"
    request = requests.get(ids_total)
    request = request.json()

    with open("ids.txt", 'a') as file:
        if request["dados"] != []:

            file.write(f"{ids_total}\n")  
