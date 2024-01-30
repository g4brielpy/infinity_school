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

    def excluir_tarefa(self, nome_deletar: str):
        if not self.lista_de_tarefas:
            return 'Não há tarefas para excluir'

        tarefas_copia = self.lista_de_tarefas.copy()

        for tarefa in tarefas_copia:
            if tarefa['Nome'] == nome_deletar:
                self.lista_de_tarefas.remove(tarefa)
                return f'Tarefa {nome_deletar} removida!'

        return f'Tarefa {nome_deletar} não encontrada!'

    def exibir_tarefas(self):
        if not self.lista_de_tarefas:
            return 'Não há tarefas para exibir.'

        minhas_tarefas = ''

        for i, tarefa in enumerate(self.lista_de_tarefas, start=1):
            minhas_tarefas += f'\nTAREFA {i}\n'
            minhas_tarefas += '\n'.join(
                [f'{chave}: {valor}' for chave, valor in tarefa.items()]) + '\n'

        return minhas_tarefas
