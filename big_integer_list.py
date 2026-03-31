"""
Big Integer ADT - Python List Implementation (Soal 1b + Soal 2)
Digit disimpan dari least-significant ke most-significant (index 0 = LSB).
"""


class BigIntegerList:
    def __init__(self, initValue="0"):
        self._digits = []   # list of int, index 0 = digit terkecil
        self._negative = False
        self._parse(str(initValue))

    # ------------------------------------------------------------------ #
    #  Internal helpers                                                    #
    # ------------------------------------------------------------------ #

    def _parse(self, s):
        """Parse string ke Python list (LSB di index 0)."""
        s = s.strip()
        if s.startswith("-"):
            self._negative = True
            s = s[1:]
        else:
            self._negative = False

        s = s.lstrip("0") or "0"
        # simpan terbalik: index 0 = digit terkecil
        self._digits = [int(ch) for ch in reversed(s)]

    def _to_int(self):
        """Kembalikan nilai sebagai int Python."""
        val = int("".join(str(d) for d in reversed(self._digits)))
        return -val if self._negative else val

    @classmethod
    def _from_int(cls, value):
        obj = cls.__new__(cls)
        obj._digits = []
        obj._negative = False
        obj._parse(str(value))
        return obj

    # ------------------------------------------------------------------ #
    #  toString                                                            #
    # ------------------------------------------------------------------ #

    def toString(self):
        s = "".join(str(d) for d in reversed(self._digits))
        return ("-" + s) if self._negative else s

    def __repr__(self):
        return f"BigInteger({self.toString()})"

    def __str__(self):
        return self.toString()

    # ------------------------------------------------------------------ #
    #  comparable                                                          #
    # ------------------------------------------------------------------ #

    def comparable(self, other):
        """Return -1, 0, or 1 (self < other, self == other, self > other)."""
        a, b = self._to_int(), other._to_int()
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def __lt__(self, other):  return self.comparable(other) < 0
    def __le__(self, other):  return self.comparable(other) <= 0
    def __gt__(self, other):  return self.comparable(other) > 0
    def __ge__(self, other):  return self.comparable(other) >= 0
    def __eq__(self, other):  return self.comparable(other) == 0
    def __ne__(self, other):  return self.comparable(other) != 0

    # ------------------------------------------------------------------ #
    #  arithmetic                                                          #
    # ------------------------------------------------------------------ #

    def arithmetic(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {
            "+":  lambda x, y: x + y,
            "-":  lambda x, y: x - y,
            "*":  lambda x, y: x * y,
            "//": lambda x, y: x // y,
            "%":  lambda x, y: x % y,
            "**": lambda x, y: x ** y,
        }
        if op not in ops:
            raise ValueError(f"Operator aritmatika tidak dikenal: {op}")
        return BigIntegerList._from_int(ops[op](a, b))

    def __add__(self, other):      return self.arithmetic("+",  other)
    def __sub__(self, other):      return self.arithmetic("-",  other)
    def __mul__(self, other):      return self.arithmetic("*",  other)
    def __floordiv__(self, other): return self.arithmetic("//", other)
    def __mod__(self, other):      return self.arithmetic("%",  other)
    def __pow__(self, other):      return self.arithmetic("**", other)

    # ------------------------------------------------------------------ #
    #  bitwise-ops                                                         #
    # ------------------------------------------------------------------ #

    def bitwise_ops(self, op, rhsInt):
        a, b = self._to_int(), rhsInt._to_int()
        ops = {
            "|":  lambda x, y: x | y,
            "&":  lambda x, y: x & y,
            "^":  lambda x, y: x ^ y,
            "<<": lambda x, y: x << y,
            ">>": lambda x, y: x >> y,
        }
        if op not in ops:
            raise ValueError(f"Operator bitwise tidak dikenal: {op}")
        return BigIntegerList._from_int(ops[op](a, b))

    def __or__(self, other):     return self.bitwise_ops("|",  other)
    def __and__(self, other):    return self.bitwise_ops("&",  other)
    def __xor__(self, other):    return self.bitwise_ops("^",  other)
    def __lshift__(self, other): return self.bitwise_ops("<<", other)
    def __rshift__(self, other): return self.bitwise_ops(">>", other)

    # ------------------------------------------------------------------ #
    #  Soal 2 – Assignment combo operators                                 #
    # ------------------------------------------------------------------ #

    def _assign(self, result):
        """Update self in-place dari objek BigInteger lain."""
        self._digits = result._digits
        self._negative = result._negative

    def __iadd__(self, other):
        self._assign(self + other); return self

    def __isub__(self, other):
        self._assign(self - other); return self

    def __imul__(self, other):
        self._assign(self * other); return self

    def __ifloordiv__(self, other):
        self._assign(self // other); return self

    def __imod__(self, other):
        self._assign(self % other); return self

    def __ipow__(self, other):
        self._assign(self ** other); return self

    def __ilshift__(self, other):
        self._assign(self << other); return self

    def __irshift__(self, other):
        self._assign(self >> other); return self

    def __ior__(self, other):
        self._assign(self | other); return self

    def __iand__(self, other):
        self._assign(self & other); return self

    def __ixor__(self, other):
        self._assign(self ^ other); return self


# ======================================================================= #
#  Demo / test                                                             #
# ======================================================================= #

if __name__ == "__main__":
    a = BigIntegerList("45839")
    b = BigIntegerList("123")

    print("=== Big Integer Python List ===")
    print(f"a = {a}  (digits list: {a._digits})")
    print(f"b = {b}  (digits list: {b._digits})")

    print("\n-- Arithmetic --")
    print(f"a + b  = {a + b}")
    print(f"a - b  = {a - b}")
    print(f"a * b  = {a * b}")
    print(f"a // b = {a // b}")
    print(f"a % b  = {a % b}")
    print(f"a ** 2 = {a ** BigIntegerList('2')}")

    print("\n-- Bitwise --")
    print(f"a | b  = {a | b}")
    print(f"a & b  = {a & b}")
    print(f"a ^ b  = {a ^ b}")
    print(f"a << 1 = {a << BigIntegerList('1')}")
    print(f"a >> 1 = {a >> BigIntegerList('1')}")

    print("\n-- Comparable --")
    print(f"a > b  : {a > b}")
    print(f"a == b : {a == b}")

    print("\n-- Assignment Operators (Soal 2) --")
    c = BigIntegerList("1000")
    print(f"c = {c}")
    c += b; print(f"c += b  => {c}")
    c -= b; print(f"c -= b  => {c}")
    c *= BigIntegerList("2"); print(f"c *= 2  => {c}")
    c //= BigIntegerList("3"); print(f"c //= 3 => {c}")
    c **= BigIntegerList("2"); print(f"c **= 2 => {c}")
    c <<= BigIntegerList("1"); print(f"c <<= 1 => {c}")
    c >>= BigIntegerList("1"); print(f"c >>= 1 => {c}")
    c |= b;  print(f"c |= b  => {c}")
    c &= b;  print(f"c &= b  => {c}")
    c ^= b;  print(f"c ^= b  => {c}")
