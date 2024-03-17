temperatura = int(input('Qual é a temperatura da carne? '))

if(temperatura < 48):
    print('Cozinhar mais um pouco')
elif(temperatura < 54):
    print('Selada')
elif(temperatura < 60):
    print('No ponto para o mal passado')
elif(temperatura < 65):
    print('Médio')
elif(temperatura < 71):
    print('No ponto para o bem passado')
else:
    print('Bem passado')
    
'''
Solução professor:

if temperatura < 48:
    print('Cozinhar mais um pouco')
elif temperatura in range(48,53):
    print('Selada')
elif temperatura in range(54,59):
    print('No ponto para o mal passado')
elif temperatura in range(60,64):
    print('Médio')
elif temperatura in range(65,70):
    print('No ponto para o bem passado')
elif temperatura >= 71:
    print('Bem passado')
'''