class Tarefa:
    lista_de_tarefas: list = []

    def __init__(self, nome: str, descricao: str, prioridade: str, categoria: str) -> None:
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria

        if self.nome and self.descricao and self.prioridade and self.categoria:
            dados_tarefa = {
                'Nome': self.nome,
                'Descrição': self.descricao,
                'Prioridade': self.prioridade,
                'Categoria': self.categoria
            }
            self.lista_de_tarefas.append(dados_tarefa)

'''    def excluir_tarefa(self, nome_deletar: str):
        tarefas_copia = self.lista_de_tarefas.copy()

        for tarefa in tarefas_copia:
            if tarefa['Nome'] == nome_deletar:
                self.lista_de_tarefas.remove(tarefa)'''