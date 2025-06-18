from my_project.calculator import Calculator
import pytest


'''def test_addition():

    calculation: Calculator = Calculator(10, 5)
    assert calculation.addition() == 13, "the sum is wrong"


def test_substraction():

    calculation: Calculator = Calculator(10, 5)
    assert calculation.subtraction() == 5, "the substraction is wrong"


def test_multiplication():

    calculation: Calculator = Calculator(10, 5)
    assert calculation.multiplication() == 50, "the multiplication is wrong"


def test_division():

    calculation: Calculator = Calculator(10, 5)
    assert calculation.division() == 2.00, "the quotient is wrong"'''


@pytest.fixture 

def calculation():

    # crea un'istanza di Calculator prima di ogni test

    return Calculator(10, 5)


def test_addition(calculation):

    assert calculation.addition() == 13, " the sum is wrong"

def test_substraction(calculation):

    assert calculation.subtraction() == 5, "the sub is wrong"

def test_multiplication(calculation):

    assert calculation.multiplication() == 50, "the prod is wrong"

def test_division(calculation):

    assert calculation.division() == 2.00 , "the quotient is wrong"






