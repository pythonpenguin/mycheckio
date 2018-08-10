from src.ElectronicStation import date_and_time_converter


def test_date_and_time_converter():
    assert date_and_time_converter.date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    assert date_and_time_converter.date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    assert date_and_time_converter.date_time("05.07.2018 01:29") == "5 July 2018 year 1 hour 29 minutes"
