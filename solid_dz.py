"""Task1"""
"""O"""

# from abc import ABC, abstractmethod
#
#
# class SpeedCalculation(ABC):
#     @abstractmethod
#     def calculate_allowed_speed(self, vehicle):
#         pass
#
# class SpeedCalculationCar(SpeedCalculation):
#     def calculate_allowed_speed(self, vehicle):
#         return vehicle.get_max_speed() * 0.8
#
#
# class SpeedCalculationBus(SpeedCalculation):
#
#     def calculate_allowed_speed(self, vehicle):
#         return vehicle.get_max_speed() * 0.6
#
#
# class Vehicle:
#     def __init__(self, max_speed: int, type: str):
#         self.max_speed = max_speed
#         self.type = type
#
#     def get_max_speed(self):
#         return self.max_speed
#
#     def get_type(self):
#         return self.type
#
#
# car = Vehicle(20, "car")
# calculate = SpeedCalculationCar()
# print(calculate.calculate_allowed_speed(car))

"""Task2"""
"""S"""
# Сделала реализацию без словаря или листов, через наследование класса Employee, не поняла, как реализовать
# через словарь или лист, по идее словарь или лист - это условная база данный получается или нет?

# from datetime import date
#
#
# class Employee:
#     def __init__(self, name: str, surname: str, dob: date):
#         self.name = name
#         self.dob = dob
#         self.surname = surname
#
#     def get_emp_info(self):
#         return f"name - {self.name}, surname - {self.surname}, dob - {self.dob}\n"
#
#
# class Account(Employee):
#     def __init__(self, name: str, surname: str, dob: date, base_salary: int):
#         super().__init__(name, surname, dob)
#         self.base_salary = base_salary
#
#     def info_base_salary(self):
#         return self.base_salary
#
#     def calculate_net_salary(self, procent=13):
#         nalog = self.base_salary * procent / 100
#         itog_salary = self.base_salary - nalog
#         return itog_salary
#
#
# employee_one = Account("Иван", "Иванов", date(1991, 5, 21), 2345)
# print(employee_one.calculate_net_salary())


"""Task3"""
"""I"""
# Данную задачу решала по примеру из класса

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape_area(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Shape_volume(ABC):
#     @abstractmethod
#     def volume(self):
#         pass
#
#
# class Circle(Shape_area):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 2 * math.pi * self.radius
#
#
# class Cube(Shape_area, Shape_volume):
#     def __init__(self, edge):
#         self.edge = edge
#
#     def area(self):
#         return 6 * self.edge * self.edge
#
#     def volume(self):
#         return self.edge * self.edge * self.edge


"""Task4"""
"""L"""
# Только такой вариант исправить данный код понимаю... не знаю, подойдет ли такой вариант...

# from abc import ABC, abstractmethod
#
# class Figure(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Figure):
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Square(Figure):
#     def __init__(self, side: int):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# square = Square(5)
# rectangle = Rectangle(5, 4)
# print(square.area())
# print(rectangle.area())