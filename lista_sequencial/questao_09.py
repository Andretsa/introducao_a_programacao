'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
1. Para homens: (72.7*h) - 58
2. Para mulheres: (62.1*h) - 44.7'''

# funcao para converter a leitura da altura


def converter_altura(altura_str):
    # Substituir vírgulas por pontos para permitir conversão para float
    altura_str = altura_str.replace(',', '.')
    return float(altura_str)


print("Calcule seu peso ideal")

# solicita a entrada do usuario e a valida
while True:
    try:
        altura_input = input("Por favor, informe a sua altura em metros: ")
        altura = converter_altura(altura_input)

        if altura <= 0:
            print("Altura inválida! Por favor, informe um valor positivo.")
            continue
        break
    except ValueError:
        print("Altura inválida! Por favor, informe um número válido.")

while True:
    sexo = input("Informe seu sexo [M/F]: ")
    if sexo.upper() not in ['M', 'F']:
        print("Sexo inválido! Por favor, informe 'M' para masculino ou 'F' para feminino.")
    else:
        break

# calcula o peso conforme o sexo
if sexo.upper() == 'M':
    peso_homem = (72.7 * altura) - 58
    print("O peso ideal para um homem com a altura de {:.2f} metros é: {:.2f} kg.".format(
        altura, peso_homem))
else:
    peso_mulher = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com a altura de {:.2f} metros é: {:.2f} kg.".format(
        altura, peso_mulher))
