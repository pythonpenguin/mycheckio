from src.ElectronicStation import reverse_roman_numerals


def test_pure_number():
    assert 1 ==reverse_roman_numerals.reverse_roman(reverse_roman_numerals.UNUS)
    assert 10 == reverse_roman_numerals.reverse_roman(reverse_roman_numerals.DECEM)
    assert 500 == reverse_roman_numerals.reverse_roman(reverse_roman_numerals.CINQUECENTUM)

def test_less_10():
    assert 2 == reverse_roman_numerals.reverse_roman("II")
    assert 4 == reverse_roman_numerals.reverse_roman("IV")
    assert 6 == reverse_roman_numerals.reverse_roman("VI")
    assert 9 == reverse_roman_numerals.reverse_roman("IX")

def test_less_100():
    assert 99 == reverse_roman_numerals.reverse_roman("XCIX")
    assert 89 == reverse_roman_numerals.reverse_roman("LXXXIX")

def test_less_1000():
    assert 999 == reverse_roman_numerals.reverse_roman("CMXCIX")

def test_complete():
    assert 3905 == reverse_roman_numerals.reverse_roman("MMMCMV")
