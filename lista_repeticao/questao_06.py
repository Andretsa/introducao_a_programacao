"""Seja criativo ao desenvolver este programa.
a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista"""

# lista de convidados
convidados = ["Brad Pitt", "Anjelina Jolie",
              "Faustão", "Jô Soares", "Humberto Gessinger"]

# exibe o convite para cada convidado da lista
for i in convidados:
    convite = ("""
              Olá, {}. Seria um enorme prazer contar com a sua presença em nosso jantar, 
              que acontecerá no dia 03/06, em nossa residência.
              Por favor confirmar a sua presença!!""").format(i.upper())
    print(convite)

# convidado desistente
convidado_desistente = ["Jô Soares"]
print(f"\nInfelizmente, {convidado_desistente[0]} não poderá comparecer.")

# substituindo o convidado desistente por um novo convidado
convidados[convidados.index("Jô Soares")] = "Serginho Groisman"

# exibe um novo convite pra lista atualizada de convidados
for i in convidados:
    convite = ("""
               Olá, {}. Seria um enorme prazer contar com a sua presença em nosso jantar, 
               que acontecerá no dia 03/06, em nossa residência. 
               Por favor confirmar sua presença!!""").format(i.upper())
    print(convite)
