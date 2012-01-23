from nose.tools import assert_equals
from fizzbuzz import fizzbuzz

def test_nao_multiplos_de_3_e_5_deve_retornar_proprio_numero():
    assert_equals(fizzbuzz(1), "1")
    assert_equals(fizzbuzz(2), "2")
    
 
def test_multiplo_de_3_retorna_fizz():
    assert_equals(fizzbuzz(3), "fizz")
    assert_equals(fizzbuzz(9), "fizz")
    assert_equals(fizzbuzz(12), "fizz")
    assert_equals(fizzbuzz(21), "fizz")

def test_5_deve_retornar_buzz():
    assert_equals(fizzbuzz(5), "buzz")
    assert_equals(fizzbuzz(10), "buzz")
    assert_equals(fizzbuzz(20), "buzz")
    assert_equals(fizzbuzz(25), "buzz")
    
def teste_multiplo_15_deve_retornar_fizzbuzz():
    assert_equals(fizzbuzz(15), "fizzbuzz") 
    assert_equals (fizzbuzz(300), "fizzbuzz")  
