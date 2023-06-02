'''Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
#ordem crescente'''

# solicita dois valores ao usuário
valor_1 = input("Escreva um valor qualquer: ")
valor_2 = input("Escreva mais um valor qualquer: ")

# Substitui a vírgula por um ponto, caso exista
valor_1 = valor_1.replace(",", ".")
valor_2 = valor_2.replace(",", ".")

# converte o valor para um número inteiro, caso não consiga, converte para um número real
try:
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    tipo = "inteiro"
except ValueError:
    try:
        valor_1 = float(valor_1)
        valor_2 = float(valor_2)
        tipo = "real"
    except ValueError:
        print("O valor digitado não é um número.")
        exit()

# Valida se os valores são iguais e solicita um valor diferente
while valor_1 == valor_2:
    valor_2 = float(
        input("Por favor, escreva um valor diferente do primeiro digitado: "))

# escreve qual o maior valor
if valor_1 < valor_2:
    print(f"A ordem crescente dos valores é: {valor_1}, {valor_2}.")
else:
    print(f"A ordem crescente dos valores é: {valor_1}, {valor_2}.")
