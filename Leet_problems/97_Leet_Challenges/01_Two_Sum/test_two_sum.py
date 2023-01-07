import pytest
from two_sum import NumList


def test_on_edges():
    test = NumList([2, 11, 7, 3], 5)
    assert test.two_sum() == [0, 3]


def test_next_to_each_other():
    test = NumList([2, 7, 11, 15], 9)
    assert test.two_sum() == [0, 1]


def test_second_half():
    test = NumList([3, 2, 4], 6)
    assert test.two_sum() == [1, 2]


def test_list_of_two():
    test = NumList([3, 3], 6)
    assert test.two_sum() == [0, 1]


def test_wrong_type():
    test = NumList([1, 2], "g")
    with pytest.raises(TypeError):
        test.two_sum()


def test_empty_list():
    test = NumList([], 6)
    assert test.two_sum() is None


def test_list_of_one():
    test = NumList([6], 6)
    assert test.two_sum() is None
