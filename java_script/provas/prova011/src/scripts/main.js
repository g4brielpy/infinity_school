import { sacar, depositar } from "./operacoes.js";

// saldo padrão da conta
let saldo = 1000.0;
demonstracao.innerHTML = `Saldo atual: R$ ${saldo.toFixed(2)}`;

// evento responsável por executar as operações
document.getElementById("caixa").addEventListener("submit", (event) => {
  event.preventDefault();

  const operacao = document.getElementById("operacoes").value;
  const valorOperacao = document.getElementById("input-valor-operacao").value;

  switch (operacao) {
    case "consultarSaldo":
      demonstracao.innerHTML = `Saldo atual: R$ ${saldo.toFixed(2)}`;
      break;
    case "sacar":
      try {
        saldo = sacar(valorOperacao, saldo);
        demonstracao.innerHTML = `Saque realizado!`;
      } catch (e) {
        demonstracao.innerHTML = e;
      }
      break;
    case "depositar":
      try {
        saldo = depositar(valorOperacao, saldo);
        demonstracao.innerHTML = `Deposito realizado!`;
      } catch (e) {
        demonstracao.innerHTML = e;
      }
      break;
  }

  document.getElementById("input-valor-operacao").value = "";
});

document.getElementById("operacoes").addEventListener("click", () => {
  if (document.getElementById("operacoes").value == "consultarSaldo") {
    document.getElementById("input-valor-operacao").style.display = "none";
  } else {
    document.getElementById("input-valor-operacao").style.display = "block";
  }
});
