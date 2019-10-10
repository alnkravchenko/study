#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import math

print('Кравченко О.О. ІС-93 Лабораторна рoбота №2 Варіант 13')

koord1 = float(input('Enter first coordinate: ')) # It's x
koord2 = float(input('Enter second coordinate: ')) # It's y

flag1 = False # Flag for square
flag2 = False # Flag for circle

if ((koord1 > -1 and koord1 < 1) or koord1 == -1 or koord1 == 1): # Conditions for circle x^2 + y^2 = 4
    if (math.pow(koord1, 2) + math.pow(koord2, 2) <= 4.0):
        flag2 = True
elif ((koord1 > 1 and koord1 < 3) or koord1 == 3 or koord1 == 1): # Conditions for square |x| + |y| = 2
    if (abs(koord1) + abs(koord2) <= 2.0):
        flag1 = True

if (flag1 or flag2): 
    print('x,y belong to the area')
else:
    print('x,y don\'t belong to the area')

