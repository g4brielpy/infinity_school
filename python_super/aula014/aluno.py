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


def pegar_matricula_aluno(ativo=True) -> str:
    sql = '''
    SELECT 
        aluno.nome,
        aluno.matricula,
        curso.descricao
    FROM 
        aluno
        INNER JOIN curso ON aluno.curso_id = curso.id
    WHERE
        aluno.ativo = TRUE
    '''
    if not ativo:
        index_where = sql.index("WHERE")
        sql = sql[:index_where]

    cursor = db.cursor()
    cursor.execute(sql)
    alunos = cursor.fetchall()

    cursor.close()

    colunas = ["Nome", "Matricula", "Curso"]
    print("\n", tabulate(alunos, colunas))

    matriculas: list = [matricula for _, matricula, _ in alunos]
    while True:
        if ativo:
            matriculas_aluno = input("\nInforme a matricula do aluno ativo: ")
        else:
            matriculas_aluno = input("\nInforme a matricula do aluno: ")

        if matriculas_aluno in matriculas:
            break
        else:
            print("Matricula não encontrada. Digite novamente!")

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
        print(f"\nErro não tratado ao inserir novo aluno: {e}")
    else:
        db.commit()
        print("\nAluno cadastrado com sucesso!")
    finally:
        cursor.close()


def editar_aluno(matricula: str, nome=None, id_curso=None) -> None:
    if nome is None and id_curso is None:
        print("\nNenhum dado alterado! Informe o nome e/ou curso.")
        return None

    dados: list = []
    sql = '''
    UPDATE aluno
    SET 
        '''

    if nome is not None:
        sql += "nome = %s, "
        dados.append(nome)
    if id_curso is not None:
        sql += "curso_id = %s, "
        dados.append(id_curso)

    dados.append(matricula)
    sql = sql.rstrip(", ")
    sql += '''
    WHERE
        matricula = %s
    '''

    try:
        cursor = db.cursor()
        cursor.execute(sql, dados)
    except Exception as e:
        db.rollback()
        print(f"\nErro não tratado ao editar aluno: {e}")
    else:
        db.commit()
        print("\nAluno editado com sucesso!")
    finally:
        cursor.close()


def desativar_aluno(matriculas_aluno: str):
    sql = '''
    UPDATE 
        aluno 
    SET 
        ativo = FALSE
    WHERE
        matricula = %s
    '''

    try:
        cursor = db.cursor()
        cursor.execute(sql, [matriculas_aluno])
    except Exception as e:
        db.rollback()
        print(f"\nErro não tratado ao desativar aluno: {e}")
    else:
        db.commit()
        print("\nAluno desativado com sucesso!")
    finally:
        cursor.close()


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
                matricula: str = pegar_matricula_aluno(ativo=False)
                dados: list = [matricula]

                nome: str = input(
                    "Insira o novo nome ou aperte <Enter> para não alterar: ").strip()
                if nome:
                    dados.append(nome)

                while True:
                    alterar_curso: str = input("Alterar curso [S/N]: ").lower()
                    match alterar_curso:
                        case "s":
                            id_curso: int = pegar_id_curso()
                            dados.append(id_curso)
                            break
                        case "n":
                            break
                        case _:
                            print(
                                "\nOpção inválida. Insira 'S' ou 'N' para alterar o curso!")
                editar_aluno(*dados)

            case "4":
                matricula: str = pegar_matricula_aluno()
                desativar_aluno(matricula)

            case "q":
                print("Programa finalizado!")
                db.close()
                break

            case _:
                print("Opção inválida. Digíte novamente!")

        input('Aperte qualquer tecla para continuar...')


if __name__ == "__main__":
    main()
