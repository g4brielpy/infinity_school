class Tarefa:
    def __init__(self, nome: str, descricao: str, prioridade: str, categoria: str) -> None:
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.lista_de_tarefas: list = []

    def criar_tarefa(self):
        tarefa = {
            'Nome': self.nome,
            'Descrição': self.descricao,
            'Prioridade': self.prioridade,
            'Categoria': self.categoria
        }
        self.lista_de_tarefas.append(tarefa)
