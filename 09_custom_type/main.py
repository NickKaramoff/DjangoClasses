class EvenNumber:
    def __init__(self, value=0):
        if isinstance(value, int) and value % 2 == 0:
            self.value = value
        else:
            raise TypeError('The resulting number is not even')

    def __abs__(self):
        return EvenNumber(abs(self.value))

    def __add__(self, other):
        if isinstance(other, int):
            return EvenNumber(self.value + other)
        elif isinstance(other, EvenNumber):
            return EvenNumber(self.value + other.value)
        else:
            raise TypeError

    def __bool__(self):
        return self.value != 0

    def __ceil__(self):
        return self

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, EvenNumber):
            return self.value == other.value
        else:
            raise TypeError

    def __float__(self):
        return float(self.value)

    def __floor__(self):
        return self

    def __ge__(self, other):
        if isinstance(other, int):
            return self.value >= other
        elif isinstance(other, EvenNumber):
            return self.value >= other.value
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other
        elif isinstance(other, EvenNumber):
            return self.value > other.value
        else:
            raise TypeError

    def __int__(self):
        return int(self.value)

    def __le__(self, other):
        if isinstance(other, int):
            return self.value <= other
        elif isinstance(other, EvenNumber):
            return self.value <= other.value
        else:
            raise TypeError

    def __lshift__(self, other):
        if isinstance(other, int):
            return EvenNumber(self.value << other)
        elif isinstance(other, EvenNumber):
            return EvenNumber(self.value << other.value)
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        elif isinstance(other, EvenNumber):
            return self.value < other.value
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return EvenNumber(self.value * other)
        elif isinstance(other, EvenNumber):
            return EvenNumber(self.value * other.value)
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, int):
            return self.value != other
        elif isinstance(other, EvenNumber):
            return self.value != other.value
        else:
            raise TypeError

    def __neg__(self):
        return EvenNumber(-self.value)

    def __pos__(self):
        return EvenNumber(+self.value)

    def __pow__(self, power, modulo=None):
        return EvenNumber(pow(self.value, power, modulo))

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __round__(self, n=None):
        return self

    def __rsub__(self, other):
        if isinstance(other, int):
            return EvenNumber(other - self.value)
        elif isinstance(other, EvenNumber):
            return EvenNumber(other.value - self.value)
        else:
            raise TypeError

    def __str__(self):
        return str(self.value)

    def __sub__(self, other):
        if isinstance(other, int):
            return EvenNumber(self.value - other)
        elif isinstance(other, EvenNumber):
            return EvenNumber(self.value - other.value)
        else:
            raise TypeError

    def __trunc__(self):
        return self

    def __and__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __floordiv__(self):
        pass

    def __mod__(self, other):
        pass

    def __or__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __rpow__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __xor__(self, other):
        pass


# a = EvenNumber(5) # will raise TypeError

b = EvenNumber(4)
print("b = %s\t\t— an EvenNumber declaration" % b)

c = b + 6
print("c = %s\t\t— EvenNumber plus int" % c)

# d = c + 3 # will raise TypeError
# print(d)

e = c == 10
print("e = %s\t— EvenNumber == int" % e)

f = b != c
print("f = %s\t— EvenNumber != EvenNumber" % f)

g = EvenNumber(-8)
print("g = %s\t\t— negative EvenNumber" % g)

h = abs(g)
print("h = %s\t\t— absolute of an EvenNumber" % h)

i = h << 2
print("i = %s\t\t— lshift of an EvenNumber by int" % i)

j = b ** 2
print("j = %s\t\t— EvenNumber to the power of int" % j)
