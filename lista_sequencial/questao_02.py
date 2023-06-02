'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área'''

#importanto biblioteca
import math

#Solicita a medida do raio ao usuário
raio = float(input("Digite o raio de um círculo: "))

#Calcula a área do círculo
area = math.pi * (raio**2)

#Imprime o resultado da área do círculo
print("A área do círculo de raio {} é: {:.2f}".format(raio, area))
