from src.Elementary import bigger_price


def test_one_element_requested():
    assert bigger_price.bigger_price(1, [{"name": "pen", "price": 5},
                                         {"name": "whiteboard", "price": 170}]) == [
               {"name": "whiteboard", "price": 170}]


def test_two_element_requested():
    assert bigger_price.bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First"
