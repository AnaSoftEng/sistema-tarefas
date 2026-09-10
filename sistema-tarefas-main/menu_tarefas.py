from cadastro_tarefa import Tarefa
from gerenciador_chaamados import cadastrar_tarefa, listar_tarefas, filtrar_por_situacao

def exibir_menu():
    tarefas = []
    
    while True:
        print("\n=== SISTEMA DE GESTÃO DE TAREFAS ===")
        print("1. Cadastrar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Filtrar por Situação")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta/Média/Baixa): ")
            cadastrar_tarefa(tarefas, titulo, descricao, prioridade, Tarefa)
            print("Tarefa cadastrada com sucesso!")
            
        elif opcao == "2":
            print("\n--- LISTA DE TAREFAS ---")
            listar_tarefas(tarefas)
            
        elif opcao == "3":
            listar_tarefas(tarefas)
            if tarefas:
                num = int(input("Digite o número da tarefa a concluir: ")) - 1
                if 0 <= num < len(tarefas):
                    tarefas[num].concluir()
                    print("Tarefa concluída!")
                else:
                    print("Número inválido.")
                    
        elif opcao == "4":
            sit = input("Situação (Pendente/Concluída): ").strip().capitalize()
            filtradas = filtrar_por_situacao(tarefas, sit)
            print(f"\n--- TAREFAS ({sit.upper()}) ---")
            listar_tarefas(filtradas)
            
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    exibir_menu()