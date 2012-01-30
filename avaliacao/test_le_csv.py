#!/usr/bin/env python
# coding: utf-8

import os
import tempfile
from random import random
import nose
from nose.tools import assert_equals
from resolucao import le_csv


def test_deve_retornar_uma_lista_cujo_tamanho_eh_o_numero_de_registros():
    arquivo = tempfile.NamedTemporaryFile(delete=False)
    arquivo.write('uf,ano,processos\nRJ,2010,100\nRJ,2009,150')
    arquivo.close()
    resultado = le_csv(arquivo.name)
    os.remove(arquivo.name)
    assert_equals(type(resultado), list)
    assert_equals(len(resultado), 2)

def test_deve_retornar_tipos_corretos():
    arquivo = tempfile.NamedTemporaryFile(delete=False)
    arquivo.write('uf,ano,processos\nRJ,2010,100\nRJ,2009,150')
    arquivo.close()
    resultado = le_csv(arquivo.name)
    os.remove(arquivo.name)
    assert_equals(type(resultado[0][0]), str)
    assert_equals(type(resultado[0][1]), int)
    assert_equals(type(resultado[0][2]), int)
    assert_equals(type(resultado[1][0]), str)
    assert_equals(type(resultado[1][1]), int)
    assert_equals(type(resultado[1][2]), int)

def test_deve_retornar_dados_corretos():
    arquivo = tempfile.NamedTemporaryFile(delete=False)
    dados = []
    arquivo.write('uf,ano,processos\n')
    for uf in ('RJ', 'SP', 'MG', 'RS'):
        for ano in (2007, 2008, 2009):
            dados.append([uf, ano, int(random() * 10000)])
            arquivo.write('{},{},{}\n'.format(*dados[-1]))
    arquivo.close()
    resultado = le_csv(arquivo.name)
    os.remove(arquivo.name)
    assert_equals(resultado, dados)

nose.main()
