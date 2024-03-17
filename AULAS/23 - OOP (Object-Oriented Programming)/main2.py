# Construtores (usar __init__)

class Funcionarios():

    def __init__(self, nome, sobrenome, data_nascimento): # Self é o objeto . (argumento -> nome, etc.)
        self.nome =  nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

# Criar o objeto
utilizador1 = Funcionarios('José', 'Helton', '01/02/2000')
utilizador2 = Funcionarios('António', 'Maria', '03/03/2000')
utilizador3 = Funcionarios('Diogo', 'Almeida', '10/10/2010')

# Print (mostrar no ecrã)
print(utilizador1.nome)
print(utilizador2.nome)
print(utilizador3.sobrenome)


print(utilizador1.nome + ' ' + utilizador1.sobrenome) # Funciona, mas nada de especial
### MELHORIA ###
# Depois de fazer o def nome_completo
print(utilizador1.nome_completo())
print(Funcionarios.nome_completo(utilizador2))

### 
# Usar agora ano de nascimento
print('\n=========\n')

from datetime import datetime

class Funcionarios2():

    def __init__(self, nome, sobrenome, ano_nascimento): # Self é o objeto . (argumento -> nome, etc.)
        self.nome =  nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Criar o objeto
utilizador1 = Funcionarios2('José', 'Helton', 2000)
utilizador2 = Funcionarios2('António', 'Maria', 2004)
utilizador3 = Funcionarios2('Diogo', 'Almeida', 2010)

# Print
print(Funcionarios2.nome_completo(utilizador2))
print(Funcionarios2.idade_funcionario(utilizador2))
