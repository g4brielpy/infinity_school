// [JS-A04] Você é um desenvolvedor de software que trabalha em uma equipe especializada em criar ferramentas matemáticas para uma empresa do mercado financeiro.
// A empresa precisa de uma nova funcionalidade para sua plataforma online, permitindo que os usuários obtenham informações sobre cálculos matemáticos importantes relacionados aos investimentos.

// Sua tarefa é criar um módulo JavaScript que ofereça aos usuários a possibilidade de inserir um número 1º inteiro positivo e, em resposta, 2° calcular o fatorial desse número e também a 3º sequência de Fibonacci até aquele número.

import input from "readline-sync";

function fatorial(num) {
  let c = num;

  while (c > 1) {
    c--;
    num *= c;
  }

  return num;
}

function fibonacci(num) {
  if (num > 1) {
    let sequencia = [];
    let f1 = 1;
    let f2 = 0;
    let f3 = 0;

    while (f3 < num) {
      sequencia.push(f3);
      f3 = f2 + f1;
      f1 = f2;
      f2 = f3;
    }
    return sequencia;
  } else {
    return [1, 1];
  }
}

console.log("\nANÁLISE INANCEIRO\n");
const numero = input.question("Digite o valor para a analise: ");

if (!isNaN(numero)) {
  console.log(`Fatorial: ${fatorial(numero)}`);
  console.log(`Fibonacci: ${fibonacci(numero)}\n`);
} else {
  console.log("Valor inválido!");
}
