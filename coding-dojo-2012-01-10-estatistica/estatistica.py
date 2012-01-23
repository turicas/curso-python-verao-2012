def estatistica(string_de_numeros):
    lista_de_numeros = []
    for i in string_de_numeros.split(','):
        lista_de_numeros.append(int(i))
    tamanho = len(lista_de_numeros)
    return [tamanho,
            min(lista_de_numeros), 
            max(lista_de_numeros), 
            float(sum(lista_de_numeros)) / tamanho]
    
