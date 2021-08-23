# chapter02_01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 용이, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대해짐 -> 복잡도 증가
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : kim
    Date : 2021.07.28
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유하고 있음) -> 중요한 개념이니 알아둘 것!
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
    
    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail info : {} {}'.format(self._company,self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_cal(self):
        return 'After Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price')*Car.price_per_raise)

    # Class Method(중요함, self가 아닌 클래스(cls)를 인자로 받음)
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please enter 1 or more')
            return
        else:
            cls.price_per_raise = per
            print('Succeed! price increased.')
    
    # staticmethod(self나 cls를 인자로 받지 않고 사용이 가능함)
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return 'OK! This car is {}'.format(inst._company)
        else:
            return 'Sorry! This car is not BMW'





# self의 의미
car1 = Car('Ferrari', {'color': 'White','horsepower':400,'price':8000})
car2 = Car('Bmw', {'color': 'Black','horsepower':270,'price':5000})

# 가격정보(직접접근)
print(car1._details.get('price'))

# 가격정보(인상 전)
print(car1.get_price())

# 가격인상(클래스 메소드 미사용, 클래스 변수를 직접 수정하여 처리)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_cal())

# 가격인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_cal())

# staticmethod의 사용 -> 상대적으로 유연하게 사용 가능(인스턴스 및 클래스로 모두 호출가능)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))