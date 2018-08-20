import string


def to_encrypt(text, delta):
    """

    :param str text:
    :param int delta:
    :rtype: str
    """
    table = string.maketrans(string.lowercase,string.lowercase[delta:] + string.lowercase[0:delta])
    return text.translate(table)
