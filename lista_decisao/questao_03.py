''' As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra.'''

# solicita o número de maçãs compradas ao usuário
while True:
    macas = input("Quantas maçãs foram compradas? ")
    if macas.isnumeric():
        macas = int(macas)
        break
    else:
        print("Entrada inválida. Por favor, insira um número inteiro.")

# calcula e escreve o custo total da compra
if macas < 12:
    custo = 1.30 * macas
    print(f"O custo total das maçãs compradas foi de: R$ {custo:.2f}.")
elif macas >= 12:
    custo = 1 * macas
    print(f"O custo total das maçãs compradas foi de: R$ {custo:.2f}.")
