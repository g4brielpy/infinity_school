from conexao import db
from os import system
from tabulate import tabulate


def menu() -> str:
    print("\nGerenciamento de Professores\n")
    print("[1] - Lista Professores")
    print("[2] - Cadastrar Professores")
    print("[3] - Editar Professores")
    print("[4] - Desativar Professores")
    print("[q] - Sair")

    comando = input("-> ")
    return comando


def lista_professores() -> None:
    sql = '''
    SELECT
        professor.id,
        professor.nome,
        (CASE
            WHEN professor.ativo = 1 THEN "Sim"
            ELSE "Não"
        END) AS ativo,
        materia.descricao,
        materia.sigla
    FROM
	    professor
        INNER JOIN materia ON professor.materia_id = materia.id;
    '''

    cursor = db.cursor()
    cursor.execute(sql)

    dados = cursor.fetchall()
    cursor.close()

    colunas: list = ["Id", "Professor", "Ativo", "Materia", "Sigla"]
    print("\n", tabulate(dados, colunas))


def cadastrar_professor():
    pass


def editar_professor():
    pass


def desativar_professor():
    pass


def main() -> None:
    while True:
        system("cls")
        comando: str = menu()

        match comando:
            case "1":
                lista_professores()

            case "2":
                cadastrar_professor()

            case "3":
                editar_professor()

            case "4":
                desativar_professor()

            case "q":
                print("Programa finalizado!")
                db.close()
                break

            case _:
                print("Opção inválida. Digíte novamente!")

        input('\nAperte qualquer tecla para continuar...')


if __name__ == "__main__":
    main()
