# Análise de Votações dos Deputados 🗳️

📜 Este projeto tem como objetivo realizar uma análise das votações na Câmara dos Deputados do Brasil, identificando os relacionamentos e a participação dos deputados. Utilizando a API de Dados Abertos da Câmara dos Deputados, o programa obtém informações sobre as votações e votos dos deputados.

## Funcionalidades

🔍 A classe `Deputados` contém os métodos necessários para realizar a análise das votações. Ao executar o programa, o método `criar_grafo` é acionado. Ele faz uma série de requisições à API para obter as informações sobre as votações e votos dos deputados. A partir dessas informações, é criado um grafo que representa os relacionamentos entre os deputados.

🔗 O grafo é construído com base nos votos "Sim" e "Não" dos deputados. Cada deputado é representado por um nó no grafo, e as arestas representam os relacionamentos entre os deputados que votaram da mesma forma. Além disso, é feita a contagem da participação de cada deputado nas votações.

📄 Os resultados da análise são escritos nos arquivos `grafo_final.txt` e `grafo_participacao.txt`. O arquivo `grafo_final.txt` contém as informações sobre os relacionamentos entre os deputados identificados no grafo. Já o arquivo `grafo_participacao.txt` apresenta a contagem da participação de cada deputado nas votações.