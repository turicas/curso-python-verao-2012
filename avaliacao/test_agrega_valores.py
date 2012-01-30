#!/usr/bin/env python
# coding: utf-8

from random import random
import nose
from nose.tools import assert_equals
from resolucao import agrega_valores


def test_deve_retornar_dicionario_com_uf_como_chave_e_processos_como_valor():
    dados = [['RJ', 2010, 123], ['SP', 2010, 456], ['RS', 2010, 234]]
    resultado = agrega_valores(dados)
    assert_equals(resultado, {'RJ': 123, 'SP': 456, 'RS': 234})

def test_deve_somar_valores_por_uf_independente_de_ano():
    dados = [['RJ', 2010, 100], ['SP', 2010, 400], ['RS', 2010, 200],
             ['RJ', 2009, 200], ['SP', 2009, 500], ['RS', 2009, 300]]
    resultado = agrega_valores(dados)
    assert_equals(resultado, {'RJ': 300, 'SP': 900, 'RS': 500})

nose.main()
