# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar objetos (instances)
    # Objetos são partes dentro de uma classe (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ===
    # Class: Frutas
    # Objects: Abacate, Banana...

class Funcionarios: # Na Class a primeira palavra tem de ser obrigatoriamente maiscula
    nome = 'Diogo'
    apelido = 'Almeida'
    data_nascimento = '01/01/2000'

utilizador1 = Funcionarios()
print(utilizador1.nome)
print(utilizador1.apelido)
print(utilizador1.data_nascimento)

###

# Criar a class
class Funcionarios2:
    pass

# Criar o objeto
utilizador1 = Funcionarios2()
utilizador2 = Funcionarios2()

# Criar os parametros do utilizador 1
utilizador1.nome = 'José'
utilizador1.sobrenome = 'Helton'
utilizador1.data_nascimento = '01/02/2000'

# Criar os parametros do utilizador 2
utilizador2.nome = 'António'
utilizador2.sobrenome = 'Maria'
utilizador2.data_nascimento = '03/03/2000'

# Print (mostrar no ecrã)
print(utilizador1.nome)
print(utilizador2.nome)