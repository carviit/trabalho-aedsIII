import requests
import json

class Deputados:
    def __init__(self):
        self.adj_list = {}
        self.num_nos = 0
        self.num_arestas = 0

    def adicionar_no(self, no):
        if no in self.adj_list:
            return
        self.adj_list[no] = {}
        self.adj_list[no]["participacao"] = 0
        self.num_nos += 1

    def adicionar_aresta(self, no1, no2):
        if no1 not in self.adj_list:
            self.adicionar_no(no1)
        if no2 not in self.adj_list:
            self.adicionar_no(no2)
        if no2 in self.adj_list[no1]:
            self.adj_list[no1][no2] += 1
        else:
            self.adj_list[no1][no2] = 1
            self.num_arestas += 1

    def criar_grafo(self):
        votos_sim = []
        votos_nao = []

        id_votacao = requests.get("https://dadosabertos.camara.leg.br/api/v2/votacoes?dataInicio=2022-01-01&ordem=DESC&ordenarPor=dataHoraRegistro")
        id_votacao = id_votacao.json()

        for votacao in id_votacao["dados"]:
            id = "https://dadosabertos.camara.leg.br/api/v2/votacoes/" + votacao["id"] + "/votos"
            votos = requests.get(id)
            votos = votos.json()
            for voto in votos["dados"]:
                voto_atual = voto
                if voto_atual["tipoVoto"] == "Sim":
                    votos_sim.append(voto_atual["deputado_"]["nome"])
                elif voto_atual["tipoVoto"] == "Não":
                    votos_nao.append(voto_atual["deputado_"]["nome"])

            for dep in votos_sim:
                for dep2 in votos_sim:
                    if dep == dep2:
                        continue
                    self.adicionar_aresta(dep, dep2)
                self.adj_list[dep]["participacao"] += 1

            for dep in votos_nao:
                for dep2 in votos_nao:
                    if dep == dep2:
                        continue
                    self.adicionar_aresta(dep, dep2)
                self.adj_list[dep]["participacao"] += 1

            votos_sim = []
            votos_nao = []

    def escrever_grafo_final(self):
        with open("grafo_final.txt", 'w') as file:
            file.write(f"{self.num_nos} {self.num_arestas}\n")
            for dep in self.adj_list:
                for dep2 in self.adj_list[dep]:
                    if dep2 != "participacao":
                        file.write(f"{dep} {dep2} {self.adj_list[dep][dep2]}\n")

    def escrever_grafo_participacao(self):
        with open("grafo_participacao.txt", 'w') as file:
            for dep in self.adj_list:
                file.write(f"{dep} {self.adj_list[dep]['participacao']}\n")

if __name__ == "__main__":
    grafoDeputados = Deputados()

    grafoDeputados.criar_grafo()

    grafoDeputados.escrever_grafo_final()

    grafoDeputados.escrever_grafo_participacao()
