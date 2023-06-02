'''Faça um programa que receba um número e que calcule e mostre a tabuada desse número.'''

#solicita o número ao usuário
print("Monte a tabuada do número que desejar!!")
tabuada = int(input("Digite o número escolhido: "))

#calcula e escreve a tabuada do número solicitado pelo usuário
print("A tabuada do número escolhido é: ")
for count in range(10):
    print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count+1)))
