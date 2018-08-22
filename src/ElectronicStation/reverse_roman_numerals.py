UNUS = "I"
QUINQUE = "V"
DECEM = "X"
QUINQUAGINTA = "L"
CENTUM = "C"
CINQUECENTUM = "D"
MILLE = "M"

INTVAL = {UNUS: 1, QUINQUE: 5, DECEM: 10, QUINQUAGINTA: 50, CENTUM: 100, CINQUECENTUM: 500, MILLE: 1000}
SPECIAL = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


def reverse_roman(roman_string):
    """

    :param str roman_string:
    :rtype: int
    """
    if len(roman_string) == 1:
        return INTVAL[roman_string]
    to_process = True
    val = 0
    for x, v in enumerate(roman_string):
        if to_process:
            _sub = roman_string[x: x + 2]
            if _sub in SPECIAL:
                val += SPECIAL[_sub]
                to_process = False
            else:
                val += INTVAL[v]
        else:
            to_process = True
    return val
