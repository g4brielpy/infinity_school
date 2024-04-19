// by: Gabriel Iuri - g4brielpy

const inputAddTarefa = document.querySelector("input#inputAddTarefa");
const buttonAdd = document.querySelector("button#buttonAdd");
const secaoTarefas = document.querySelector("ol#listaDeTarefas");

const listaTarefas = [];
const listaTarefasDeletadas = [];
const listaTarefasConcluidas = [];

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

const validarTarefa = (novaTarefa) => {
  if (!novaTarefa) {
    return false;
  }
  for (const tarefa of listaTarefas) {
    if (tarefa == novaTarefa) {
      return false;
    }
  }
  return true;
};

const adicionarTarefa = () => {
  const tarefaAtual = inputAddTarefa.value.trim();
  validarTarefa(tarefaAtual)
    ? listaTarefas.push(tarefaAtual)
    : alert("Tarefa Inválida");

  exibirTarefas();
};

const excluirTarefa = (id) => {
  listaTarefasDeletadas.push(listaTarefas[id]);
  listaTarefas.splice(id, 1);

  exibirTarefas();
};

const concluirTarefa = (id) => {
  const tarefa = listaTarefas[id];
  listaTarefasConcluidas.push(tarefa);

  const tarefaConcluirda = `<del>${tarefa}</del>`;
  listaTarefas.splice(id, 1, tarefaConcluirda);

  exibirTarefas();
};

const exibirTarefas = () => {
  secaoTarefas.innerHTML = "";
  listaTarefas.forEach((tarefa, index) => {
    // Estrutura de cada item da tarefa:
    // Adicionar button lixo e 'CONCLUIR'

    // <li class="boxTarefa">
    //   Nome da Nota
    //   <span class="containerImg">
    //     <button class="buttonLixo">
    //       <img src="src\image\lixo.png" alt="Lixo" title="Excluir" />
    //     </button>
    //     <button class="buttonConcluir">
    //       <img src="src/image/verificar.png" alt="Verificar" />
    //     </button>
    //   </span>
    // </li>;

    const li = document.createElement("li");
    li.setAttribute("class", "boxTarefa");
    li.innerHTML = tarefa;

    const buttonLixo = criarElemento("lixo");
    const buttonConcluir = criarElemento("concluir");

    const spanContainerImg = document.createElement("span");
    spanContainerImg.setAttribute("class", "containerImg");

    spanContainerImg.appendChild(buttonLixo);
    spanContainerImg.appendChild(buttonConcluir);

    li.appendChild(spanContainerImg);
    secaoTarefas.appendChild(li);

    buttonLixo.addEventListener("click", () => {
      excluirTarefa(index);
    });
    buttonConcluir.addEventListener("click", () => {
      concluirTarefa(index);
      // remover button de concluir quando for clicado;
    });
  });
};

buttonAdd.addEventListener("click", () => {
  adicionarTarefa();
  inputAddTarefa.value = "";
});
