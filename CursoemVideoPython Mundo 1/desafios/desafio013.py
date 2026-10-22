salario = float(input('Qual é o seu salário?:R$'))
aumento = salario + (salario*15/100)
print('PARABÉNS você ganhou um aumento de 15%!')
print('Seu salário agora é de R${:.2f}'.format(aumento))