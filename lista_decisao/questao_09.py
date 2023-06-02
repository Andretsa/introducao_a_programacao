"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E"""

# solicita as duas notas parciais ao usuário, validando suas entradas
def validar_nota(mensagem):
    while True:
        nota = input(mensagem)
        nota = nota.replace(",", ".")  # Substitui vírgula por ponto
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número válido.")

nota_1 = validar_nota("Digite a primeira nota: ")
nota_2 = validar_nota("Digite a segunda nota: ")

# calcula a média das suas notas
media = (float(nota_1) + float(nota_2)) / 2

# atribui conceitos à sua nota
if 6 < media < 10:
    if 9 <= media <= 10:
        print("Seu conceito foi A.")
    elif 7.5 <= media < 9:
        print("Seu conceito foi B.")
    elif 6 <= media < 7.5:
        print("Seu conceito foi C.")
    print("Aprovado!!")
else:
    if 4 <= media < 6:
        print("Seu conceito foi D.")
    elif 0 <= media < 4:
        print("Seu conceito foi E.")
    print("Reprovado")

print("Suas notas foram : {}, {}; e sua média {}.".format(nota_1, nota_2, media))
