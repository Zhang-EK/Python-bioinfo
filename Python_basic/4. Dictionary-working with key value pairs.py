#! python3
# -*- coding: UTF-8 -*-

# keys and values
student = {'name': 'John', 'age': 25, 'course': ['Math', 'Compsci']}
# print(student)
# print(student['name'])      # 只输出某个key的内容
# print(student.get('phone', 'not found'))      # get也可以输出key内容，并且可以自定义没找到时输出的信息

##############
# student['phone'] = '555-5555'     # 这样可以直接插入，如果输入已经有的key那么就会更新dict中的value
# print(student)
#############
# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
# print(student)      # 批量更新
############
# del student['age']     # 删除key
# print(student)
###########
# age = student.pop('age')
# print(student)
# print(age)         # 同样的pop也可以用来删除，但是会保留删除的部分 
###########

#########
# print(len(student))    # 输出几个key
# print(student.keys())     # 输出具体key的名字
# print(student.values())     # 输出具体value
# print(student.items())       # 同时输出
#########
# for key, value in student.items():
#     print(key, value)
#########