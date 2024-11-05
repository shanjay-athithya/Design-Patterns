class MyException(Exception):
    pass

class Vector(list):
    def __init__(self, vector=None):
        self.v = []
        if vector is None:
            self.v = []7997
        else:
            for val in vector:
                if isinstance(val, int):
                    self.v.append(val)
                else:
                    raise TypeError('the given vector contains a non-integer element')
                    
    def __setitem__(self, ind, val):
        if isinstance(val, int):
            self.v[ind] = val
        else:
            raise ValueError('not an int object')

    def __add__(self, other):
        self.result = []
        self.v.sort()
        other.v.sort()
        a_len = len(self.v)
        a = 0
        b_len = len(other.v)
        b = 0
        while a < a_len or b < b_len:
            if a < a_len and (b >= b_len or self.v[a] < other.v[b]):
                self.result.append(self.v[a])
                a += 1
            elif b < b_len and (a >= a_len or self.v[a] > other.v[b]):
                self.result.append(other.v[b])
                b += 1
            elif a < a_len and b < b_len and self.v[a] == other.v[b]:
                self.result.append(self.v[a])
                a += 1
                b += 1
        return Vector(self.result)

    def __sub__(self, other):
        self.result = []
        self.v.sort()
        other.v.sort()
        a_len = len(self.v)
        a = 0
        b_len = len(other.v)
        b = 0
        while a < a_len or b < b_len:
            if a < a_len and (b >= b_len or self.v[a] < other.v[b]):
                self.result.append(self.v[a])
                a += 1
            elif b < b_len and (a >= a_len or self.v[a] > other.v[b]):
                self.result.append(other.v[b])
                b += 1
            elif a < a_len and b < b_len and self.v[a] == other.v[b]:
                a += 1
                b += 1
        return Vector(self.result)

    def getRatios(self, other):
        self.ratio = []
        if len(self.v) != len(other.v):
            raise IndexError('the lengths of both vectors are not equal')
        elif len(self.v) == 0 or len(other.v) == 0:
            raise MyException('the vectors cannot be empty')
        else:
            
            for i in range(len(self.v)):
                if other.v[i] != 0:
                    self.ratio.append(self.v[i] / other.v[i])
                else:
                    self.ratio.append(0)
        return Vector(self.ratio)
    
    def append(self, val):
        if isinstance(val, int):
            self.v.append(val)
        else:
            raise TypeError('Appended value is not an integer')

    def __str__(self):
        return str(self.v)

if __name__ == '__main__':
    v1 = Vector([1, 2, 18])
    v2 = Vector([1, 1, 9])
    r = v1 - v2
    v1[0] = 9
    try:
        v1.append(42)  # This will work
        v1.append('abc')  # This will raise a TypeError
    except TypeError as e:
        print(f"Error: {e}")

    print(v1)
    print(v1.getRatios(v2))