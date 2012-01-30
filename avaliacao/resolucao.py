#!/usr/bin/env python
# coding: utf-8

"""Essa avaliação é dividida em 3 exercícios, sendo a resolução de cada um
independente do outro. Em todos eles você precisará criar uma função que
recebe e retorna objetos. Apesar dessas funções poderem ser utilizadas uma
a partir da outra (uma recebendo o resultado da outra), as resoluções delas
são independentes, ou seja, você terá todas as instruções para fazer o
exercício 3, mesmo não tendo feito o 2.

Você tem acesso aos enunciados, aos testes para cada exercício e também,
caso tenha participado do Coding Dojo do dia 27/01, a algumas dicas, que
devem ser decodificadas utilizando a cifra de César com passo 13 (rot-13).
Os enunciados estão contidos em _docstrings_ no arquivo `resolucao.py`,
que deve ser utilizado como base para a resolução dessa avaliação. As dicas
codificadas estão contidas apenas no arquivo `README.markdown`. Você deve
colocar seu nome na variável `nome` (que está após a _docstring_ do módulo
`resolucao.py`).

Cada exercício possui um arquivo de teste associado, cujo nome é
`test_nome_da_funcao_a_ser_criada.py`. Para verificar se sua implementação
da função está funcionando como esperado, apenas rode o arquivo de testes
com o comando `nosetests nome_do_arquivo.py`.

Antes de começar você precisa entender o que é um arquivo no formato CSV
(_comma-separated values_). Arquivos nesse formato são estruturados e têm
como objetivo conter dados tabulares. Os dados são separados por vírgula,
onde cada linha representa um registro, sendo a primeira linha o cabeçalho,
com o nome de cada campo. Pense, por exemplo, na tabela que está no arquivo
`exemplos/planilha.png` (anexado a essa avaliação). Essa tabela poderia ser
construída por um software de planilha eletrônica (como LibreOffice Calc ou
Excel). Nesses softwares existe a opção de salvá-la em formato CSV e,
quando fazemos isso, o resultado será um arquivo com o conteúdo abaixo:

    uf,ano,processos
    RJ,2007,67282
    RS,2007,94445
    SP,2007,134511
    RJ,2009,23080
    RS,2009,30897
    SP,2009,44668

Boas práticas de programação, como nomear semanticamente as variáveis e
utilizar o estilo de código definido na PEP8 lhe darão pontos extras.

Happy hacking! :-)"""

nome = "Seu Nome Aqui"

def le_csv():
    """Essa função deve receber um único parâmetro: o nome de um arquivo CSV a
    ser lido e processado.

    Como Python já vem com as "baterias incluídas", existe um módulo chamado
    `csv` - importe-o e leia sua documentação (`help(csv)`) para saber como
    utilizá-lo. Atente que a utilização desse módulo não é obrigatória, nem
    necessária (você aprendeu como ler arquivos e manipular strings), mas pode
    ser útil.

    Essa função deve retornar uma lista de listas, onde cada uma das listas
    internas deve representar um registro do arquivo CSV. O cabeçalho deve ser
    omitido. Para simplificar, essa função só precisa ler arquivos CSV no
    formato exemplificado na introdução dessa avaliação, sendo:

    - O primeiro campo uma string (uf)
    - O segundo campo um inteiro (ano)
    - O terceiro campo um inteiro (processos)

    Assim, um exemplo de registro seria:

        ['RJ', 2007, 67282]

    Caso o arquivo CSV exemplificado na introdução fosse salvo em `dados.csv`,
    ao chamarmos `le_csv('dados.csv')` deveríamos receber como retorno a
    seguinte lista:

        [['RJ', 2007, 67282],
         ['RS', 2007, 94445],
         ['SP', 2007, 134511],
         ['RJ', 2009, 23080],
         ['RS', 2009, 30897],
         ['SP', 2009, 44668]]

    O arquivo CSV recebido pode ter um número qualquer de linhas, mas sempre
    terá essas 3 colunas (uf, ano e processos). Ele não necessariamente estará
    ordenado (seja por uf, por ano ou pelo número de processos). Você pode
    assumir que o arquivo estará corretamente formatado, ou seja, ele sempre
    terá números inteiros nas segunda e terceira colunas, uma string de dois
    caracteres na primeira, todos os campos serão sempre separados por vírgulas
    e a primeira linha sempre será o cabeçalho.

    Os testes para esse exercício estão no arquivo `test_le_csv.py`."""
    pass

def agrega_valores():
    """Essa função deve se chamar `agrega_valores`, receberá uma lista
    como a retornada pela função `le_csv` e retornará um dicionário, contendo
    o somatório de processos por estado (independente do ano). Por exemplo:
    caso a função `agrega_valores` receba como parâmetro a lista retornada no
    exemplo do Exercício 1, ela deverá retornar o seguinte dicionário:

        {'RJ': 90362, 'RS': 125342, 'SP': 179179}

    Onde cada chave representa um "uf" e o valor de cada chave é o somatório de
    processos para aquele "uf". Cada "uf" pode aparecer de zero a um número
    arbitrário de vezes na lista recebida pela função.

    Os testes para esse exercício estão no arquivo `test_agrega_valores.py`."""
    pass

def plota_grafico():
    """Essa função deve se chamar `plota_grafico` e receberá dois parâmetros:
    um dicionário no mesmo formato do que deve ser retornado pela função
    `agrega_valores` e o nome de um arquivo. Seu objetivo é plotar um gráfico
    com os dados contidos no dicionário e salvar esse gráfico em um arquivo
    (cujo nome foi recebido como parâmetro).

    Os UFs (SP, RJ etc.) devem ficar no eixo x do gráfico e o número de
    processos, no eixo y. Por exemplo, o código:

        plota_grafico({'SP': 200, 'RJ': 100, 'RS': 150, 'MG': 125}, 'ex3.png')

    deve gerar um gráfico igual ao que está disponível em `exemplos/ex3.png`.

    Você deverá utilziar o arquivo `exemplos/grafico.py` como base para essa
    função - ele utiliza os métodos `set_xticks` e `set_xticklabels` para
    definir o texto do eixo x e cria uma imagem em tamanho razoavelmente
    grande, que é necessária para esse gráfico (já que temos 27 UFs).
    Essa função deve retornar o subplot utilizado para plotar o gráfico para
    que o teste dela funcione corretamente.

    Os testes para esse exercício estão no arquivo `test_plota_grafico.py`."""
    pass

