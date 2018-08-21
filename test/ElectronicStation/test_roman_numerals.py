import pytest

from src.ElectronicStation.roman_numerals import RomanNumbersUnit, RomanNumbersDecine, RomanNumbersCent, \
    RomanNumbersMill, checkio


def test_correct_number_unit():
    assert isinstance(RomanNumbersUnit(1), RomanNumbersUnit)
    assert RomanNumbersUnit(1) == RomanNumbersUnit(1)
    assert set([RomanNumbersUnit(1) for x in xrange(6)]) == set([RomanNumbersUnit(1)])


def test_incorrect_number_unit():
    with pytest.raises(ValueError):
        assert RomanNumbersUnit(0)
        assert RomanNumbersUnit(10)
        assert RomanNumbersUnit(11)
        assert RomanNumbersUnit(100)


def test_number_less_than_10():
    assert "I" == RomanNumbersUnit(1).translate()
    assert "II" == RomanNumbersUnit(2).translate()
    assert "III" == RomanNumbersUnit(3).translate()
    assert "IV" == RomanNumbersUnit(4).translate()
    assert "V" == RomanNumbersUnit(5).translate()
    assert "VI" == RomanNumbersUnit(6).translate()
    assert "VII" == RomanNumbersUnit(7).translate()
    assert "VIII" == RomanNumbersUnit(8).translate()
    assert "IX" == RomanNumbersUnit(9).translate()


def test_number_less_than_100():
    assert "X" == RomanNumbersDecine(10).translate()
    assert "XXX" == RomanNumbersDecine(30).translate()
    assert "XL" == RomanNumbersDecine(40).translate()
    assert "L" == RomanNumbersDecine(50).translate()
    assert "LX" == RomanNumbersDecine(60).translate()
    assert "XC" == RomanNumbersDecine(90).translate()


def test_number_less_than_1000():
    assert "C" == RomanNumbersCent(100).translate()
    assert "D" == RomanNumbersCent(500).translate()
    assert "DC" == RomanNumbersCent(600).translate()
    assert "CM" == RomanNumbersCent(900).translate()


def test_numbe_less_than_4000():
    assert "MMM" == RomanNumbersMill(3000).translate()


def test_number_composed():
    assert "XIV" == RomanNumbersDecine(14).translate() + RomanNumbersUnit(4).translate()
    assert "CDLXXXIX" == RomanNumbersCent(489).translate() + RomanNumbersDecine(89).translate() + RomanNumbersUnit(
        9).translate()

def test_checkio():
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
