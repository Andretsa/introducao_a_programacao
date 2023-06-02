'''Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'.'''

# solicita o número da conta do cliente, saldo, débito e crédito
# validação do número da conta do cliente
while True:
    try:
        numero_conta = int(input("Digite o número da sua conta (sem caracteres especiais): "))
        break
    except ValueError:
        print("Número da conta inválido. Por favor, digite um número inteiro.")

# Validação do saldo
while True:
    try:
        saldo = float(input("Digite o saldo atual da conta: "))
        break
    except ValueError:
        print("Saldo inválido. Por favor, digite um número real.")

# Validação do débito
while True:
    try:
        debito = float(input("Digite o valor do débito: "))
        break
    except ValueError:
        print("Débito inválido. Por favor, digite um número real.")

# Validação do crédito
while True:
    try:
        credito = float(input("Digite o valor do crédito: "))
        break
    except ValueError:
        print("Crédito inválido. Por favor, digite um número real.")

# calcula e escreve o saldo atual
saldo_atual = saldo - debito + credito
print(f"Seu saldo atual é: R$ {saldo_atual:.2f}.")

# verifica se o saldo é positivo ou negativo
if saldo_atual >= 0:
    print("Saldo Positivo!!")
else:
    print("Saldo Negativo!!")
