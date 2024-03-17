funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

set1 = set(funcionarios)
set2 = set(turno_dia)
set3 = set(turno_noite)
set4 = set(tem_carro)

print(set4 & set3)
print(set2 & set4)
print(set1 - set4)
