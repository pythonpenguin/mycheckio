def all_the_same(objs):
    """

    :param list objs:
    :rtype: bool
    """
    return len(set(objs)) < 2
