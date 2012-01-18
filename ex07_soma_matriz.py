# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:59:22 2012
Renato Rocha
Alvaro Justen
"""

def sum_matrix(a,b):
    """Sum matrixes a and b"""
    lines_of_a = len(a)
    columns_of_a = len(a[0])
    #C = []
    #lv = [0]
    #for i in range (sizeL):
    #    C.append(sizeC * lv)
    c = [columns_of_a * [0] for i in range(lines_of_a)]
    for line in range(lines_of_a):
        for column in range(columns_of_a):
            c[line][column] = a[line][column] + b[line][column]
    return c

matrix_1 = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
matrix_2 = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
matrix_3 = sum_matrix(matrix_1, matrix_2)
print matrix_3