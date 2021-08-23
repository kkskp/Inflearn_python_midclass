# chapter04-03
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque])
# 플랫(Flat : 한 가지의 자료형만 담을 수 있음[str, bytes, bytearray array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블
# key에 Value를 저장하는 구조
# 파이썬의 dict은 해쉬 테이블의 예시
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1)) # 해쉬값을 가질 수 있는 것은 불변형
# print(hash(t2)) 리스트가 입력된 경우에는 오류가 발생함

# Dict SetDefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의사항(이렇게 하면 안됨!)
new_dict3 = {k : v for k, v in source}
print(new_dict3)
