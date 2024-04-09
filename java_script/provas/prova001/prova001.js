// [JS-A01] Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3).
// Calcule a média ponderada das notas e atribua o resultado à variável "media".
// Após o cálculo, exiba a média ponderada no console.

// Média ponderada: ((n1 * p1) + (n2 * p2) + (n3 * p3)) / soma dos pesos

let n1 = 8;
let p1 = 4;

let n2 = 6;
let p2 = 3;

let n3 = 4;
let p3 = 2;

let somaDasNotas = n1 * p1 + n2 * p2 + n3 * p3;
let somaDosPesos = p1 + p2 + p3;
let mediasPonderadasNotas = somaDasNotas / somaDosPesos;

console.log(
  `A Média Ponderada das notas é: ${mediasPonderadasNotas.toFixed(2)}`
);
