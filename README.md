# Descrição do Projeto

📜 Este projeto tem como objetivo criar um grafo de relacionamentos entre deputados com base em votações na Câmara dos Deputados do Brasil. Utilizando a API de Dados Abertos da Câmara dos Deputados, o programa realiza requisições para obter informações sobre votações e votos de deputados.

## Funcionamento

🔍 A classe `Deputados` contém os métodos necessários para criar o grafo de relacionamentos. A cada execução do programa, o método `criar_grafo` é acionado. Ele faz uma série de requisições para a API para obter as informações sobre as votações e votos dos deputados. Em seguida, cria o grafo de relacionamentos com base nos votos "Sim" e "Não" de cada deputado.

🔗 O grafo é representado por um dicionário de adjacências, em que cada deputado é um nó do grafo e as arestas representam os relacionamentos entre os deputados que votaram da mesma forma. Além disso, é contabilizada a participação de cada deputado nas votações.

📄 Os resultados do grafo são escritos nos arquivos `grafo_final.txt` e `grafo_participacao.txt`. O arquivo `grafo_final.txt` contém as informações sobre os relacionamentos entre os deputados, enquanto o arquivo `grafo_participacao.txt` apresenta a contagem de participação de cada deputado nas votações.