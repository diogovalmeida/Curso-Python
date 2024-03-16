# Mexer em Strings & Numeros com Input
'''
nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade: ')
idade = str(idade)
cidade = input('Onde moras: ')

print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora na cidade de ' + cidade + '.')
'''

# Calculando a idade com o Input
ano_nascimento = input('Em que ano nasceste? ')
print(type(ano_nascimento))
idade = 2023 - int(ano_nascimento)
print(idade)
