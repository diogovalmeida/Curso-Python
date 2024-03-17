print('Calculadora de IMC - Índice de Massa Corporal\n')
peso = float(input('Qual é o seu peso em kg: '))
altura = float(input('Qual é a sua altura em cm: '))

imc = peso / (altura/100)**2

if imc < 18.5:
    print('Magreza')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')