from src.Home import sun_angle


def test_proposed_by_exercise():
    assert sun_angle.sun_angle("07:00") == 15
    assert sun_angle.sun_angle("01:23") == "I don't see the sun!"


def test_sunrise():
    assert sun_angle.sun_angle("06:00") == 0
    assert sun_angle.sun_angle("05:59") == "I don't see the sun!"

def test_sunset():
    assert sun_angle.sun_angle("18:01") == "I don't see the sun!"

def test_