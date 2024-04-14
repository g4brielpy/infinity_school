# Ex02 Faça uma classe "Email" que deve ter as propriedades
# - email
# - pessoa
# - fl_principal

# Você também deve fazer uma classe "Pessoa" que obrigatóriamente precisa de
# um email para ser criado, essa classe deve conter as propriedades
# - nome
# - cpf
# - emails (uma lista de emails)
#
# Adicione também um metódo "adicionar_email()" que irá adicionar um email a pessoa
# OBS: Só pode haver um email principal

class Pessoa:
    def __init__(self, nome: str, cpf: str, email: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.email_principal = Email(email, self, True)
        self.emails = [self.email_principal]
    
    def __repr__(self) -> str:
        return f"<Pessoa - {self.nome}/ {self.cpf}/ Emails: {self.emails}>"


class Email:
    def __init__(self, email: str, pessoa: Pessoa, fl_principal: bool = False) -> None:
        self.email = email
        self.pessoa = pessoa
        self.fl_principal = fl_principal

    def __repr__(self) -> str:
        return f"<Email - {self.email}/ Principal {self.fl_principal}>"

    def adicionar_email(self, email: str):
        pass
