# Chapter05-01
'''
일급 함수(일급 객체)
파이썬 함수 특징
1. 런타임 초기화
2. 변수 할당 가능
3. 함수 인수 전달 가능
4. 함수 결과 반환 가능(return)
-> 자바스크립트도 동일한 특징을 가지고 있다!
'''

# 5! = 5x4x3x2x1
# 함수 객체


from functools import partial
from operator import mul
from operator import add
from functools import reduce


def factorial(n):
    '''
    factorial function
    n : int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)  # 재귀함수


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))  # 함수는 객체 취급이다.
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print()
print(factorial.__name__)
print(factorial.__code__)
print()
print()

# 변수 할당 가능
var_func = factorial
print(var_func)
print(var_func(5))
print(list(map(var_func, range(1, 11))))
print()
print()

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
# JS -> es6 에도 동일한 함수가 존재함

print('함수의 인수 전달 및 함수결과 반환')
print(list(
    map(var_func,
        filter(lambda x: x % 2, range(1, 6)))
)
)
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce

print('reduce함수 실습')
print(reduce(add, range(1, 11)))
# 이 경우에는 아래의 방식이 더 빠르지만 위의 reduce 함수를 사용해야 하는 순간이 온다...
print(sum(range(1, 11)))

print()
print()
# 익명함수(lambda)
# 가급적 주석을 작성해야 한다(권장)
# 가급적 함수를 새로 작성하는 것을 권장함
# 일반 함수 형태로 리펙토링 권장함

print('lambda함수 실습')
print(reduce(lambda x, t: x + t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인(__call__이 있으면 호출이 가능함!)

print('Callable 실습')
print(callable(str), callable(A), callable(var_func), callable(3.14))
print()
print()

# partial 사용법(중요! 많이 사용함) 인수 고정 -> 콜백 함수 사용

print('partial 사용법 실습')

print(mul(10, 10))

# 인수 고정

five = partial(mul, 5)
# 함수를 인자로 받고, 함수를 변수에 할당하여 새로운 함수가 생성됨
print('partial로 인수 고정')
print(five(10))

# 고정 추가

six = partial(five, 6)
print(six())
# print(six(10)) -> 이렇게 하면 인수 초과로 오류남
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))
