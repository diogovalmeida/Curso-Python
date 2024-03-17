def calcular_latas(rendimento, altura, largura):
    area = altura * largura
    calcular_latas = area / rendimento
    print(f'Você precisa de {calcular_latas} latas de tinta')

rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))

calcular_latas(rendimento,altura,largura)