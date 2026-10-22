l = float(input('Qual é a Largura da sua parede? '))
a = float(input('E qual é a Altura? '))
area = l * a
t = area / 2
print('A sua parede tem a DIMENSÃO de {}x{} e sua area e de {}m'.format(l,a,area))
print('e para pinta-la sera necessario {:.2f}l de TINTA'.format(t))