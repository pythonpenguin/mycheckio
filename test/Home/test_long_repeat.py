from src.Home import long_repeat


def test_long_repeat():
    assert long_repeat.long_repeat('sdsffffse') == 4
    assert long_repeat.long_repeat('ddvvrwwwrggg') == 3
    assert long_repeat.long_repeat('abababaab') == 2
    assert long_repeat.long_repeat('') == 0
