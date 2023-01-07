import pytest

from roman_to_integer import RomanNum


# Doesnt work as __init__ requires user input. Needs more thinking on how to mock it
# @pytest.fixture
# def result():
#     return RomanNum()


def test_v(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "V")
    result = RomanNum()
    assert result.convert_roman_to_int() == 5


def test_iii(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "III")
    result = RomanNum()
    assert result.convert_roman_to_int() == 3


def test_lviii(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "LVIII")
    result = RomanNum()
    assert result.convert_roman_to_int() == 58


def test_mcmxciv(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "MCMXCIV")
    result = RomanNum()
    assert result.convert_roman_to_int() == 1994


def test_xlix(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "XLIX")
    result = RomanNum()
    assert result.convert_roman_to_int() == 49
