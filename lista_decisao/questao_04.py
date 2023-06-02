'''Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.'''

# Solicita as notas da 1a. e 2a. avaliações de um aluno
def obter_numero(mensagem):
    while True:
        try:
            numero = input(mensagem)
            numero = numero.replace(',', '.')  # substitui vírgulas por pontos
            numero = float(numero)
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

nota_1 = obter_numero("Digite a sua 1ª nota: ")
nota_2 = obter_numero("Digite a sua 2ª nota: ")

# Calcula a média aritmética simples
media = (nota_1 + nota_2) / 2

'''Imprime se o aluno foi ou não aprovado e sua media 
(considerando que nota igual ou maior que 6 o aluno é aprovado)'''
if media >= 6:
    print(f"Sua média foi {media:.1f}. Você foi aprovado!!")
else:
    print(f"Sua média foi {media:.1f}. Você não foi aprovado!!")
