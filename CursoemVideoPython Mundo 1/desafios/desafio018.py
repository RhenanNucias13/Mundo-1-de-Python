import math
angulo = float(input('Qual e o ângulo?: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O SENO vai ser de {:.2f}'.format(seno))
print('O COSSENO vai ser de {:.2f}'.format(cosseno))
print('O TANGENTE vai ser de {:.2f}'.format(tangente))