expres = str(input('Digite sua expressão: '))
pilha = []
for simb in expres:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão esta inválida!')