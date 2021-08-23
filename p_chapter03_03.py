# Chapter03-03
# Special Method or Magic Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), Class(클래스)
# 클래스 안에 정의할 수 있는 특별한(built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
from typing import Collection

leng1 = sqrt((pt1[0]-pt2[0]) ** 2 + (pt1[1]-pt2[1]) ** 2)
print(leng1)

# 네임드 튜플을 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

leng2 = sqrt((pt3.x-pt4.x) ** 2 + (pt3.y-pt4.y) ** 2)
print('두 점 사이의 거리는 {}입니다.'.format(leng2))

# 네임드 튜플의 선언 방법
Point1 = namedtuple('Point',['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # default is False, rename으로 class라는 예약어를 사용할 수 있음

# 출력
print(Point1,Point2,Point3,Point4)

# Dict to unpacking
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10,y=35)
p2 = Point2(20, 40)
p3 = Point3(15, y=25)
p4 = Point4(10, 20, 30, 40) # rename test
p5 = Point1(**temp_dict) # unpacking test

print(p1, p2, p3, p4) # rename으로 사용할 때 난수로 변수가 등록되는 것을 볼 수 있음
print(p4._3)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# 네임드 튜플 메소드
temp = [58, 38]

# _make 는 네임트 튜플을 만들어 준다, 새로운 객체 생성
p4 = Point3._make(temp)
print(p4)

# _field : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)
print(dir(p1))

# _asdict() : OrderedDict 반환
print(p1._asdict())

p6 = p1._make((1,1))
print(p6)

# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)

classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List comprehension
students = [classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천 -> 변수 선언을 어떻게 하면 가독성 있게 할 수 있는지? 
students2 = [classes(rank, number)
            for rank in 'A B C D'.split()
            for number in [str(n)
            for n in range(1,21)]]
print()
print()
print(students2)