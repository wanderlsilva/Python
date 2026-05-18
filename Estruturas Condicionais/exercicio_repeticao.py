alunos = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar aluno")
    print("2 - Gerar relatório")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = {}

        aluno["nome"] = input("Digite o nome do aluno: ")
        aluno["idade"] = int(input("Digite a idade do aluno: "))
        aluno["sexo"] = input("Digite o sexo do aluno: ")
        aluno["serie"] = input("Digite a série do aluno: ")

        aluno["disciplinas"] = []

        qtd_disciplinas = int(input("Quantas disciplinas deseja cadastrar para esse aluno? "))

        for i in range(qtd_disciplinas):
            disciplina = {}

            disciplina["nome"] = input(f"\nDigite o nome da {i + 1}ª disciplina: ")
            disciplina["notas"] = []

            for j in range(4):
                nota = float(input(f"Digite a {j + 1}ª nota de {disciplina['nome']}: "))
                disciplina["notas"].append(nota)

            media = sum(disciplina["notas"]) / 4
            disciplina["media"] = media

            aluno["disciplinas"].append(disciplina)

        alunos.append(aluno)

        print("\nAluno cadastrado com sucesso!")

    elif opcao == "2":
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
                    print(f"- {disciplina['nome']}: Média {disciplina['media']:.2f}")

    elif opcao == "3":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")