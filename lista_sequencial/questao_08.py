'''tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

print("Calcule seu peso ideal")
altura = input("Por favor, nos informe a sua altura: ")

# verifica se a altura contém apenas dígitos, pontos e vírgulas
while not altura.replace(',', '.').replace('.', '').isdigit():
    print("Altura inválida. Por favor, insira um valor numérico válido.")
    altura = input("Por favor, nos informe a sua altura: ")

# converte a altura para um número real
altura = float(altura.replace(',', '.'))

# calcula o peso ideal
peso_ideal = (72.7 * altura) - 58

# imprime o peso ideal
print("Seu peso ideal é: {:.2f} kg.".format(peso_ideal))
