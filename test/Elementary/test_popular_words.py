from src.Elementary import popular_words


def test_empty_text():
    assert {} == popular_words.popular_words("", [])


def test_one_text():
    assert {"foo": 1} == popular_words.popular_words("foo", ["foo"])
    assert {"foo": 1} == popular_words.popular_words("foo ", ["foo"])
    assert {"foo": 1} == popular_words.popular_words("foo   fao", ["foo"])


def test_assert_no_items():
    assert {"no": 0} == popular_words.popular_words("foo", ["no"])


def test_assert_multiple_values():
    assert {"foo": 4} == popular_words.popular_words("Foo is not foo but foo is foo clear?", ["foo"])


def test_only_lower_case():
    assert {"foo": 4} == popular_words.popular_words("FOO is not fOo but FoO is fOO clear?", ["foo"])


def test_more_words():
    assert popular_words.popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
