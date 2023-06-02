'''Faça um programa que converta metros para centímetros.'''

# Solicitando uma medida ao usuário
while True:
    try:
        metros = float(input("Digite uma medida em metros: "))
        if metros < 0:
            print("A medida deve ser maior ou igual a zero.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

# Convertendo a medida de metros para centímetros
cm = metros * 100

# Imprime a resposta da conversão
print("A medida de {} metros equivale a {} cm.".format(metros, cm))
