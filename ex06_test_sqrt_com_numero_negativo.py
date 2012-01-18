from nose.tools import assert_equals
from ex06_sqrt_com_numero_negativo import sqrt


def test_numeros_positivos_devem_funcionar():
    assert_equals(sqrt(16), 4)
    assert_equals(sqrt(25), 5)
    assert_equals(sqrt(1048576), 1024)

def test_numeros_negativos_devem_retornar_complexos():
    assert_equals(sqrt(-16), 4j)
    assert_equals(sqrt(-25), 5j)
    assert_equals(sqrt(-1048576), 1024j)
