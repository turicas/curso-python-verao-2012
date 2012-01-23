from nose.tools import assert_equals
from romanos import converte_de_romanos_para_indoarabico


def test_I_deve_retornar_numeros_de_um_digito():
    assert_equals(converte_de_romanos_para_indoarabico('I'), 1)
    assert_equals(converte_de_romanos_para_indoarabico('V'), 5)
    assert_equals(converte_de_romanos_para_indoarabico('X'), 10)
    assert_equals(converte_de_romanos_para_indoarabico('L'), 50)
    assert_equals(converte_de_romanos_para_indoarabico('C'), 100)
    assert_equals(converte_de_romanos_para_indoarabico('D'), 500)
    assert_equals(converte_de_romanos_para_indoarabico('M'), 1000)
    
def test_numeros_repetidos_deve_retornar_o_multiplo():
    assert_equals(converte_de_romanos_para_indoarabico('II'), 2)
    assert_equals(converte_de_romanos_para_indoarabico('XX'), 20)
    assert_equals(converte_de_romanos_para_indoarabico('XXX'), 30)

def test_numeros_diferentes_somando():
    assert_equals(converte_de_romanos_para_indoarabico('VI'), 6)
    assert_equals(converte_de_romanos_para_indoarabico('VII'), 7)
    assert_equals(converte_de_romanos_para_indoarabico('VIII'), 8)
    assert_equals(converte_de_romanos_para_indoarabico('XI'), 11)
    assert_equals(converte_de_romanos_para_indoarabico('XII'), 12)
    assert_equals(converte_de_romanos_para_indoarabico('XIII'), 13)
    assert_equals(converte_de_romanos_para_indoarabico('CX'), 110)
    assert_equals(converte_de_romanos_para_indoarabico('CXI'), 111)
    assert_equals(converte_de_romanos_para_indoarabico('MDCLXVI'), 1666)
    assert_equals(converte_de_romanos_para_indoarabico('MDCLXVII'), 1667)
    assert_equals(converte_de_romanos_para_indoarabico('MDCLXVIII'), 1668)

def test_numeros_diferentes_subtraindo():
    assert_equals(converte_de_romanos_para_indoarabico('IX'), 9)
    assert_equals(converte_de_romanos_para_indoarabico('XC'), 90)
    assert_equals(converte_de_romanos_para_indoarabico('IV'), 4)
    assert_equals(converte_de_romanos_para_indoarabico('CDXLIV'), 444)
    assert_equals(converte_de_romanos_para_indoarabico('CMXCIX'), 999)
