import time

HOUR_ANGLE = 15.00
MINUTES = 60.00
MINUTE_ANGLE = HOUR_ANGLE / MINUTES
MAX_MINTIME = 18 * MINUTES
MIN_MINTIME = 6.00 * MINUTES


def sun_angle(timing):
    """

    :param str timing:
    :rtype: float or str
    """

    hm = time.strptime(timing, "%H:%M")
    acttime = hm.tm_min + hm.tm_hour * MINUTES
    if MIN_MINTIME <= acttime <= MAX_MINTIME:
        return (acttime - MIN_MINTIME) * MINUTE_ANGLE
    return "I don't see the sun!"
