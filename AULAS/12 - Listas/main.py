# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequência dos dados em uma variável

cidade1 = 'Lisboa'
cidade2 = 'Porto'
cidade3 = 'Faro'
#             0         1        2
cidades = ['Lisboa', 'Porto', 'Faro']

cidades.append('Portimão') # Adicionar no final da lista
cidades.remove('Faro') # Remover um da lista
cidades.insert(1, 'Castelo Branco') # Adicionar no index 1 Castelo Branco (o Porto passa para o index 2)
cidades[0] = 'Braga' # Trocar Lisboa por Braga (index 0)
cidades.pop(0) # Retirar Index 0 -> Lisboa/Braga deixam de aparecer
cidades.sort() # Ordenar em ordem alfabética
print(cidades)
print(cidades[1])

# Juntar listas / extender listas

numeros = [2,3,4,5]
letras = ['a','b','c','d']

final = numeros + letras
print(final)

numeros.extend(letras)
print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[0])
print(itens[1])
print(itens[0][1])

# Lista de Produtos

produtos = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6, 7]

item1, item2, item3, *outros, item8 = produtos

print(item1)
print(item2)
print(item3)
print(item8)
print(outros)

# Loop em listas

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(x)

# Lista de cores
'''
cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']

cor = input('Por favor, indique uma cor: ')

if cor.capitalize() in cores:
    print('Sim')
else:
    print('Não')
'''
# Juntar listas de valores e cores
    
cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
valores = [50, 80, 110, 150, 170]

var = list('comprar')
print(var)

listas = zip(cores,valores)
print(list(listas))

# Fazer listas a partir de um input

frutas_utilizador = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_utilizador.split(', ')

print(frutas_lista)