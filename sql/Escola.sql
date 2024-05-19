USE escola;

SELECT * FROM curso;
SELECT * FROM aluno;
SELECT * FROM materia;
SELECT * FROM professor;


INSERT INTO curso(descricao)
VALUES
	("Desenvolvimento de Software"),
	("Ciência de Dados");
    
    
INSERT INTO aluno(nome, matricula, curso_id)
VALUES ("Gabriel Iuri", "12345", 1);

INSERT INTO aluno(nome, matricula, curso_id)
VALUES ("Davi", "54321", 1),
	("Felipe", "98765", 2),
    ("Fernando", "85296", 2);
    

INSERT INTO materia(descricao, sigla)
VALUES ("Python", "PY"),
	("JavaScript", "JS");
    
    
INSERT INTO professor(nome, cpf, materia_id)
VALUES ("Otavio", "70536987802", 2),
	("Davi", "70506248987", 1);