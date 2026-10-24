titulo = input("Título: ")
prioridade = int(input("Prioridade (1 a 5): "))
prazo_horas = float(input("Prazo em horas: "))
urgente = input("É urgente? (sim/nao): ") == "sim"

esforco_estimado = prazo_horas * 1.2
prioritaria = prioridade >= 4 or urgente

print(f"Tarefa: {titulo}")
print(f"Esforço estimado: {esforco_estimado:.2f} horas")
print(f"Prioritária: {prioritaria}")
