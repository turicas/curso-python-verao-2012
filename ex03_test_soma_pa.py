#!/usr/bin/env python

from nose.tools import assert_equals
from ex03_soma_pa import cria_soma_pa


def test_pa_com_a_1_igual_a_1_e_r_igual_a_2():
    pa = cria_soma_pa(1, 2)
    assert_equals(pa(4), 16)
    assert_equals(pa(5), 25)

def test_pa_com_a_1_igual_a_10_e_r_igual_a_3():
    pa = cria_soma_pa(10, 3)
    assert_equals(pa(2), 23)
    assert_equals(pa(3), 39)
    assert_equals(pa(4), 58)
