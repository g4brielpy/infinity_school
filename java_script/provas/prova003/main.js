// [JS-A03] Você foi contratado(a) para desenvolver um programa que irá auxiliar um professor a calcular algumas estatísticas das notas de seus alunos.
// O programa deve solicitar ao professor o número total de estudantes na turma e, em seguida, pedir que ele insira as notas de cada aluno individualmente.
// Após receber todas as notas, o programa deverá calcular a média da turma e identificar a maior e a menor nota obtida.

// Instruções:

// 1. Solicite ao professor que digite o número total de estudantes na turma. OK
// 2. Em seguida, peça que o professor insira a nota de cada aluno individualmente, uma por vez. OK
// 3. Calcule a média da turma somando todas as notas e dividindo pelo número total de estudantes. OK
// 4. Identifique e registre a maior nota obtida na turma. OK
// 5. Ao final, exiba a média da turma e a maior e a menor nota encontrada. OK

// Dicas:

// 1. Utilize um loop while para coletar as notas de todos os alunos. OK
// 2. Armazene as notas em uma variável e vá atualizando o valor da soma a cada nova nota inserida. OK
// 3. Compare cada nota com a maior nota atualmente registrada para encontrar a maior nota. OK
// 4. Para calcular a média, divida a soma das notas pelo número total de estudantes. OK
// 5. Exiba os resultados de forma clara e organizada.

import input from "readline-sync";

function calcularMedia(notas) {
  let somaNotas = 0;
  let qtdsNotas = notas.length;

  for (let nota of notas) {
    somaNotas += nota;
  }
  let media = somaNotas / qtdsNotas;
  return media;
}

function getMaiorNota(notas) {
  let maiorNota = 0;

  for (let nota of notas) {
    if (nota > maiorNota) {
      maiorNota = nota;
    }
  }
  return maiorNota;
}

function getMenorNota(notas) {
  let menorNota = notas[0];

  for (let nota of notas) {
    if (nota < menorNota) {
      menorNota = nota;
    }
  }
  return menorNota;
}

console.log("\n-- MÉDIA DA SALA --\n");
const quantidadeAlunos = input.question("Digite a quantidade de alunos: ");
let notasAluno = [];
let i = 1;

while (i <= quantidadeAlunos) {
  let nota = Number(input.question(`Digite a nota do ${i}o aluno: `));
  if (!isNaN(nota)) {
    notasAluno.push(nota);
  }
  i++;
}
const mediaAlunos = calcularMedia(notasAluno);
const maiorNotaAluno = getMaiorNota(notasAluno);
const menorNotaAluno = getMenorNota(notasAluno);

console.log("\nRESULTADO\n");
console.log(`Média dos alunos: ${mediaAlunos}`);
console.log(`Maior nota: ${maiorNotaAluno}`);
console.log(`Menor nota: ${menorNotaAluno}`);
