# Chapter03-02
# Special Method or Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), Class(클래스)
# 클래스 안에 정의할 수 있는 특별한(built-in) 메소드

# 기본형
n = 10

print(n + 100)
print(n.__add__(100))
print()
print(n.__bool__(),bool(n))

print()
print()

# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def __str__(self):
        return 'Fruit Class info : {}  {}'.format(self._name,self._price)

    def __add__(self, x):
        print("Called >> __add__")
        return self._price + x._price

    def __sub__(self, x):
        print("Called >> __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("Called >> __le__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("Called >> __ge__")
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Apple', 7200)
s2 = Fruit('Banana', 3600)

print(s1)
print(s1 + s2)
print(s2 - s1)
print(s1 <= s2)
print(s1 >= s2)