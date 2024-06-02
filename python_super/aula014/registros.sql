USE escola;

-- DML
INSERT INTO curso(descricao)
VALUES ("Desenvolvimento de Software"),
	("Ciência de Dados");

INSERT INTO aluno(nome, matricula, curso_id)
VALUES ("Gabriel", "12345", 1),
	("Iuri", "54321", 1),
	("Felipe", "98765", 2),
	("Fernando", "85296", 2),
    ("Jhon", "96385", 2);
    
INSERT INTO materia(descricao, sigla)
VALUES ("Python", "PY"),
	("JavaScript", "JS");
    
INSERT INTO professor(nome, cpf, materia_id)
VALUES ("Davi", "70506248987", 1),
	("Otavio", "70536987802", 2);