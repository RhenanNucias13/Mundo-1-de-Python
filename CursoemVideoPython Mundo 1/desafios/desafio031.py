distancia = float(input('Quantos Km vai ter sua viagem?: '))
print('Sua viagem vai ser de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
    print('Então a passagem vai ser no preço de R${}'.format(preço))
else:
    preço = distancia * 0.45
    print('Então a passagem vai ser no preço de R${}'.format(preço))