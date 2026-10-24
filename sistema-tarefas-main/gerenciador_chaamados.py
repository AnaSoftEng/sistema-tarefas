class Tarefa:
    def __init__(self, titulo, prioridade):
        self.titulo = titulo
        self.prioridade = prioridade
        self.situacao = "Pendente"

    def concluir(self):
        self.situacao = "Concluída"

    def resumo(self):
        return f"{self.titulo} | {self.prioridade} | {self.situacao}"

def listar_tarefas(tarefas):
    for tarefa in tarefas:
        print(tarefa.resumo())

primeira = Tarefa("Revisar rotas", "Alta")
segunda = Tarefa("Atualizar documentação", "Média")
tarefas = [primeira, segunda]
primeira.concluir()
listar_tarefas(tarefas)
