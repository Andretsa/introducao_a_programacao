'''Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
divididos por 11, produzam o resto igual a 5.'''

# cria a lista dos numeros
numeros = []

# percorre os numeros entre 1.000 e 2.000
for n in range(1000, 2001):
    # verifica quais números divididos por 11, resultam em 5
    if n % 11 == 5:
        # add esses numeros na lista
        numeros.append(n)

# exibe a lista desses numeros
print(f"Os números entre o número 1.000 e 2.000, que quando divididos por 11, resultam em 5, são:\n{numeros}")
