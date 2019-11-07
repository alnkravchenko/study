#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

print('Кравченко О.О. ІС-93 Лабораторна рoбота №4 Варіант 13')

iterCount = int(input('Enter number of iterations: '))

x = y = 1
result = 0

for count in range(iterCount):
    result += x / (1 + abs(y))
    y += x
    x *= 0.3

print(result)


