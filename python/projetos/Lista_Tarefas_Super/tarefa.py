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
                'Categoria': self.categoria,
                'Status': 'A Fazer'
            }
            self.lista_de_tarefas.append(dados_tarefa)

    def verificar_nome(self, nome: str) -> bool:
        for tarefa in self.lista_de_tarefas:
            if tarefa['Nome'] == nome:
                return False
        return True

    def excluir_tarefa(self, nome_deletar: str) -> str:
        if not self.lista_de_tarefas:
            return 'Não há tarefas para excluir'

        tarefas_copia = self.lista_de_tarefas.copy()

        for tarefa in tarefas_copia:
            if tarefa['Nome'] == nome_deletar:
                self.lista_de_tarefas.remove(tarefa)
                return f'Tarefa {nome_deletar} removida!'

        return f'Tarefa {nome_deletar} não encontrada!'

    def exibir_tarefas(self) -> str:
        if not self.lista_de_tarefas:
            return 'Não há tarefas para exibir.'

        minhas_tarefas = ''

        for i, tarefa in enumerate(self.lista_de_tarefas, start=1):
            minhas_tarefas += f'\nTAREFA {i}\n'
            minhas_tarefas += '\n'.join(
                [f'{chave}: {valor}' for chave, valor in tarefa.items()]) + '\n'

        return minhas_tarefas

    def exibir_tarefas_categoria(self, categoria: str) -> str:
        if not self.lista_de_tarefas:
            return 'Não há tarefas para exibir.'

        minhas_tarefas_categoria = ''

        for tarefa in self.lista_de_tarefas:
            if tarefa['Categoria'] == categoria:
                minhas_tarefas_categoria += f'\nTAREFA CATEGORIA\n'
                minhas_tarefas_categoria += '\n'.join(
                    [f'{chave}: {valor}' for chave, valor in tarefa.items()]) + '\n'

        if not minhas_tarefas_categoria:
            return f'Tarefas da categoria {categoria} não existe.'
        else:
            return minhas_tarefas_categoria

    def exibir_tarefa_prioridade(self, prioridade: str) -> str:
        if not self.lista_de_tarefas:
            return 'Não há tarefas para exibir.'

        minhas_tarefas_prioridade = ''

        for tarefa in self.lista_de_tarefas:
            if tarefa['Prioridade'] == prioridade:
                minhas_tarefas_prioridade += f'\nTAREFA PRIORIDADE\n'
                minhas_tarefas_prioridade += '\n'.join(
                    [f'{chave}: {valor}' for chave, valor in tarefa.items()])
                
        if not minhas_tarefas_prioridade:
            return f'Tarefas da prioridade {prioridade} não existe.'
        else:
            return minhas_tarefas_prioridade
