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

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)


# self의 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': 300, 'price': 6000})

print(car1)
print()
print(car2)
print()
print(car3)
print()

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)
print(Car.__doc__)