# Map Function
    # Muito utilizado com listas
    # Aplicar uma função a um Interable, por item. (List, tuple, dic, etc...)

lista1 = [1, 2, 3, 4]

# Como já sabemos?
def multi(x):
    return x * 2

print(multi(2))

# Como funciona o Map?
lista2 = map(multi, lista1) # Multiplica por 2 todos da lista
print(list(lista2))

# Lambda
resultado = lambda x: x * 2
lista2 = map(resultado, lista1)
print(list(lista2))
# Lambda Simplificado
lista2 = map(lambda x: x * 2, lista1)
print(list(lista2))
# Lambda Simplificado (1 Linha)
print(list(map(lambda x: x * 2, lista1)))