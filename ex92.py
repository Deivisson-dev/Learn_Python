from datetime import date
atual = date.today().year
dados = dict()
while True:
    dados["nome"] = str(input('Nome: '))
    dados["idade"] = atual - int(input("Ano de Nascimento: "))
    dados["ctps"] = int(input('Carteira de Trabalho (0 Não tem): '))
    if dados["ctps"] == 0:
        break
    dados["contratacao"] = int(input('Ano de Contratação: '))
    dados["salario"] = float(input('Salario: '))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - atual)
    break

print('-'*35)
if dados["ctps"] == 0:
    print(f'nome tem o valor {dados["nome"]}')
    print(f'idade tem o valor {dados["idade"]}')
    print(f'ctps tem o valor {dados["ctps"]}')
else:
    print(f'nome tem o valor {dados["nome"]}')
    print(f'idade tem o valor {dados["idade"]}')
    print(f'ctps tem o valor {dados["ctps"]}')
    print(f'contratação tem o valor {dados["contratacao"]}')
    print(f'Salario tem o valor {dados["salario"]}R$')
    print(f'Aposentadoria tem o Valor {dados["aposentadoria"]}')
