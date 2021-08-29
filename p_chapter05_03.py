# Chapter05-03
"""
일급 함수(일급 객체)
클로저 기초
외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능
"""

# Closure 사용
def closure_ex1():
    # Free variable(자유변수)
    # 클로저 영역
    series = []
    def averager(v):
        nonlocal series # 이 경우 있어도 없어도 상관 없음
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(avg_closure1.__closure__[0].cell_contents)

# 잘못된 클로저 사용
'''
def closure_ex2():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

print()
print()

avg_closure2 = closure_ex2()
'''
# print(avg_closure2(10)) -> 변수 참조범위 오류가 발생한다.

def closure_ex3():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # 이 경우 반드시 있어야 함
        cnt += 1
        total += v
        return total / cnt
    return averager

print()
print()

avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))
