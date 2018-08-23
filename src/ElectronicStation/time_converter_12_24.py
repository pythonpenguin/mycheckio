import datetime


def time_converter(time):
    """

    :param str time:
    :rtype: str
    """
    afternoon = datetime.timedelta(hours=12)
    if 'a' in time:
        ts = datetime.datetime.strptime(time, "%H:%M a.m.")
        if ts.hour == 12 and ts.minute == 00:
            ts = ts + afternoon
    else:
        ts = datetime.datetime.strptime(time, "%H:%M p.m.")
        if ts.hour < 12:
            ts = ts + afternoon
    return ts.strftime("%H:%M")
