from cadastro_tarefa import Tarefa
from gerenciador_chaamados import cadastrar_tarefa, listar_tarefas, filtrar_por_situacao

def main():
    tarefas = []

    cadastrar_tarefa(tarefas, "Revisar chamados", "Verificar chamados pendentes", "Alta", Tarefa)
    cadastrar_tarefa(tarefas, "Atualizar manual", "Ajustar instruções de atendimento", "Média", Tarefa)
    cadastrar_tarefa(tarefas, "Planejar reunião", "Preparar pauta semanal", "Baixa", Tarefa)

    tarefas[0].concluir()

    print("--- TODAS AS TAREFAS ---")
    listar_tarefas(tarefas)

    print("\n--- TAREFAS CONCLUÍDAS ---")
    listar_tarefas(filtrar_por_situacao(tarefas, "Concluída"))

if __name__ == "__main__":
    main()