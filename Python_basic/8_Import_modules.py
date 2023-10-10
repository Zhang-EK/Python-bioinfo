#! python3
# -*- coding: UTF-8 -*-



print('imported my_modules...')

test = 'test string'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1