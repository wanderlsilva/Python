# =========================
# FUNÇÃO PARA CADASTRAR ALUNO
# =========================

def cadastrar_aluno():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["sexo"] = input("Digite o sexo do aluno: ")
    aluno["serie"] = input("Digite a série do aluno: ")

    aluno["disciplinas"] = []

    qtd_disciplinas = int(input("Quantas disciplinas deseja cadastrar? "))

    for i in range(qtd_disciplinas):
        disciplina = cadastrar_disciplina(i)
        aluno["disciplinas"].append(disciplina)

    return aluno


# =========================
# FUNÇÃO PARA CADASTRAR DISCIPLINA
# =========================

def cadastrar_disciplina(i):
    disciplina = {}

    disciplina["nome"] = input(f"\nDigite o nome da {i + 1}ª disciplina: ")
    disciplina["notas"] = []

    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        disciplina["notas"].append(nota)

    disciplina["media"] = calcular_media(disciplina["notas"])

    return disciplina


# =========================
# FUNÇÃO PARA CALCULAR MÉDIA
# =========================

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


# =========================
# FUNÇÃO PARA MOSTRAR RELATÓRIO
# =========================

def mostrar_relatorio(alunos):
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.")
    else:
        print("\n===== RELATÓRIO FINAL =====")

        for aluno in alunos:
            print("\n----------------------------")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Sexo: {aluno['sexo']}")
            print(f"Série: {aluno['serie']}")

            print("\nDisciplinas:")

            for disciplina in aluno["disciplinas"]:
                print(f"{disciplina['nome']} -> Média: {disciplina['media']:.2f}")

                if disciplina["media"] >= 7:
                    print("Situação: Aprovado")

                elif disciplina["media"] >= 5:
                    print("Situação: Recuperação")

                else:
                    print("Situação: Reprovado")


# =========================
# FUNÇÃO MENU
# =========================

def menu():
    alunos = []

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Mostrar relatório")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aluno = cadastrar_aluno()
            alunos.append(aluno)

            print("\nAluno cadastrado com sucesso!")

        elif opcao == "2":
            mostrar_relatorio(alunos)

        elif opcao == "3":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


# =========================
# INICIANDO O SISTEMA
# =========================

menu()