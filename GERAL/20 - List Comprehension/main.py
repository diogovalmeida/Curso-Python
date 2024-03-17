# List Comprehension
    # Mais simples de se escrever
    # Utilizando quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for iten in itens]

produtos = ['arroz', 'feijão', 'laranja', 'banana']
produtos2 = []

for item in produtos: 
    if 'a' in item: # Se tiver a letra a vai para a lista produtos2
        produtos2.append(item)

print(produtos2)

###

produtos2 = [item for item in produtos if 'a' in item]
print(produtos2)

###

valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)

valores = [x * 10 for x in range(6)]
print(valores)