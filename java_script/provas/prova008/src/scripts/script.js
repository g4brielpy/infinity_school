// Prova [JS-A08]

// Instruções:

// Selecione a unidade de medida de destino no segundo menu suspenso.
// Você pode escolher entre "Jarda", "Pé", "Polegada" ou "Milha".

// Clique no botão "Converter" para ver o resultado da conversão.

// Dicas de Valores:
//  * Um metro é aproximadamente igual a 1.094 jardas, 3.281 pés, 39.37 polegadas ou 0.000621 milhas.

const buttonConverter = document.getElementById("buttonConverter");
const main = document.getElementById("conteudo");
const resultado = document.createElement("p");

const converter = () => {
  const inputMetros = document.getElementById("inputMetros").value;
  const inputUnidade = document.getElementById("inputUnidade").value;

  const getValorUnidade = () => {
    const valoresUnidades = {
      polegadas: 39.37,
      milhas: 0.000621,
      jardas: 1.094,
      pes: 3.281,
    };
    return valoresUnidades[inputUnidade];
  };

  const getValorConvertido = () => {
    const valorUnidade = getValorUnidade();
    const valorConvertido = inputMetros * valorUnidade;

    return exibirValorConvertido(valorConvertido);
  };

  const exibirValorConvertido = (valor) => {
    resultado.setAttribute("id", "resultado");
    resultado.textContent = `Valor convertido: ${valor}`;
    main.appendChild(resultado);
  };

  getValorConvertido();
};

buttonConverter.addEventListener("click", (event) => {
  event.preventDefault();
  converter();
});
