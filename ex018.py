import math

A = float(input('Qual o valor do Ângulo? '))
sen = math.sin(math.radians(A))
cos = math.cos(math.radians(A))
tan = math.tan(math.radians(A))
print('O Cosseno é {:.2f},O Seno é {:.2f}, e a Tangente é {:.2f}'.format(cos, sen, tan))