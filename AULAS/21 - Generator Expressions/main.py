from sys import getsizeof

# Generator Expressions
    # Uma forma mais rápida para listas, dicionários, etc.
    # Menos memória alocada
    # Valores em bytes

numeros = [x * 10 for x in range(10000000)] # Armazena na memória
print(type(numeros))
print(getsizeof(numeros))

print('===')

numeros = (x * 10 for x in range(10000000)) # Não armazenza na memória
print(type(numeros))
print(getsizeof(numeros))

