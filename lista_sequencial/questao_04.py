'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

#solicita a entrada do valor por hora de trabalho ao usuário
while True:
    try:
        # solicita a entrada do valor por hora de trabalho ao usuário
        valor_hora = float(input("Quanto você ganha por hora? "))

        # verifica se o valor é negativo
        if valor_hora < 0:
            print("O valor por hora não pode ser negativo. Tente novamente.")
            continue

        # solicita a entrada da quantidade de horas trabalhadas por mês
        horas_mes = float(input("Quantas horas você trabalha por mês? "))

        # verifica se o valor é negativo
        if horas_mes < 0:
            print("O número de horas não pode ser negativo. Tente novamente.")
            continue

        # calcula o total do seu salário mensal
        salario = valor_hora * horas_mes

        # imprime o total do seu salário mensal
        print(f"Total do seu salário neste mês é: R$ {salario:.2f}.")
        break
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer apenas números. Tente novamente.")
