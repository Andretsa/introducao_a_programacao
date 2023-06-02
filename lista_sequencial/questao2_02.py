'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área'''

import math

#funcao que calcula a area do circulo
def calcular_area_circulo():
    while True:
        try:
            # Solicita a medida do raio ao usuário
            raio_str = input("Digite o raio de um círculo: ")

            # Verifica se a entrada contém vírgula e substitui por ponto
            if ',' in raio_str:
                raio_str = raio_str.replace(',', '.')

            # Converte a string para float
            raio = float(raio_str)

            # Verifica se o raio é válido
            if raio <= 0:
                print("O raio deve ser um número positivo.")
                continue

            # Calcula a área do círculo
            area = math.pi * (raio ** 2)

            # Imprime o resultado da área do círculo
            print("A área do círculo de raio {} é: {:.2f}".format(raio, area))
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido para o raio.")

calcular_area_circulo()
