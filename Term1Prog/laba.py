#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

print('Кравченко О.О. ІС-93 Лабораторна рoбота №1 Варіант 13')

first_el = float(input('Enter first element of progression: ')) # Asking user for entering the first element of arithmetic progression 
differ = float(input('Enter difference: ')) # Asking user for entering the difference of arithmetic progression
number_el = int(input('Enter number of element of progression: ')) # Asking user for entering the number of element of arithmetic progression

if number_el == 1: # If number of element is 1, we shouldn't do anything with first_el
    next_el = first_el
else: 
    for i in range(number_el-1): # Use formula for element of arithmetic progression
        next_el = first_el + differ
        first_el = next_el

print(str(number_el) + ' number of arithmetic progression is ' + str(next_el)) # Output
