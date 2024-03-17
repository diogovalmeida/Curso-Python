# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')

###
# Ao fazer desta forma o programa continua mesmo em erro

try:    
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números.')

print('Mais código em baixo')

### Else & Finally

try:    
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números.')
else: # Else só aparece quando o Try está OK
    print('Utilizador digitou um valor correto')
    resultado = valor * 2
    print(resultado)

try:    
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números.')
finally: # Aparece em ambas as formas
    print('Finally')

print('Mais código em baixo')