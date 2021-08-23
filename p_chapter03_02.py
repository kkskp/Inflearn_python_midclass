# Chapter03-02
# Special Method or Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), Class(클래스)
# 클래스 안에 정의할 수 있는 특별한(built-in) 메소드

# 클래스 예제2
# 벡터 계산 -> 클래스로 만든다면?
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class vector(object):
    def __init__(self, *args):
        '''
        Create a vector, example : v = vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector informations.'''
        return  'vector(%r, %r)' %(self._x, self._y)
    
    def __add__(self, other):
        '''Return vector summation'''
        return vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        '''Return vector scalar product'''
        return vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))

# vector instance create
v1 = vector(5,3)
v2 = vector(23,35)
v3 = vector()

# magic method print
print(vector.__init__.__doc__)
print(vector.__repr__.__doc__)
print(vector.__add__.__doc__)
print()
print()
print(v1, v2, v3)
print()
print()
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v2), bool(v3))
print()
print()

