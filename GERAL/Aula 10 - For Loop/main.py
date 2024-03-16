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