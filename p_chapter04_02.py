# chapter04-02
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형을 담을 수 있음[list, tuple, collections.deque])
# 플랫(Flat : 한 가지의 자료형만 담을 수 있음[str, bytes, bytearray array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# Tuple advanced
# Unpacking

# b, a = a, b -> unpacking의 예제로 볼 수 있다

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*divmod(100, 9))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m)) # 가변형의 경우 id가 자기자신의 id에 재할당 될 수 있음 -> 자기 자신에게 재할당 해야할 때 조금 더 유리함

print()
print()

# sort vs sorted
# reverse, key = len, key = srt.lower, key = func....

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted -',sorted(f_list))
print('sorted reverse -',sorted(f_list, reverse=True))
print('sorted len -',sorted(f_list, key=len))
print('sorted func -',sorted(f_list, key=lambda x:x[-1]))
print('sorted reverse and func -',sorted(f_list, key=lambda x:x[-1], reverse=True))
print(f_list)

# sort : 정렬 후 객체를 직접 변경
# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x:x[-1]), f_list)
print(f_list)
# List vs Array 적합한 사용법은?
# 리스트 기반 : 융통성(다양한 자료형 입력가능), 범용적 사용, 적당한 속도
# Array 기반 : 숫자 데이터를 사용시, 빠른 속도, 리스트와 호환되는 함수가 많음
 


