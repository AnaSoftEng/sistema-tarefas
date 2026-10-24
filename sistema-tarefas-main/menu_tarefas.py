tarefas = ["Revisar código", "Atualizar documentação"]
while True:
    print("\n1. Listar tarefas")
    print("2. Cadastrar tarefa")
    print("3. Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f"{indice}. {tarefa}")
    elif opcao == "2":
        titulo = input("Título da tarefa: ")
        tarefas.append(titulo)
        print("Tarefa cadastrada.")
    elif opcao == "3":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")
