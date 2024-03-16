'''
SUPERMERCADO
Function: 
    Maça
        - Peso
        - Cor 
        - Preço
    Banana
        - Peso
        - Cor 
        - Preço
Posso juntar tudo num module (por ex com o nome Sessão Frutas e Verduras) -> Outros exemplos, sessão de beleza... carnes, etc.. 
E posso juntar vários modules dentro de um package (por ex. Supermercado A, B, C)
Dentro desses packages posso criar uma Library (por ex. HyperMarket -> Grupo de Supermercados)
'''

# Function

def boas_vindas(): 
    print('Olá Diogo')
    print('Temos 5 computadores em estoque')

boas_vindas()


def somar_dois_numeros(numero1,numero2):
    resultado = int(numero1) + int(numero2)
    print(resultado)

numero1 = input('Diz o numero 1:')
numero2 = input('Diz o numero 2:')

somar_dois_numeros(numero1,numero2)


def welcome(nome, quantidade=6): # O nome não é Default | A quantidade está como Default (6) --- REGRA: O Default tem de estar sempre no fim.
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} computadores em estoque')

welcome('Marcos') # Podemos definir a quantidade aqui na mesma


def cliente1(nome):
    print(f'Olá {nome}')

print(cliente1('Maria')) # Aparece None porque não guarda nada na memória (não retorna, apenas faz print na função acima)

def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('Jose')) # Como temos return, ele agora ao fazer print aparece


# Vários argumentos (xargs)
def soma(*numeros): # Usar o *
    total = 0
    for num in numeros:
        total += num
    return total

x = soma(2,3,4,7)
print(x)

# Criar uma função que armazena numeros e strings (dados) -> Xargs
def agencia(**carro): # 2's ** -> Significa que pode ter vários parametros
    return carro

print(agencia(marca='Ferrari', cor='Vermelho', motor=2.2, placa='22-bx-21'))
print(agencia(marca='Porsche', cor='Verde Escuro', motor=2.0, placa='11-op-99'))
print(agencia(marca='Lamborghini', cor='Preto', motor=2.6))