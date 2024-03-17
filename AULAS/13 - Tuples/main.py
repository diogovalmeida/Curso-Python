# As Tuples não podem ser alertadas (Immutable) - Diferente das listas
# Se os items podem ser alterados -> Lista
# Se não podem -> Tuple
# Tuple gasta menos memória que listas (se compararmos 1000 items em cada)

cores_list = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
cores_tuple = ('Amarelo', 'Verde', 'Azul', 'Vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_tuple * 2
print(duas_listas)