const criarElemento = (elemento) => {
  switch (elemento) {
    case "lixo":
      const imgLixo = document.createElement("img");
      imgLixo.setAttribute("src", "src/image/lixo.png");
      imgLixo.setAttribute("alt", "Lixo");
      imgLixo.setAttribute("title", "Excluir");

      const buttonLixo = document.createElement("button");
      buttonLixo.setAttribute("class", "buttonLixo");
      buttonLixo.appendChild(imgLixo);
      return buttonLixo;

    case "concluir":
      const imgConcluir = document.createElement("img");
      imgConcluir.setAttribute("src", "src/image/verificar.png");
      imgConcluir.setAttribute("alt", "Concluit");
      imgConcluir.setAttribute("title", "Concluir Tarefa");

      const buttonConcluir = document.createElement("button");
      buttonConcluir.setAttribute("class", "buttonConcluir");
      buttonConcluir.appendChild(imgConcluir);
      return buttonConcluir;
  }
};

export { criarElemento };
