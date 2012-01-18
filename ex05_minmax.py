def minimo(lista):
    """Essa funcao recebe uma lista como parametro e retorna o menor numero
    contido nela. A lista pode ter qualquer tipo de objeto.

    Exemplo:
    >>> minimo([3, 2, 1])
    1
    """
    menor = lista[0]
    for elemento in lista[1:]:
        if elemento < menor:
            menor = elemento
    return menor

def maximo(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior
