const button_enviar = document.getElementById("button_calcular");

const calcularGorjeta = (event) => {
  event.preventDefault();

  const valorConta = Number(document.getElementById("valor_conta").value);
  const qualidadeServico = document.getElementById("qualidade_servico").value;
  const getProcentagemServico = {
    bom: 0.1,
    regular: 0.05,
    ruim: 0.01,
  };
  const valorProcentagem = getProcentagemServico[qualidadeServico];

  const exibirValorTotal = (valorTotal, valorGorjeta) => {
    const container = document.getElementById("container-valores");
    const labelGorjeta = "Valor da Gorjeta: ".padEnd(30, ".");
    const labelTotal = "Valor Total: ".padEnd(30, ".");

    container.innerHTML =
      "<p>" + labelGorjeta + ` R$ ${valorGorjeta.toFixed(2)} </p>`;
    container.innerHTML +=
      "<p>" + labelTotal + ` R$ ${valorTotal.toFixed(2)} </p>`;
  };

  const calcularValoresFinais = (valor, procentagem, callback) => {
    const valorGorjeta = valor * procentagem;
    const valorTotal = valor + valorGorjeta;
    callback(valorTotal, valorGorjeta);
  };

  calcularValoresFinais(valorConta, valorProcentagem, exibirValorTotal);
};

button_enviar.addEventListener("click", calcularGorjeta);
