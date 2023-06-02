'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
#desta área para o usuário.'''

#Solicite a medida do lado do quadrado ao usuário
while True:
    lado = input("Digite o valor do lado do quadrado em metros para obter a sua área: ")
    # Verifica se a entrada contém apenas dígitos, ponto ou vírgula
    if lado.replace('.', '', 1).isdigit() or lado.replace(',', '', 1).isdigit():
        # Substitui a vírgula por ponto, se presente
        lado = lado.replace(',', '.')
        # Verifica se é um número válido
        try:
            lado = float(lado)
            if lado > 0:
                break  # Valor válido, sai do loop
            else:
                print("Digite um número positivo!")
        except ValueError:
            print("Digite um número válido!")
    else:
        print("Digite apenas números!")

# Calcula a área do quadrado
area_quadrado = lado ** 2

# Imprime a área do quadrado
print("A área do quadrado de lado {} é: {} m².".format(lado, area_quadrado))
