'''Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'''

# Leitura e validação da quantidade atual em estoque
while True:
    quantidade_atual = input("Digite a quantidade atual em estoque: ")
    if quantidade_atual.isdigit():
        quantidade_atual = int(quantidade_atual)
        break
    else:
        print("Quantidade atual em estoque inválida. Por favor, digite um número inteiro.")

# Leitura e validação da quantidade máxima em estoque
while True:
    quantidade_maxima = input("Digite a quantidade máxima em estoque: ")
    if quantidade_maxima.isdigit():
        quantidade_maxima = int(quantidade_maxima)
        break
    else:
        print("Quantidade máxima em estoque inválida. Por favor, digite um número inteiro.")

# Leitura e validação da quantidade mínima em estoque
while True:
    quantidade_minima = input("Digite a quantidade mínima em estoque: ")
    if quantidade_minima.isdigit():
        quantidade_minima = int(quantidade_minima)
        break
    else:
        print("Quantidade mínima em estoque inválida. Por favor, digite um número inteiro.")

# Calcula e escreve a quantidade média
media = (quantidade_maxima + quantidade_minima) / 2
print(f"A média do estoque é {media}.")

# Verifica se é necessário efetuar ou não a compra para reposição do estoque
if quantidade_atual >= media:
    print("Não efetuar compra.")
else:
    print("Efetuar compra")
