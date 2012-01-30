#!/usr/bin/env python
# coding: utf-8

import os
import tempfile
import nose
from nose.tools import assert_equals
from resolucao import plota_grafico


def test_deve_retornar_subplot_contendo_dados_corretos():
    arquivo = tempfile.NamedTemporaryFile(delete=False)
    arquivo.close()
    dados = {'SP': 300, 'RJ': 200}
    resultado = plota_grafico(dados, arquivo.name)
    os.remove(arquivo.name)
    x_tick_labels = resultado.get_xticklabels()
    ufs = [x_tick_labels[0].get_text(), x_tick_labels[1].get_text()]
    ufs.sort()
    assert_equals(ufs, ['RJ', 'SP'])
    y_values = [valor for valor in resultado.get_lines()[0].get_ydata()]
    y_values.sort()
    assert_equals(y_values, [200, 300])

nose.main()
