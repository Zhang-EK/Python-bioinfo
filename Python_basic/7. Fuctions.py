#! python3
# -*- coding: UTF-8 -*-

##########
# def hello_func():
#     print('hello function!')
# hello_func()        # 通过改变func可以批量更改, keep dry
##########
# def hello_func():
#     return('hello function!')
# print(hello_func().upper())         # 关注于输出的结果，可以在输出的结果之上根据其类型继续用功能处理
##########
# def hello_func(greeting):
#     return '{} function!'.format(greeting)
# print(hello_func('hi'))
#########
# def hello_func(greeting, name='you'):
#     return('{}, {}').format(greeting, name)
# print(hello_func('hi', 'mike'))            # 有指定默认用指定，也可以在print里面改
#########
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['math', 'art']
# info = {'name': 'mike', 'age': 22}
# student_info(*courses, **info)     # args，kwargs是约定熟成的两种变量分类，args值得是位置参数，kwargs指的是关键字参数
#########
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2001))
print(days_in_month(2020, 4))