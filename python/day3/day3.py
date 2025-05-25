# class Human:
#     pass
#
# obj = Human()
# if isinstance(obj, Human):
#     print("yes")
# print(obj)
# mystr = "hello"
# print(isinstance(mystr, str))
from itertools import count

from typing_extensions import overload


##############################################

# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# obj = Human('AHMED',23)
# print(obj.name

# print(obj.age)

#################################################

# class Human:
#     count = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Human.count += 1
#
#
# obj = Human('AHMED',23)
# obj2 = Human('Mohamed',23)

##############################################
#
# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def welcome(self,city):
#         print(f"welcome {self.name} your age is {self.age} and your city is {city}")
#
# obj = Human('AHMED',23)
# obj.welcome('cairo')

###############################################
# class Human:
#     leg = 2
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def welcome(self,city):
#         print(f"welcome {self.name} your age is {self.age} and your city is {city}")
#
#     # @classmethod
#     # def calss_method(cls):
#     #     print(cls.leg)
#     #     print('Hello From Class Method')
#     # @classmethod
#     def calss_method(cls,obj1,obj2):
#         if isinstance(obj1, Human) and isinstance(obj2, Human):
#             name = obj1.name + obj2.name
#             age = obj1.age + obj2.age
#             return Human(name, age)
#
#
#
#
#
# obj = Human('AHMED',23)
# obj.leg = 3
# # print(obj.leg)
# # obj.calss_method()
#
# obj2 = Human('Mohamed',23)
# obj3 = Human('Ali',23)
# obj3.calss_method(obj2,obj3)
#
#####################################################33333

# class Human:
#     leg = 2
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def static_method():
#         print('Hello From Static Method')
#
#
# obj = Human('AHMED',23)
# obj.static_method()
# Human.static_method()

#####################################################33333

# class Human:
#
#     def __init__(self):
#         print('Hello From Class Human')
#
#
# class Person(Human):
#     def __init__(self):
#         # super(Person, self).__init__()
#         super().__init__()
#         print('Hello From Class Person')
#
#
# obj = Person()
# print(isinstance(obj, Human))

############################################
#
# class Human:
#
#     def __init__(self,name):
#         self.name = name
#
#     def welcome(self):
#         print('Hello From welcome method')
#
#
# class Person(Human):
#     def __init__(self,name):
#         super().__init__(name)
#         print('Hello From Class Person')
#
#
#     def welcome(self,flag = False):
#         if flag:
#             super().welcome()
#         print('Hello From Class Person welcome method')
#
#
# obj = Person('Ali')
# print(isinstance(obj, Human))
#######################################################


# class Human:
#
#     def __init__(self):
#         print('Hello From Class Human')
#
#     def welcome_person(self):
#         print('Hello From Class Human welcome method')
#
# class Person():
#     def __init__(self):
#         print('Hello From Class Person')
#
#     def welcome_person(self):
#         print('Hello From Class Person welcome method')
#
# class Student(Human,Person):
#     def __init__(self):
#         super().__init__()
#         Person.__init__(self)
#         super().welcome_person()
#         print('Hello From Class Student')
#     def welcome_person(self):
#         super().welcome_person()
#         Person.welcome_person(self)
#
# obj = Student()
# obj.welcome_person()

######################################################


# class Human:
#
#     def __init__(self):
#         print('Hello From Class Human')
#
#     def welcome_person(self, name : str):
#         print('Hello From Class Human welcome method')
#
# class Person(Human):
#     def __init__(self):
#         print('Hello From Class Person')
#
#     @overload
#     def welcome_person(self, name : int):
#         print('Hello From Class Person welcome method')


#######################################################
#
# class Human:
#
#     def __init__(self, age):
#         # __name = 'Ahmed'
#         print('Hello From Class Human')
#
#         self._name = 'Ahmed'
#         self.__age = age
#
#
# obj = Human(23)
# # print(obj.__age)
# print(obj._Human__age)

#######################################################

# from abc import ABC, abstractmethod
#
# class Human(ABC):
#     @abstractmethod
#     def welcome(self):
#         pass
#
#
# class Person(Human):
#
#     def welcome(self):
#         print('Hello From Class Person')
#
#
# obj = Person()

#################################################

class Human:
    @property
    def say_hello(self):
        print('Hello From Class Human')


obj = Human()
obj.say_hello()