n = input('Digite Algo: ')

print('\033[1;35mA Classe de, {} é {}'.format(n, type(n)))
print('\033[1;31mesta em maiusculo? {}'.format(n.isupper()))
print('\033[1;34mesta em minusculo? {}'.format(n.islower()))
print('\033[1;36mé letra? {}'.format(n.isalpha()))
print('\033[1;33mé númerico? {}'.format(n.isnumeric()))
print('\033[1;32mé alphanumerico? {}'.format(n.isalnum()))