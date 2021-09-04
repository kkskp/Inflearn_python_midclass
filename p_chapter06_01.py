# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... -> iterable
# 반복문(for문 등) 사용가능?

# 반복 가능한 이유? -> iter(x) 함수 호출
t ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in t:
    print('>', c)

# while(위의 for문에서 이런 내부로직을 통해 값을 출력함)
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
from collections import abc
from typing import Generator

# print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))
print(abc)

print()
print()

# next 패턴

class word_splitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")
    
    def __next__(self):
        print('Called __next__ in iterator')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx += 1        
        return word

    def __repr__(self):
        return 'WordSplit(%s)'%(self._text)
    
word1 = word_splitter('Do something Now')
print(word1)
print(next(word1))
print(next(word1))
print(next(word1))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가, 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사용

class word_split_generator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        
    def __repr__(self):
        return 'WordSplitGenerator(%s)'%(self._text)

    
word2 = word_split_generator('Do something Now')

word2_iter = iter(word2)
print(word2_iter, word2)
print()
print('Generator')

print(next(word2_iter))
print(next(word2_iter))
print(next(word2_iter))

print()
print()