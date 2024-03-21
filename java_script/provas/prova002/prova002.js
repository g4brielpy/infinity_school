// [JS-A02] Escreva um programa em JavaScript que solicite ao usuário o nome, altura em centímetros e peso de uma pessoa. O programa deve calcular o índice de massa corporal (IMC) dessa pessoa, considerando a fórmula IMC = peso / (altura * altura), onde a altura deve ser convertida de centímetros para metros. Em seguida, o programa deve classificar o peso com base no IMC calculado, de acordo com a tabela a seguir:

// Menor que 16: Baixo peso muito grave
// De 16 a 16.99: Baixo peso grave
// De 17 a 18.49: Baixo peso
// De 18.50 a 24.99: Peso normal
// De 25 a 29.99: Sobrepeso
// De 30 a 34.99: Obesidade grau I
// De 35 a 39.99: Obesidade grau II
// Maior ou igual a 40: Obesidade grau III

// O programa deve exibir o nome da pessoa, o índice de massa corporal calculado e a classificação correspondente.

import input from "readline-sync";

function calcularIMG(alturaCentimetros, peso) {
  const alturaEmMetros = alturaCentimetros / 100;
  const IMC = peso / alturaEmMetros ** 2;

  return IMC.toFixed(2);
}

function definirPeso(imc) {
  if (imc < 16) {
    return "Baixo peso muito grave";
  } else if (imc >= 16 && imc <= 16.99) {
    return "Baixo peso grave";
  } else if (imc >= 17 && imc <= 18.49) {
    return "Baixo peso";
  } else if (imc >= 18.5 && imc <= 24.99) {
    return "Peso normal";
  } else if (imc >= 25 && imc <= 29.99) {
    return "Sobrepeso";
  } else if (imc >= 30 && imc <= 34.99) {
    return "Obesidade grau I";
  } else if (imc >= 35 && imc <= 39.99) {
    return "Obesidade grau II";
  } else {
    return "Obesidade grau III";
  }
}

console.log("\n-- CALCULO DE IMG --\n");

const nome = input.question("Digite seu nome: ");
const alturaEmCentimetros = input.question("Digite sua altura (cm): ");
const peso = input.question("Digite seu peso (k): ");

const IMC = calcularIMG(alturaEmCentimetros, peso);
const classificacaoPesoIMC = definirPeso(IMC);

console.log(
  `\nNome: ${nome}, IMC: ${IMC} \nClassificação: ${classificacaoPesoIMC}\n`
);
