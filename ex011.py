l = float(input('Digite a largura da parede: '))
h = float(input('Digie a altura da parede: '))
a = l * h
print('\033[1;31mSua parede tem a dimensão de {}x{} e a área de {}'.format(l , h , a))
tinta = a / 2
print('\033[1;31mPra pintar essa parede você vai precisar de {}l de tinta'.format(tinta))
