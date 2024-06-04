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
    dados = [
        (ID, nome, "Sim" if ativo == 1 else "Não", matricula, curso)
        for ID, nome, ativo, matricula, curso in dados
    ]

    cursor.close()

    colunas = ["Id", "Nome", "Ativo", "Matricula", "Curso"]
    print("\n", tabulate(dados, colunas), "\n")


def pegar_id_curso() -> int:
    sql = '''
    SELECT
        id,
        descricao
    FROM
        curso
    '''

    cursor = db.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()

    colunas = ["Id", "Descrição"]
    print("\n", tabulate(dados, colunas), "\n")

    cursos_ids: list = [str(id) for id, _ in dados]
    while True:
        curso_id: str = input("Digite o ID de um curso existente: ")
        if curso_id in cursos_ids:
            break
        print("\nOpção inválida. Digite novamente!")

    return int(curso_id)


def pegar_matricula_aluno() -> str:
    sql = '''
    SELECT 
        aluno.nome,
        aluno.matricula,
        curso.descricao
    FROM 
        aluno
        INNER JOIN curso ON aluno.curso_id = curso.id;
    '''

    cursor = db.cursor()
    cursor.execute(sql)
    alunos = cursor.fetchall()

    cursor.close()

    colunas = ["Nome", "Matricula", "Curso"]
    print("\n", tabulate(alunos, colunas))

    matriculas: list = [matricula for _, matricula, _ in alunos]
    while True:
        matriculas_aluno = input(
            "\nInforme o id do aluno para ser desativado: ")
        if len(matriculas_aluno) == 5:
            if matriculas_aluno in matriculas:
                break
            else:
                print("Matricula não encontrada. Digite novamente!")
        else:
            print("Tamanho inválido da matricula. Digite novamente!")

    return matriculas_aluno


def verificar_matricula(matricula: str) -> bool:
    if len(matricula) > 5:
        return False

    sql = '''
    SELECT
        id, nome
    FROM
        aluno
    WHERE
        matricula = %s
    '''

    cursor = db.cursor()
    cursor.execute(sql, [matricula])
    dados = cursor.fetchone()

    cursor.close()

    return dados == None


def cadastrar_aluno(nome: str, matricula: str, id_curso: int) -> None:
    sql = '''
    INSERT INTO aluno (nome, matricula, curso_id)
    VALUES (%s, %s, %s)
    '''

    try:
        cursor = db.cursor()
        cursor.execute(sql, [nome, matricula, id_curso])
    except Exception as e:
        db.rollback()
        print("\nErro não tratado ao inserir novo:", e)
    else:
        db.commit()
        print("\nAluno cadastrado com sucesso!")
    finally:
        cursor.close()


def editar_aluno():
    pass


def desativar_aluno(matriculas_aluno: int):
    pass


def main():
    while True:
        system("cls")
        comando: str = menu()

        match comando:
            case "1":
                lista_alunos()

            case "2":
                nome: str = input("Digite o nome do aluno: ").strip()
                matricula: str = input(
                    "Digite a matricula do aluno (5 dígitos): ").strip()

                if not verificar_matricula(matricula):
                    print("Matricula repetida ou inválida!")
                else:
                    id_curso: int = pegar_id_curso()
                    cadastrar_aluno(nome, matricula, id_curso)

            case  "3":
                editar_aluno()

            case "4":
                matricula: str = pegar_matricula_aluno()
                print(f"Matricula do aluno: {matricula}")
                desativar_aluno(matricula)

            case "q":
                print("Programa finalizado!")
                break

        input('Aperte qualquer tecla para continuar...')


if __name__ == "__main__":
    main()
