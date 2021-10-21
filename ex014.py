s = float(input('Informe o Salário do Fúncionario: R$'))
novo = s + (s * 15 / 100)

print('O Funcionario que Ganhava {}R$, com o aumento ganha {:.2f}R$'.format(s, novo))