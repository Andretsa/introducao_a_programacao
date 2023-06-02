'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
graus Fahrenheit.'''

# solicita a entrada da temperatura em ºC ao usuário
while True:
    try:
        celsius = float(input("Digite a temperatura em ºC: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

# calculo da tranformação de ºC para ºF (C/5 = F - 32/9)
fahrenheit = celsius * 1.8 + 32

# imprime o resultado da transformação em ºF
print("O valor da temperatura de {}ºC em Fahrenheit é: {}ºF.". format(
    celsius, fahrenheit))
