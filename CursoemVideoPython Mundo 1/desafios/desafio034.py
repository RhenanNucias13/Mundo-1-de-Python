salario = float(input('Digite o sálario do funcionario R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print('Você ganhou um aumento de 15%! Seu sálario era R${:.2f} e ficou R${:.2f}'.format(salario,aumento))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('Você ganhou um aumento de 10%! Seu sálario era R${:.2f} e ficou R${:.2f}'.format(salario,aumento))
