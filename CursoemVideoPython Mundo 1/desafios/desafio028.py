import random
computador = random.randint (0, 5) #faz o computador "PENSAR"
print('Pensei em um numero entre 0 e 5, tente adivinhar!')
jogador = int(input('Em que numero eu pensei? ')) #o jogador tenta adivinhar
if jogador == computador:
    print('PARABENS! você acertou!')
else:
    print('ERROU! eu pensei no numero {} e nao no {}'.format(computador,jogador))