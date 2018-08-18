from src.Home import all_the_same


def test_proposed_by_problem():
    assert all_the_same.all_the_same([1, 1, 1]) == True
    assert all_the_same.all_the_same([1, 2, 1]) == False
    assert all_the_same.all_the_same(['a', 'a', 'a']) == True
    assert all_the_same.all_the_same([]) == True
    assert all_the_same.all_the_same([1]) == True
