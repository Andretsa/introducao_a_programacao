'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
 a temperatura em graus Celsius.
1. C = 5 * ((F-32) / 9).'''

# solicita a entrada da temperatura em ºF
while True:
    try:
        fahrenheit = float(input("Digite a temperatura em ºF: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

# calcula a transformação de ºF em ºC (C/5 = F - 32/9)
celsius = (fahrenheit - 32) / 1.8

# imprime o resultado da transformação em ºC
print(f"O valor da temperatura de {fahrenheit} ºF em Celsius é: {celsius:.2f} ºC.")
