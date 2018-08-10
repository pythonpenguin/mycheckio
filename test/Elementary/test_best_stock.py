from src.Elementary import best_stock


def test_one_values():
    d = {"A": 10.0}
    assert "A" == best_stock.best_stock(d)


def test_two_values():
    d = {"A": 10.0, "B": 0.2}
    assert "A" == best_stock.best_stock(d)


def test_100_values():
    d = {"A_%d" % x: float(x) for x in xrange(100)}
    assert "A_99" == best_stock.best_stock(d)
