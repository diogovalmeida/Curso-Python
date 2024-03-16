mensagem = 'adoro comida caseira'
mensagem2 = '    adoro'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('c')) # Começa com 0 a contagem (é diferente c e C) -> -1 significa que não existe
print(mensagem.replace('a', 'e'))
print(mensagem.replace('caseira', 'feita em casa'))
print(mensagem2.strip()) # remover os espaços caso ponha no inicio