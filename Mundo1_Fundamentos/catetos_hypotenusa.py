from math import hypot
co = float(input('Entre com o cateto oposto: '))
ca = float(input('Entre com o cateto adjacente: '))
hi = hypot(co, ca)
print('A hypotenusa vai medir {:.2f}'.format(hi))
