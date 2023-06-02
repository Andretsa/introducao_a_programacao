'''Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até
#agora.'''

print("Seja bem vindo ao cadastro de usuários!!")

# solicita a quantidade de usuários a cadastrar
num = int(input("Quantos usuários você quer cadastrar? "))

# solicita os dados do cadastro de usuário, organizando em uma lista
usuarios = []
for c in range(0, num):
    usuarios.append(input("Informe o seu nome: "))
    usuarios.append(int(input("Informe a sua idade: ")))
    usuarios.append(input("Informe seu email: "))

# exibe a lista de cadastro dos usuários
print("_" * 30)
print("Cadastro de Usuários")
print("_" * 30)

# percorre toda a lista de cadastros a cada 3 posições
for pos in range(0, len(usuarios), 3):
    print(f"Nome: {usuarios[pos]}")
    print(f"Idade: {usuarios[pos + 1]} anos")
    print(f"Email: {usuarios[pos + 2]}")
    print("_" * 30)

# exibe a lista completa
print(usuarios)
