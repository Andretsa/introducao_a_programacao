'''Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até
#agora.'''

#estudando a biblioteca re(Operações com expressões regulares), tentei fazer esta versao
import re

# Define uma classe para o usuário
class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

# Cria uma lista vazia para armazenar os usuários cadastrados
usuarios = []

# Função para validar a idade
def validar_idade(idade):
    try:
        idade = int(idade)
        if idade <= 0:
            return False
        return True
    except ValueError:
        return False

# Função para validar o nome
def validar_nome(nome):
    return bool(re.match("^[a-zA-Z]+ [a-zA-Z]+$", nome))

# Função para validar o email
def validar_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email)) and (email.endswith(".com") or email.endswith(".com.br"))

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    while True:
        nome = input("Digite o nome completo do usuário: ")
        if validar_nome(nome):
            break
        else:
            print("Nome inválido. Digite o nome completo com nome e sobrenome separados por um espaço.")
    while True:
        idade = input("Digite a idade do usuário: ")
        if validar_idade(idade):
            break
        else:
            print("Idade inválida. Digite apenas números inteiros positivos.")
    while True:
        email = input("Digite o email do usuário: ")
        if validar_email(email):
            break
        else:
            print(
                "Email inválido. Digite um email válido com '.com' ou '.com.br' no final.")

    # Cria um novo objeto de usuário
    usuario = Usuario(nome, idade, email)

    # Adiciona o usuário à lista de usuários
    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")

# Função para exibir os usuários cadastrados
def exibir_usuarios():
    if len(usuarios) == 0:
        print("Não há usuários cadastrados.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(
                f"Nome: {usuario.nome}, Idade: {usuario.idade}, Email: {usuario.email}")
            
# Menu principal
while True:
    print("\n====== CADASTRO DE USUÁRIOS ======")
    print("1 - Cadastrar usuário")
    print("2 - Exibir usuários cadastrados")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_usuario()
        resposta = input("Deseja cadastrar outro usuário? (S/N): ")
        if resposta.upper() != "S":
            break
    elif opcao == "2":
        exibir_usuarios()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")

print("Programa encerrado.")
