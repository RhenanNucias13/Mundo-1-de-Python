velocidade = float(input('Você estava a quantos Km/h? '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Está tudo certo!')
else: print('MULTADO! sua multa é de {}'.format(multa))

