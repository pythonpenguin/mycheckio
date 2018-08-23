from src.ElectronicStation.time_converter_12_24 import time_converter


def test_time_converter():
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('12:00 p.m.') == '00:00'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
