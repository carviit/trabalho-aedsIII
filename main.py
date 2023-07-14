from deputados_votacao import Deputados

gDep = Deputados()

# Criação do grafo de relacionamentos entre os deputados
gDep.criar_grafo()

# Escrita das informações sobre os relacionamentos no arquivo grafo_final.txt
gDep.escrever_grafo_final()

# Escrita da contagem da participação dos deputados no arquivo grafo_participacao.txt
gDep.escrever_grafo_participacao()
