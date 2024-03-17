###
# MODULES

# Utilizando from/import -> Apenas importei o somar, portanto o multi vai falhar
from funcoes import somar

somar()
#multi()

# Utilizando from/import -> Importei ambos (podemos importar o que quisermos)
from funcoes import somar, multi

somar()
multi()

# Utilizando import (todas as funções são importadas)
import funcoes 

funcoes.somar()
funcoes.multi()

###
# PACKAGE
    # Ir buscar um módulo a partir de uma pasta (package)
    # Para funcionar é necessário criar nessa pasta um ficheiro
    # com o nome "__init__.py" e deixar em branco e fazer o seguinte
    # import:

from items.cadastro import clientes

clientes()

######## PROXIMO ########
print('\n==============\n')
######## PROXIMO ########

from funcoes import find_index
#          0    1    2    3    4
lista1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(lista1, 'b')
print(var1)