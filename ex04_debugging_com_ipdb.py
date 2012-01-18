import ipdb
from math import sqrt


a = -2
b = 2
c = 1

delta = b ** 2 - 4 * a * c
raiz_1 = (- b + sqrt(delta)) / (2 * a)
ipdb.set_trace()
raiz_2 = (- b - sqrt(delta)) / (2 * a)
ipdb.set_trace()
print raiz_1, raiz_2
