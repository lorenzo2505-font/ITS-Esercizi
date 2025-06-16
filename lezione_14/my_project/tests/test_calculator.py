from my_project.calculator import Calculator


def test_addition():

    calculation: Calculator = Calculator(10, 5)
    assert calculation.addition() == 13, "the sum is wrong"