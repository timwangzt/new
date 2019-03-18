
#
# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b
#
# fib = fibonacci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# def debug(func):
#     def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
#         # print('[DEBUG]: %s').format(func.__name__)
#         print('Prepare and say...')
#         return func(*args, **kwargs)
#     return wrapper  # 返回
#
# @debug
# def say(something):
#     print("hello {}!" + something)
#
# say('dfdlfj
# k')

# class myDecoratertest:
#     sex = 1;
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def print_hello(x):
#         print('hello {}'.format(x))
#
#     @classmethod
#     def print_salary(cls,salary):
#         print('Salary: {}'.format(salary))
#
#     @property
#     def get_name(self):
#         return self.name
#
#
# myDecoratertest.print_hello('Tim')
# myDecoratertest.print_salary(8888.98)
#
# my = myDecoratertest('Amber',44)
# print(my.get_name)

# class RevealAccess(object):
#     def __init__(self,interval=None, name='var'):
#         self.val = interval
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         print('Retrieving ', self.name)
#         return self.val
#
#     def __set__(self, obj, val):
#         print('Updating ', self.name)
#         self.val = val
#
# class myClass(object):
#     x = RevealAccess(10, 'var "x"')
#     y = 5

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000/admin')

browser.quit()