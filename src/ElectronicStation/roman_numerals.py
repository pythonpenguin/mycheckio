UNUS = "I"
QUINQUE = "V"
DECEM = "X"
QUINQUAGINTA = "L"
CENTUM = "C"
CINQUECENTUM = "D"
MILLE = "M"


class RomanNumbers(object):
    DIVISORE = 0
    MAX = 4000
    RV = ""
    MID_RV = None
    CHANGE_RV = None
    MAX_REP = 3

    @classmethod
    def mid_pre(cls):
        return cls.RV + cls.MID_RV

    @classmethod
    def mid(cls):
        return 5

    @classmethod
    def change(cls):
        return 10

    @classmethod
    def mid_post(cls, rep):
        """

        :param int rep:
        :return:
        """
        return cls.MID_RV + cls.RV * int(rep)

    @classmethod
    def change_pre(cls):
        return cls.RV + cls.CHANGE_RV

    @classmethod
    def rv_rep(cls, rep):
        """

        :param int rep:
        :rtype: str
        """
        return cls.RV * int(rep)

    def __init__(self, number):
        self._number = self._fix_limits(number)

    def _fix_limits(self, number):
        """

        :param int number:
        :rtype: int
        """

        if number > self.MAX or number < self.DIVISORE:
            raise ValueError("{m}<number<{M}".format(m=self.DIVISORE, M=self.MAX))
        return number

    def translate(self):
        raise NotImplemented

    def __hash__(self):
        return self.DIVISORE

    def __cmp__(self, other):
        return hash(self) == hash(other)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def translate(self):
        val = self._number / self.DIVISORE
        if val == self.mid():
            return self.MID_RV
        if val > self.mid():
            val = val - self.mid()
            if val > self.MAX_REP:
                return self.change_pre()
            return self.mid_post(val)
        if val > self.MAX_REP:
            return self.mid_pre()
        return self.rv_rep(val)


class RomanNumbersUnit(RomanNumbers):
    DIVISORE = 1
    MID_RV = QUINQUE
    CHANGE_RV = DECEM
    RV = UNUS


class RomanNumbersDecine(RomanNumbers):
    DIVISORE = 10
    MID_RV = QUINQUAGINTA
    CHANGE_RV = CENTUM
    RV = DECEM


class RomanNumbersCent(RomanNumbers):
    DIVISORE = 100
    MID_RV = CINQUECENTUM
    CHANGE_RV = MILLE
    RV = CENTUM


class RomanNumbersMill(RomanNumbers):
    DIVISORE = 1000
    MID_RV = "VS"
    CHANGE_RV = "MS"
    RV = MILLE


class ComposedNumber(object):
    _factory = {1: RomanNumbersUnit, 10: RomanNumbersDecine, 100: RomanNumbersCent, 1000: RomanNumbersMill}
    _div = [1000, 100, 10, 1]

    def __init__(self, number):
        self._number = number
        self._scomposed = []
        self._parse()

    def translate(self):
        return "".join((x.translate() for x in self._scomposed))

    def _parse(self):
        val = self._number
        for _d in self._div:
            res, val = divmod(val, _d)
            if res:
                self._scomposed.append(self._factory[_d](res * _d))


def checkio(data):
    """

    :param int data:
    :rtype: str
    """
    return ComposedNumber(data).translate()
