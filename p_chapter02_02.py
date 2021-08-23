# chapter02_01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 용이, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대해짐 -> 복잡도 증가
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : kim
    Date : 2021.07.28
    """

    # 클래스 변수(모든 인스턴스가 공유하고 있음) -> 중요한 개념이니 알아둘 것!
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail info : {} {}'.format(self._company,self._details.get('price')))

# self의 의미
car1 = Car('Ferrari', {'color': 'White','horsepower':400,'price':8000})
car2 = Car('Bmw', {'color': 'Black','horsepower':270,'price':5000})
car3 = Car('Audi', {'color': 'silver','horsepower':300,'price':6000})

#ID 확인
print(id(car1))
print(id(car2))
print(id(car3)) 

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__) #dict으로 접근하면 클래스 변수가 안보임!
print(car2.__dict__)

# Doctring
print(car1.__doc__)
print()

# 메소드 실행
car1.detail_info()

# 비교
print(car1.__class__)
print(id(car1.__class__),id(car2.__class__),id(car3.__class__))
# car1,2,3의 class의 id를 호출했기 때문에 부모 class인 car의 id가 출력되므로 모두 그 값이 같게 된다

'''
에러
Car.detail_info() -> self인자가 없다고 오류가 남
Car.detail_info(car1) -> car1인자를 넘겨주게 되므로 car1.detail_info()와 동일한 결과가 나옴
'''

#클래스 변수 출력의 확인(클래스 변수는 공유된다)
print()
print()
print(Car.car_count)
print(car1.car_count)
print(car2.car_count)


print()
print()
#삭제 확인
del car2
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
# 다만 동일한 이름으로 변수를 생성하는 것은 가급적이면 권장되지 않음