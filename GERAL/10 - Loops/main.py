# Utilizando Números
# Imprimir de 1 a 5

for numero in range(6): # Vem o 0 
    print(numero)

for numero in range(1, 6): # Desta forma não vem o 0 
    print(numero)

for numero in range(1, 20, 2): # De 2 em 2 (começando no 1)
    print(numero)


# Utilizando Strings

palavra = 'Google'

for letra in palavra:
    print(f'{letra} está dentro da palavra Google')


# Loop Nested (um loop dentro de outro)
    
for numero1 in range(1, 6):
    print('Produto ' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)


# Loop - Separando Strings
        
palavra2 = 'FANTASTICO'

for espaco in palavra2:
    print(espaco, end=' ')
    print()


# Loop - Criando retângulo
    
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()


# While Loop
    
valor = 100
dia = 1

while valor > 20:
    print(f'No dia {dia} o produto vai ser vendido a {valor}€')
    dia += 1
    valor -= 5


# Operador Ternário
    
idade = 18

'''
if idade >= 18:
    resultado = print('Voto permitido')
else:
    resultado = print('Voto não permitido')
'''

resultado = 'Voto permitido' if idade >= 18 else 'Voto não permitido'

print(resultado)


# Criar condições com o While Loop

valor2 = int(input('Digite o valor do seu produto em €: '))

while valor2 > 20:
    valor2 = (valor2 * 0.10) + valor2  # Comissão de 10% acima de 20€
    print(f'O valor final do seu produto será {valor2}€')
    break