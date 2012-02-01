#!/usr/bin/env python
# coding: utf-8

import csv
from matplotlib.pyplot import figure


def le_csv(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    nova_lista = []
    for linha in arquivo:
        nova_lista.append(linha.replace('\n', '').split(','))
    #nova_lista = [linha.replace('\n', '').split(',') for linha in arquivo]
    arquivo.close()
    nova_lista.pop(0)
    for registro in nova_lista:
        registro[1] = int(registro[1])
        registro[2] = int(registro[2])
    return nova_lista

def le_csv_solucao_2(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    nova_lista = []
    for linha in arquivo:
        registro = linha.replace('\n', '').split(',')
        if registro != ['uf', 'ano', 'processos']:
            registro[1] = int(registro[1])
            registro[2] = int(registro[2])
            nova_lista.append(registro)
    arquivo.close()
    return nova_lista

def le_csv_solucao_3(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    nova_lista = []
    for indice, linha in enumerate(arquivo):
        if indice > 0:
            registro = linha.replace('\n', '').split(',')
            registro[1] = int(registro[1])
            registro[2] = int(registro[2])
            nova_lista.append(registro)
    arquivo.close()
    return nova_lista

def le_csv_solucao_4(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    nova_lista = []
    for indice, linha in enumerate(arquivo):
        if indice > 0:
            uf = linha[0:2]
            ano = int(linha[3:7])
            processos = int(linha[8:-1])
            nova_lista.append([uf, ano, processos])
    arquivo.close()
    return nova_lista

def le_csv_solucao_5(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    nova_lista = []
    for indice, registro in enumerate(csv.reader(arquivo)):
        if indice > 0:
            registro[1] = int(registro[1])
            registro[2] = int(registro[2])
            nova_lista.append(registro)
    arquivo.close()
    return nova_lista

def agrega_valores(lista):
    dados = {}
    for registro in lista:
        dados[registro[0]] = 0
    for registro in lista:
        dados[registro[0]] += registro[2]
    return dados

def agrega_valores_solucao_2(lista):
    dados = {}
    for registro in lista:
        if registro[0] not in dados:
            dados[registro[0]] = registro[2]
        else:
            dados[registro[0]] += registro[2]
    return dados

def agrega_valores_solucao_3(lista):
    dados = {}
    for registro in lista:
        if registro[0] not in dados:
            dados[registro[0]] = 0
        dados[registro[0]] += registro[2]
    return dados

def plota_grafico_(dados, nome_arquivo):
    x_labels = dados.keys()
    y = dados.values()

    x = x_ticks = range(len(x_labels))
    figura = figure(figsize=(15, 11.25), dpi=90)
    subplot = figura.add_subplot(1, 1, 1)
    subplot.grid(True) # opcional (poderia ser 'False' ou ser omitido)
    subplot.set_yscale('linear') # poderia ser omitido, poderia ser 'log'
    subplot.plot(y) # poderia ser subplot.bar(x, y) para gráfico de barras
    subplot.set_xticks(x_ticks)
    subplot.set_xticklabels(x_labels)
    figura.savefig(nome_arquivo)
    return subplot

def plota_grafico__(dados, nome_arquivo):
    x_labels = dados.keys()
    x_labels.sort()
    y = []
    for valor in x_labels:
        y.append(dados[valor])

    x = x_ticks = range(len(x_labels))
    figura = figure(figsize=(15, 11.25), dpi=90)
    subplot = figura.add_subplot(1, 1, 1)
    subplot.grid(True) # opcional (poderia ser 'False' ou ser omitido)
    subplot.set_yscale('linear') # poderia ser omitido, poderia ser 'log'
    subplot.plot(y) # poderia ser subplot.bar(x, y) para gráfico de barras
    subplot.set_xticks(x_ticks)
    subplot.set_xticklabels(x_labels)
    figura.savefig(nome_arquivo)
    return subplot

def plota_grafico(dados, nome_arquivo):
    itens = dados.items()
    itens.sort(lambda x, y: cmp(y[1], x[1]))
    x_labels = [uf for (uf, processos) in itens]
    y = [processos for (uf, processos) in itens]

    x = x_ticks = range(len(x_labels))
    figura = figure(figsize=(15, 11.25), dpi=90)
    subplot = figura.add_subplot(1, 1, 1)
    subplot.grid(True) # opcional (poderia ser 'False' ou ser omitido)
    subplot.set_yscale('linear') # poderia ser omitido, poderia ser 'log'
    subplot.plot(y) # poderia ser subplot.bar(x, y) para gráfico de barras
    subplot.set_xticks(x_ticks)
    subplot.set_xticklabels(x_labels)
    figura.savefig(nome_arquivo)
    return subplot
