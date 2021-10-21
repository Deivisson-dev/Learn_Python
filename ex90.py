dados = dict()
dados["Nome"] = str(input('Nome: '))
dados["Média"] = float(input('Média: '))
print('-'*25)
print(f'Nome é igual a {dados["Nome"]}')
print(f'Média é igual a {dados["Média"]}')
if dados["Média"] >= 7:
    print('Situação é igual a Aprovado')
elif dados["Média"] >= 5 and dados["Média"] < 7:
    print('Situação é igual a Recuperação')
else:
    print('Situação é igual a Recuperação')
