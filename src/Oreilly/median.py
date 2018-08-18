def checkio(data):
    """

    :param list data:
    :rtype: int or float
    """
    index, remainder = divmod(len(data), 2)
    if remainder:
        return sorted(data)[index]
    ls = sorted(data)
    return (ls[index] + ls[index - 1]) / 2.0
