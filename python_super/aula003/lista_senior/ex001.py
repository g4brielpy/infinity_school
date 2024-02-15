'''
Dado o seguinte dicionario, preciso que altere todos os campos que estao com valor
null praa 'vazio'.(exe1)
'''

dados = {
    "ticket_origem": "SR-1020070",
    "url_ticket_origem": "https://servicedesk.algartech.com/helpdesk/tickets/1020070",
    "tipo_de_solicitacao": "ESTACAO DE TRABALHO - DESATIVAR",
    "descricao_resumida": "recolha de monitor ",
    "regional": 17000313903,
    "telefone": "34992106551",
    "usuario_em_home_office": "Não",    "endereco_completo_destino_rua_avenida_numero_tipo_n_apto_casa_bloco_bairro": "R. José Ayube, 260 - Fundinho, Uberlândia - MG, 38400-188",
    "horario_de_entrega_recolhimento": 'null',
    "matricula_do_associado": "92266",
    "numero_de_patrimonio_dos_ativos": "-",
    "chamado_categorizado_como_mau_uso": 'null',
    "equipamentos_faltantes_nao_devolvidos_em_recolha": 'null',
    "itens_faltantes": 'null',
    "solucao_aplicada": 'null',
    "chamado_improcedente": 'null',
    "quantidade_de_usuario_afetado": 'null',
    "aprovador": 'null',
    "ticket_com_fornecedor": 'null',
    "tratativa_com_fornecedor": 'null',
    "tentativa_de_contato": 'null'
}

for chave, valor in dados.items():
    if valor == 'null':
        dados[chave] = 'vazio'

print(dados)
