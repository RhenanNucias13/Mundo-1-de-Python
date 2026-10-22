a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('DIgite outro novamente: '))
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O MENOR número é {}'.format(menor))
print('O MAIOR número é {}'.format(maior))