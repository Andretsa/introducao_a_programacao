'''Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
#menor que 10. O programa deve escrever a mensagem correspondente (maior ou
#menor) e informar o valor digitado pelo usuário.'''

# Solicita ao usuário um valor numérico, inteiro ou real
valor = input("Digite um número: ")

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

# verifica se o valor é maior ou menor que 10
if valor > 10:
    print(f"O valor digitado foi: {valor}. É maior que 10.")
elif valor < 10:
    print(f"O valor digitado foi: {valor}. É menor do que 10.")
else:
    print(f"O valor digitado foi: {valor}. É igual a 10.")
