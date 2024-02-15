'''
No mesmo dicionario preciso que informe na tela o “Service_item_id” e o
“Service_item_name”
'''

dados = {
    'requested_items': [
        # dicionário [0]
        {
            'custom_fields': {
                'ticket_origem': 'SR-1020070',
                'url_ticket_origem': 'https://servicedesk.algartech.com/helpdesk/tickets/1020070',
                'tipo_de_solicitacao': 'ESTACAO DE TRABALHO - DESATIVAR',
                'descricao_resumida': 'recolha de monitor ',
                'regional': 17000313903,
                'telefone': '34992106551',
                'usuario_em_home_office': 'Sim',  # HOME OFFICE
                'horario_de_entrega_recolhimento': 'null',
                'matricula_do_associado': '92266',
                'numero_de_patrimonio_dos_ativos': '-',
                'chamado_categorizado_como_mau_uso': 'null',
                'equipamentos_faltantes_nao_devolvidos_em_recolha': 'null',
                'itens_faltantes': 'null',
                'solucao_aplicada': 'null',
                'chamado_improcedente': 'null',
                'quantidade_de_usuario_afetado': 'null',
                'aprovador': 'null',
                'ticket_com_fornecedor': 'null',
                'tratativa_com_fornecedor': 'null',
                'tentativa_de_contato': 'null'
            },
            'id': 17004351221,
            'created_at': '2023-07-19T18:51:51Z',
            'updated_at': '2023-07-19T18:51:51Z',
            'quantity': 1,
            'stage': 1,
            'loaned': 'false',
            'cost_per_request': 0.0,
            'remarks': 'null',
            'delivery_time': 'null',
            'is_parent': 'true',
            'service_item_id': 246,
            'service_item_name': 'HOME OFFICE ALMOXARIFADO'
        }
    ]
}

print(f"Service item id: {dados['requested_items'][0]['service_item_id']}")
print(f"Service item name: {dados['requested_items'][0]['service_item_name']}")