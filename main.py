usuarios = {
    "admin": "12345"
}

def login():
    print("\n===== LOGIN =====")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("\nLogin realizado com sucesso!")
        return True
    else:
        print("\nUsuário ou senha incorretos.")
        return False

def cadastrar():
    print("\n===== CADASTRAR USUÁRIO =====")

    usuario = input("Novo usuário: ")

    if usuario in usuarios:
        print("Esse usuário já existe!")
        return

    senha = input("Senha: ")

    usuarios[usuario] = senha

    print("Usuário cadastrado com sucesso!")

def listar():
    print("\n===== USUÁRIOS CADASTRADOS =====")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print("-", usuario)

def remover():
    print("\n===== REMOVER USUÁRIO =====")

    usuario = input("Usuário que deseja remover: ")

    if usuario == "admin":
        print("O usuário admin não pode ser removido.")
    elif usuario in usuarios:
        del usuarios[usuario]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

if login():

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Remover usuário")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            remover()

        elif opcao == "4":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")
