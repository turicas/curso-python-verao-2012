from nose.tools import assert_equals
from ex05_minmax import minimo, maximo


def test_minimo():
    assert_equals(minimo([2, 5, 10, 9, 1]), 1)
    assert_equals(minimo([-1, -2, -20, -5]), -20)

def test_maximo():
    assert_equals(maximo([2, 5, 10, 9, 1]), 10)
    assert_equals(maximo([-1, -2, -20, -5]), -1)
