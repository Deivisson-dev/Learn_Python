peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O IMC dessa pessoa é: {:.1f}'.format(imc))
    print('\033[1;31mAbaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print('O IMC dessa pessoa é: {:.1f}'.format(imc))
    print('\033[1;31mPeso ideal')
elif imc >= 25 and imc <= 30:
    print('O IMC dessa pessoa é: {:.1f}'.format(imc))
    print('\033[1;31mSobrepeso')
elif imc >= 30 and imc <= 40:
    print('O IMC dessa pessoa é: {:.1f}'.format(imc))
    print('\033[1;31mObesidade')
elif imc > 40:
    print('O IMC dessa pessoa é: {:.1f}'.format(imc))
    print('\033[1;31mObesidade Mórbida')