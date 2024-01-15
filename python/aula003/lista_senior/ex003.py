'''
Dado o seguinte dicionario, preciso verificar se o usuario esta em home_office caso
ele esteja crie um texto com a seguinte descrição:

    “Usuario que mora na regional {numero da regional}, esta em Home-
    office ele possui a matricula: {numero de matricula} e telefone
    {numero de telefone}”)
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

user_home_office = dados['requested_items'][0]['custom_fields']['usuario_em_home_office']

if user_home_office.lower() == 'sim':
    regiao_user_home_office = dados["requested_items"][0]['custom_fields']['regional']
    matricula_user_home_office = dados["requested_items"][0]['custom_fields']['matricula_do_associado']
    telefone_user_home_office = dados["requested_items"][0]['custom_fields']['telefone']

    print(f"\nUsuario que mora na regional {regiao_user_home_office} esta em Home-office ele possui a matricula: {
        matricula_user_home_office} e telefone {telefone_user_home_office}\n")
else:
    print('Usuário não estar em home-office')
