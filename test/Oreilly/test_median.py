from src.Oreilly import median


def test_proposed():
    assert median.checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert median.checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert median.checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert median.checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    assert median.checkio(list(range(1000000))) == 499999.5, "Long."
