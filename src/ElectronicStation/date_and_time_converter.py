import datetime


def date_time(time):
    """

    :param str time:
    :rtype str:
    """
    fmt = "%%d %B %Y year %%d hour%%s %%d minute%%s"
    pl = {True: "s", False: ""}
    date = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    return date.strftime(fmt) % (date.day, date.hour, pl[date.hour != 1], date.minute, pl[date.minute != 1])
