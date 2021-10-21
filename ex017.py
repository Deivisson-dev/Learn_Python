import math

co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente? '))
h = math.hypot(co, ca)
print('A Hipotenusa de {} e {}, é igual a : {:.2f}'.format(co,ca, h))