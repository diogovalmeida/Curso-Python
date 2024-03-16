# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita string, int's, float, boolean...

aluno = {'Nome': 'Ana', 'Idade': 16, 'Nota_Final': 'A', 'Aprovação': True}

print(aluno['Idade'])

aluno['Nome'] = 'José'
print(aluno)

print(aluno.get('Endereço')) # Não gera falha, mas sim "None" caso não exista

aluno.update({'Nome': 'António', 'Nota_Final': 'B'})
print(aluno)

aluno.update({'Endereço': 'Rua A'})
print(aluno)

del aluno['Idade']
print(aluno)