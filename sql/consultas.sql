USE escola;

-- consultar alunos e cursos
SELECT 
	aluno.id,
    aluno.nome AS Aluno,
    aluno.matricula AS Matricula,
    curso.descricao AS Curso
FROM 
	aluno
    INNER JOIN curso ON aluno.curso_id = curso.id
WHERE
	aluno.ativo = 1;

-- consultar professores e matérias
SELECT
	professor.id,
    professor.nome AS professor,
    (CASE
		WHEN professor.ativo = 1 THEN "Sim"
        ELSE "Não"
    END) AS ativo,
    materia.descricao AS materia,
    materia.sigla
FROM
	professor
    INNER JOIN materia ON professor.materia_id = materia.id;