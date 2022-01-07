# -*- coding: UTF-8 -*-

# list
courses = ['history', 'math', 'physics', 'compsci']
# print(len(courses))      # 输出了list中有多少个元素
# print(courses[2])       #第n+1个元素，从0开始，从左到右，-1是最后一个
# print(courses[0:2])      #选取范围

#########   这里要注意.后的命令其实有一个自动重新复制给变量的功能
# courses.append('art')
# print(courses)       #添加元素指令
#########
# courses.insert(0, 'art')
# print(courses)     #在指定位置插入
#########
courses_2 = ['art', 'education']
# courses.insert(0, courses_2)
# print(courses)      #这样不对，形成了向量中的向量
# courses.extend(courses_2)
# print(courses)       #extend能够解决问题，这也是extend和insert的区别
#########
# courses.remove('compsci')   
# print(courses)     # 删除制定元素
#########
# courses.pop()   #同样删掉元素，默认最后一个
# popped = courses.pop()    #这样可以看到去除了什么元素
# print(popped)
# print(courses)
###########
# courses.reverse()      #反转
# print(courses)
#########
# courses.sort()
# print(courses)      #英文按照abc排序，数字按照从小到大排序，如要反过来排，括号里加reverse=Ture
########
# sorted_courses = sorted(courses)
# print(sorted_courses)       #sorted不会自动重新赋值，所以可以不改变原始的数据
########

########
# print(courses.index('math'))     #寻找位置
# print('math' in courses)     #查找，输出T or F
########
# for item in courses:
#     print(item)        #loop循环查找，for逻辑,'item'随便叫什么都可以
#######
# for index, item in enumerate(courses, start=1):
#     print(index, item)      #输出编号和元素，起始编号可以自定义
#######
# courses_str = ', '.join(courses)     #将序列中的元素以指定的字符连接生成一个新的字符串,注意现在是字符串了，不再是list，转化成字符串
# print(courses_str)
# new_courses = courses_str.split(', ')       
# print(new_courses)            #通过制定字符再转化回去
########


# Tuples     tuples（数组）不可变，list可以，不可以mutate，不能insert等等


# Sets
# cs_courses = {'history', 'math', 'physics', 'compsci'}      #用大括号,set没有排序位置信息，但在处理找相同或者找不同的时候更有效率
# art_courses = {'history', 'math', 'art', 'design'}
# print(cs_courses.intersection(art_courses))      #找共同
# print(cs_courses.difference(art_courses))        #找不同，注意两个set在指令的先后顺序，结果不同
# print(cs_courses.union(art_courses))             #并集


# 创建空的list、tuples、sets
# empty_list = []
# empty_list = list()
# empty_tuples = ()
# empty_tuples = tuple()
# empty_sets = {}         # 这样是不对的。这创建了一个dict
# empty_sets = set()

# 总结：tuple是一个不可改变的list，set是一个没有Value的dict，list，dict和set的数据是可变的，tuple数据是不可变的
