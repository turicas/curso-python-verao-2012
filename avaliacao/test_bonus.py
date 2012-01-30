#!/usr/bin/env python
# coding: utf-8

from resolucao import le_csv, agrega_valores, plota_grafico


registros = le_csv('exemplos/processos.csv')
valores_agregados = agrega_valores(registros)
plota_grafico(valores_agregados, 'processos-stf.png')
