'''Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.'''

#solicita dois valores ao usuário
def obter_numero(mensagem):
    while True:
        try:
            numero = input(mensagem)
            numero = numero.replace(',', '.')  # substitui vírgulas por pontos
            numero = float(numero)
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

valor_1 = obter_numero("Escreva um valor qualquer: ")
valor_2 = obter_numero("Escreva mais um valor qualquer: ")

# Valida se os valores são iguais e solicita um valor diferente
while valor_1 == valor_2:
    valor_2 = float(input("Por favor, escreva um valor diferente do primeiro digitado: "))

# Escreve qual o maior valor
if valor_1 < valor_2:
    print(f"O maior valor é: {valor_2}")
else:
    print(f"O maior valor é: {valor_1}")
