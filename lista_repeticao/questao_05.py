'''Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.'''

amigos = ["Camila", "Fernanda", "Lidiane"]

#percorre todo o tamanho da lista e acessa um de cada vez
for amigo in amigos:
    saudacao = f"Olá, como vai você, {amigo}?"
    print(saudacao)
