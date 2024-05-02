Armazenamento de dados
alunos = []
usuario_autenticado = False

Função para registrar um novo aluno
def cadastrar():
    global usuario_autenticado
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    escola = input("Digite sua escola: ")
    turma = input("Digite sua turma: ")
    serie = input("Digite sua série: ")
    perfil = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "escola": escola,
        "turma": turma,
        "serie": serie,
        "notas": [],
        "frequencias": [],
        "tarefas": []
    }
    alunos.append(perfil)
    usuario_autenticado = True
    print("Cadastro realizado com sucesso!")

Função para salvar os dados em um arquivo
def salvar_dados():
    with open("dados_alunos.txt", "w") as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno}\n")
    print("Dados salvos com sucesso!")

Função principal
def principal():
    while True:
        if not usuario_autenticado:
            escolha = input("Você precisa estar autenticado para acessar. Deseja fazer login (L) ou cadastrar (C)? ")
            if escolha.upper() == "L":
                # Login
                pass  # Adicione a funcionalidade de login
            elif escolha.upper() == "C":
                # Cadastrar
                cadastrar()
            else:
                print("Opção inválida. Por favor, tente novamente.")
        else:
            print("1. Perfil")
            print("2. Notas")
            print("3. Frequências")
            print("4. Tarefas")
            print("5. Calendário")
            print("6. Salvar Dados")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
Perfil
                pass  # Adicione a funcionalidade de exibir perfil
            elif opcao == "2":
                # Notas
                pass  # Adicione a funcionalidade de exibir notas
            elif opcao == "3":
                # Frequências
                pass  # Adicione a funcionalidade de exibir frequências
            elif opcao == "4":
                # Tarefas
                pass  # Adicione a funcionalidade de exibir tarefas
            elif opcao == "5":
                # Calendário
                pass  # Adicione a funcionalidade do calendário
            elif opcao == "6":
                # Salvar Dados
                salvardados()
            elif opcao == "7":
                print("Até logo!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

if name == "_main":
    principal()
