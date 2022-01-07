#! python3
# -*- coding: UTF-8 -*-

# 字符与赋值
message = 'hello world'
# print(message)             # 注意'Bobby's world'会引起错误，单引号前加/可以解决，或者左右单引号改成双引号

# print(len(message))      # 字符计数
# print(message[6])           # 第n个字符，注意是从0开始的
# print(message[0:5])        #  从0开始到4结束，注意不是5

# 一些简单的功能函数
# print(message.upper())     # 一些简单的功能函数，改变大小写
# print(message.lower())      # 一些简单的功能函数，改变大小写
# print(message.count('l'))     # 一些简单的功能函数，查找字符中的元素个数
# print(message.find('hello'))    # 查找字符中的元素，输出开始出现的位置，如不存在，返回-1

#######
# message = message.replace('world','universe')
# print(message)              # 替换，重新赋值
########

#######
greeting = 'Hello'
name = 'Zhang'
# message = greeting + ' ' + name + '. Welcome'
# print(message)              # 多个语句组合，注意空格也要插入
#
# message = '{}, {}. Welcome!'.format(greeting, name)          #另一种方法，通过大括号严格限制位置
# print(message)
#######








