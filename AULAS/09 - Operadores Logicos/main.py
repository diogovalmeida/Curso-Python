renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento reprovado')

if renda_acima_5mil or nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento reprovado')    

# Multiplos Operadores

valor = 20

'''
if valor >= 20 and valor < 40:
    print('Produto foi aceite')
else:
    print('Produto não aceite')
'''

if 20 <= valor < 40:
    print('Produto foi aceite')
else:
    print('Produto não aceite')