#-*- coding: utf-8 -*-
import nose
from nose.tools import assert_equals
from r13 import palavra

def test_passando_string_de_uma_letra_minuscula():
    assert_equals(palavra('a'), 'n')
    assert_equals(palavra('z'), 'm')
    assert_equals(palavra('c'), 'p')
    
def test_passando_string_de_uma_letra_maiusculas():
    assert_equals(palavra('A'), 'N')
    assert_equals(palavra('Z'), 'M')
    assert_equals(palavra('F'), 'S')
    
def test_passando_string_nao_alfabeticas():
    assert_equals(palavra('3'), '3')
    assert_equals(palavra('$'), '$')
    
def test_passando_string_com_duas_letras():
    assert_equals(palavra('zc'), 'mp')

def test_passando_string_com_mais_que_duas_letras():
    assert_equals(palavra('zcaaaa'), 'mpnnnn')

def test_passando_string_com_mais_que_duas_letras_e_numeros():
    assert_equals(palavra('zcaa22'), 'mpnn22')

def test_passando_string_com_letras_maiusculas_minusculas():
    assert_equals(palavra('zCAa22'), 'mPNn22')
    
def test_passando_string_com_letras_acentuadas():
    assert_equals(palavra('áCAa22ç , "'), 'áPNn22ç , "')


nose.run()
