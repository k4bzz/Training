import pytest

from palindrome import Number


def test_four_digit():
    test1 = Number(1221)
    assert test1.is_palindrome() == True


def test_three_digit():
    test2 = Number(345)
    assert test2.is_palindrome() == False


def test_negative_equal():
    test3 = Number(-11)
    assert test3.is_palindrome() == False


def test_zero():
    test4 = Number(0)
    assert test4.is_palindrome() == True

def test_not_a_number():
    test5 = Number("www")
    with pytest.raises(TypeError):
        test5.is_palindrome()

def test_random():
    test6 = Number("www")