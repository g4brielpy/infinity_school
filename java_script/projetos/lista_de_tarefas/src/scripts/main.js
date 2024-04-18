// < Projeto lista de tarefas v-1.0 - Gabriel Iuri >

// selecionando os elementos do HTML;
const buttonAdd = document.querySelector("#buttonAdd");
const inputAddTarefa = document.querySelector("#inputAddTarefa");
const sectionTarefas = document.querySelector("#listaDeTarefas");

// iniciando a lista de tarefas como um array;
// subistituir a array por um dicionário,
// colocando os index como chave
const listaTarefas = [];
const listaTarefasConcluidas = [];

// add evento de click para deletar tarefa
const adicionarEventoLixo = () => {
  const listaButtonLixo = document.querySelectorAll(".buttonLixo");
  listaButtonLixo.forEach((button, index) => {
    button.addEventListener("click", () => {
      excluirTarefa(index);
    });
  });
};
const excluirTarefa = (id) => {
  listaTarefas.splice(id, 1);
  exibirTarefas();
};

// ...

// função para adicionar evento de concluir tarefa
const adicionarEventoConcluir = () => {
  const listButtonConcluir = document.querySelectorAll(".buttonConcluir");

  listButtonConcluir.forEach((button, index) => {
    button.addEventListener("click", () => {
      concluirTarefa(index);
      button.removeEventListener("click", adicionarEventoConcluir);
    });
  });
};
const concluirTarefa = (id) => {
  const tarefa = listaTarefas[id];
  listaTarefasConcluidas.push(tarefa);
  exibirTarefas();
};

// função para exibir as tárefas válidas no HTML
const exibirTarefas = () => {
  // limpando as tarefas para não duplicar
  sectionTarefas.innerHTML = "";

  // iterando sobre a lista e exibindo todas as tarefas
  listaTarefas.forEach((tarefa, index) => {
    const containerTarefa = document.createElement("li");
    const boxImg = document.createElement("span");
    boxImg.setAttribute("id", "boxImg");

    const buttonLixo = document.createElement("button");
    buttonLixo.classList.add("buttonTarefa");
    buttonLixo.classList.add("buttonLixo");

    const buttonConcluir = document.createElement("button");
    buttonConcluir.classList.add("buttonTarefa");
    buttonConcluir.classList.add("buttonConcluir");

    const imgLixo = document.createElement("img");
    imgLixo.setAttribute("src", "src/image/lixo.png");
    imgLixo.setAttribute("alt", "Lixo");

    const imgConcluir = document.createElement("img");
    imgConcluir.setAttribute("src", "src/image/verificar.png");
    imgConcluir.setAttribute("alt", "Concluir Tarefa");

    buttonLixo.appendChild(imgLixo);
    buttonConcluir.appendChild(imgConcluir);

    boxImg.appendChild(buttonLixo);

    // verifica se a tarefa está concluída
    if (listaTarefasConcluidas.includes(tarefa)) {
      const tarefaConcluida = document.createElement("del");
      tarefaConcluida.textContent = tarefa;
      containerTarefa.appendChild(tarefaConcluida);
    } else {
      // adiciona a tarefa normalmente
      containerTarefa.textContent = tarefa;
    }

    // adiciona o botão de concluir apenas se a tarefa não estiver concluída
    if (!listaTarefasConcluidas.includes(tarefa)) {
      boxImg.appendChild(buttonConcluir);
    }

    containerTarefa.appendChild(boxImg);
    containerTarefa.setAttribute("id", `tarefa_${index}`);
    containerTarefa.setAttribute("class", "boxTarefa");
    sectionTarefas.appendChild(containerTarefa);
  });

  // add evento de click concluir tarefa
  adicionarEventoConcluir();

  // add evento de click para deletar e concluir tarefa
  adicionarEventoLixo();
};

// função base para adicionar as tarefas
const adicionarTarefa = () => {
  // tarefa há ser acresentada
  const tarefa = inputAddTarefa.value.trim();

  // função para verifica se a tarefa é válida
  const verificarTarefaValida = () => {
    // verificar se a tarefa é vazia ou muito longa
    if (tarefa == "") {
      return false;
    }

    // verificar se a tarefa já existe na lista
    for (let tarefaAtual of listaTarefas) {
      if (tarefaAtual == tarefa) {
        return false;
      }
    }

    return true;
  };

  // verificando se tarefa é valida através da função
  if (verificarTarefaValida()) {
    listaTarefas.push(tarefa);
    exibirTarefas();
  } else {
    alert("Tarefa Inválida!");
  }
};

// adicionar um observador de 'clicks' no elemento 'button' e 'lixeira'
buttonAdd.addEventListener("click", () => {
  // adicionar tarefa
  adicionarTarefa();
  // limpar o valor do input
  inputAddTarefa.value = "";
});
