# -*- coding: utf-8 -*-
"""
Matrix Multiplication
Renato Rocha
Alvaro Justen
"""

def multiply(a, b):
    """Multiplies matrixes a and b"""
    columns_of_a = len(a[0])
    lines_of_b = len(b)
    if columns_of_a != lines_of_b:
        # Check matrix dimensions
        print "Incompatible sizes!"
    else:
        lines_of_a = len(a)
        columns_of_b = len(b[0])
        #C = []
        #for i in range (lines_of_a):
        #    C.append(columns_of_b * [0])
        c = [columns_of_b * [0] for i in range(lines_of_a)]
        for i in range(lines_of_a):
            for j in range(columns_of_b):
                for k in range(lines_of_b):
                    c[i][j] += a[i][k] * b[k][j]
        return c

matrix_1 = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
matrix_2 = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
matrix_3 = mult(matrix_1, matrix_2)
print matrix_3