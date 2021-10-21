nome = input('Digite uma Frase: ').strip().lower()

primeira = nome.count('a')

segunda = nome.find('a')+1

terceira = nome.rfind('a')+1

print('Quantas vezes aparece a letra A? {}'.format(primeira))

print('Aparece pela primeira vez na posicao? {}'.format(segunda))

print('Apareceu na Ultima vez na posicao? {}'.format(terceira))