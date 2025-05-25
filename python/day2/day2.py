# myList = ['ahmed', 2, 3, 4, 5, 6, 'ali', 8, 9, [1, 2, 3]]
# print(myList)
# print(myList[0])
# print(11 in myList)
# myTuble = ('ahmed', 2, 3, 4, 5, 6, 'ali', 8, 9, [1, 2, 3])
# mySet = {'ahmed', 2, 3, 4, 5, 6, 'ali', 8, 9, [1, 2, 3]}
# # looping
# for i in range(1, len(myList) +1 ):
#     print(f'index is {i} and value is {myList[i -1]}')

# Hashble data type       unhashble data type

# for i in mySet:
#     print(i)

# while Loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

####################################################
# functions
# def sayHello(age="24",name='unknown'):
#     print(f'hello {name} welcome to python your age is {age}')

# sayHello(20)

# country = 'egypt'

# if country == 'egypt': print('welcome to egypt')
# elif country == 'KSA':
#     print('welcome to Saudi Arabia')
# elif country == 'england':
#     print('welcome to England')
# else:
#     print('welcome to world')

# print('welcome to egypt') if country == 'egypt' else print('welcome to world')
# print('omar','aya','abdo')

# def sayHello(*args, **kwargs):
#     print(f'hello {args}')
#
#
# sayHello('omar', 'aya', 'abdo')


# def sayHello(**kwargs):
#     """
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     pass
# if 10 == 10:
#     pass
# values = {'name': 'omar', 'age': 24}
# sayHello(**values)

# sayHello()

##############################################################33
# Scoping
# mayStr = 'global'
#
# def myFuncOuter():
#     global mayStr
#     mayStr = 'local'
#     print(mayStr)
#
# myFuncOuter()
# print(mayStr)

############################################################
# import file_one
# import file_two
# import modules.say
###############################################

# Error handling
# print('hello world')
# print(10/0
# print('hello world')

# def say_hello(name):
#     print(f'hello {name}')
# def say_bye(name):
#     say_hello(name)
#     print(f'bye {name}')
#
# say_bye('omar')
# try:
#     print(10/0)
# except Exception as e:
#     print(e)
# else:
#     print('else')
# finally:
#     print('finally')

#######################################################

# File System

# myFile = open('file.txt', 'w')
#
# myFile.write('hello from python \n')
# myFile.write('welcome \n')

# res = myFile.read()
# print(res)
# myFile = open('file.txt', 'r')
# res = myFile.readlines()
# print(res)
# myFile.close()
# import os
# # os.remove('file.txt')
# system = os.system('ls -la')
# print(system)

import re
# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# email = 't0Sb9@example.com'
# match = re.match(regex, email)
# if match:
#     print('valid')
# else:
#     print('invalid')
# print(match)

# def myDecorator(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper
#
# @myDecorator
# def myRunFunc():
#     print('run function')
#
# myRunFunc()
def myDecorator(func):
    def wrapper(*args, **kwargs):
        print('first')
        func(*args, **kwargs)
        print('fist')
    return wrapper
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        # print(f"Before{args}")
        # print(f"Before{kwargs}")
        res = func(self, *args, **kwargs)
        print(f"After method execution {self}, {kwargs}")
        return res
    return wrapper



# @myDecorator
# @method_decorator
# def myRunFunc(arg):
#     print('run function')
#
# myRunFunc('omar')

# abdu lra hma n
# omar