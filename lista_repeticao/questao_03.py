'''Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
pessoa acessando cada elemento da lista um de cada vez.'''

amigos = []
print("Crie a sua lista de amigos")

num = input("Informe a quantidade de amigos: ")

while not num.isdigit():
    print("Entrada inválida. Por favor, informe um número inteiro.")
    num = input("Informe a quantidade de amigos: ")

num = int(num)

for a in range(0, num):
    amigo = input(f"Qual o nome do seu {a + 1}º amigo: ")
    while not amigo.isalpha():
        print("Nome inválido. Por favor, informe apenas um nome.")
        amigo = input(f"Qual o nome do seu {a + 1}º amigo: ")
    amigos.append(amigo)

# percorre todo o tamanho da lista e exibe um de cada vez
print("Minha lista de amigos é: ")
for amigo in amigos:
    print(amigo)
