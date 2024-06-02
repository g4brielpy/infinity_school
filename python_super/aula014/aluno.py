from conexao import db
from os import system
from tabulate import tabulate


def menu() -> str:
    print("\nGerenciamento de Alunos\n")
    print("[1] - Lista Alunos")
    print("[2] - Cadastrar Aluno")
    print("[3] - Editar Aluno")
    print("[4] - Desativar Aluno")
    print("[q] - Sair")

    comando = input("-> ")
    return comando


def lista_alunos() -> None:
    sql = '''
    SELECT 
        aluno.id,
        aluno.nome,
        aluno.ativo,
        aluno.matricula,
        curso.descricao
    FROM 
        aluno
        INNER JOIN curso ON aluno.curso_id = curso.id;
    '''

    cursor = db.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()

    colunas = ["Id", "Nome", "Ativo", "Matricula", "Curso"]
    print(tabulate(dados, colunas))


def pegar_id_curso() -> int:
    sql = '''
    SELECT
        id,
        descricao,
    FROM
        curso
    '''

    cursor = db.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()

    colunas = ["Id", "Descrição"]
    print(tabulate(dados, colunas))

    cursos_ids: list = [str(id) for id, _ in dados]
    while True:
        curso_id: str = input("Digite o ID de um curso existente: ")
        if curso_id in cursos_ids:
            break
        print("\nOpção inválida. Digite novamente!")

    return int(curso_id)


def verificar_matricula(matricula: str) -> bool:
    sql = '''
    SELECT
        id
    FROM
        alunos
    WHERE
        alunos.matricula = %s
    '''


def cadastrar_aluno():
    pass


def editar_aluno():
    pass


def desativar_aluno():
    pass


def main():
    while True:
        system("cls")
        comando: str = menu()

        match comando:
            case "1":
                lista_alunos()

            case "2":
                cadastrar_aluno()

            case  "3":
                editar_aluno()

            case "4":
                desativar_aluno()

            case "q":
                print("Programa finalizado!")
                break

        input('Aperte qualquer tecla para continuar...')


if __name__ == "__main__":
    main()
