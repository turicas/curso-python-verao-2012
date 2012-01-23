from nose.tools import assert_equals
from exemplo import soma


def test_funcao_soma_deve_retornar_a_adicao_dos_parametros():
    assert_equals(soma(1, 2), 3)
    assert_equals(soma(5.0, 2.5), 7.5)

def test_funcao_soma_deve_somar_numeros_negativos():
    assert_equals(soma(-5, -3), -8)
    assert_equals(soma(-10, 5), -5)
