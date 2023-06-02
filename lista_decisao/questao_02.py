'''Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
negativo (considere o valor zero como positivo).'''

# Solicite ao usuário um valor numérico, inteiro ou real
valor = input("Digite um número qualquer: ")

# Substitui a vírgula por um ponto, caso exista
valor = valor.replace(",", ".")

# converte o valor para um número inteiro, caso não consiga, converte para um número real
try:
    valor = int(valor)
    tipo = "inteiro"
except ValueError:
    try:
        valor = float(valor)
        tipo = "real"
    except ValueError:
        print("O valor digitado não é um número.")
        exit()

# Escreve se é positivo ou negativo (considere o valor zero como positivo)
if valor >= 0:
    print("Esse número é positivo!!")
else:
    print("Esse número é negativo!!")
