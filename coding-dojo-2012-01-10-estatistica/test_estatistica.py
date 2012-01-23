from nose.tools import assert_equals
from estatistica import estatistica

def test_passando_somente_um_numero_retorna_lista_com_ele_proprio():
    assert_equals(estatistica("1"), [1, 1, 1, 1])

def test_passando_apenas_numero_dois_retorna_lista_equivalente():
    assert_equals(estatistica("2"), [1, 2, 2, 2])
    
def test_passando_apenas_numero_tres_retorna_lista_equivalente():
    assert_equals(estatistica("3"), [1, 3, 3, 3])
    
def test_passando_apenas_numero_dez_retorna_lista_equivalente():
    assert_equals(estatistica("10"), [1, 10, 10, 10])
    
def test_passando_dois_numeros_retorna_lista_equivalente():
    assert_equals(estatistica("1,1"), [2, 1, 1, 1])
    
def test_passando_dois_outros_numeros_retorna_lista_equivalente():
    assert_equals(estatistica("1,10"), [2, 1, 10, 5.5])

def test_passando_lista_com_numeros_negativos():
    assert_equals(estatistica("-1,-3,1,10,-2"), [5, -3, 10, 1])
    
    
