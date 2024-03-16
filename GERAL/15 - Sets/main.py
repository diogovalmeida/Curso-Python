# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # O "|" significa Union e retira os valores repetidos
print(num1 - num2) # O "-" significa Diferença e retira do num1 o que está no num2
print(num1 ^ num2) # O "^" significa Diferença Simétrica retira todos os duplicados das duas listas
print(num1 & num2) # O "&" significa And e mostra o que está duplicado em ambas as listas

print(len(num1)) # O tamanho do set

###

lista1 = set([1, 2, 3, 5, 6]) # Podemos transformar em set desta forma 
#print(type(lista1))
s1 = {1, 2, 3, 5, 6} # Também dá para fazer um set desta forma 
print(type(s1))
s1.add(7)
s1.update({8, 9, 10}) # Posso adicionar vários no set
s1.remove(1) # Gera um erro se o nº não existir no set
s1.discard(90) # Não gera um erro se o nº não existir no set
print(s1)

###
# Sets com Strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) 
set4 = set1.difference(set3)
set4 = set1.intersection(set2) # O que tem em ambos (duplicado em ambas os sets)
set4 = set1.symmetric_difference(set3)

print(set4)