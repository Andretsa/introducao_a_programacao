'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo .
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.'''

# solicita a entrada dos números inteiros e do número real
num_1 = int(input("DIgite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))
num_3 = float(input("Digite um número real: "))

# calcula o produto dobro do primeiro com metade do segundo
produto = num_1 * 2 * (num_2 / 2)

# a soma do triplo do primeiro com o terceiro
soma = num_1 * 3 + num_3

# o terceiro elevado ao cubo
cubo = num_3 ** 3

# imprime os resultados calculados
print("O resultado do dobro de {} * {} / 2 é: {}.".format(
    num_1, num_2, produto))
print("O resultado do triplo de {} + {} é: {}.".format(num_1, num_3, soma))
print("O resultado do número real {} elevado ao cubo é: {:.2f}.".format(num_3, cubo))
