# chapter04-01
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque])
# 플랫(Flat : 한 가지의 자료형만 담을 수 있음[str, bytes, bytearray array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급

# 지능형 리스트(comprehending list)

chars = '+_)(*&^%$#@!'
'''
code_list1 = []
for s in chars:
    code_list1.append(ord(s))

# Comprehending lists
code_list2 = [ord(char) for char in chars]
print(code_list1)
print(code_list2)

# comprehending list + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # filter함수와 map함수 그리고 lambda 함수형식을 이용한 list생성
print()
print(code_list3)
print(code_list4)
print()
print()
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()
'''
# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g)) # next로 다음 값을 반환할 수 있음
print()
print(type(array_g))
print(array_g)
print(array_g.tolist()) # array를 list로 변환하는 함수는 tolist() 함수이다.

print()
print()

# 제네레이터 예제
print( ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21) ) )

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)

print()
print()

# 리스트 사용시 주의할 점(깊은 복사와 얕은 복사의 이해)
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3 ] * 4

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1]) # -> id값이 모두 다른 것을 알 수 있음
print([id(i) for i in marks2]) # -> id값이 모두 같음을 알 수 있음