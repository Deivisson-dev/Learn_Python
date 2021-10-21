extensos = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um número de 0 a 20: '))
while numero not in range(0,21):
    numero = int(input('Pro favor tente novamente.Digite um Número de 0 a 20: '))
print(f'Você digitou o número {extensos[numero]}')