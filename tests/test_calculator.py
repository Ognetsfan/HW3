'''My Calculator Test'''
from calculator import Calculator 

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(2,2) == 4

def test_subraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(2,2) == 0

def test_multiply():

    assert Calculator.multiply(2,2) == 4

def test_divide():

    assert Calculator.divide(2,2) == 1