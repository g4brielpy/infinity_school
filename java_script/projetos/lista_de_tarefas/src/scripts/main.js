// by: Gabriel Iuri - g4brielpy

import { criarElemento } from "./elementos.js";

const inputAddTarefa = document.querySelector("input#inputAddTarefa");
const buttonAdd = document.querySelector("button#buttonAdd");
const secaoTarefas = document.querySelector("ol#listaDeTarefas");

const listaTarefas = [];

const validarTarefa = (novaTarefa) => {
  if (!novaTarefa.nome) {
    alert("Tarefa Inválida!");
    return false;
  }
  for (const tarefa of listaTarefas) {
    if (tarefa.nome == novaTarefa.nome) {
      alert("Essa Tarefa Já Existe!");
      return false;
    }
  }
  return true;
};

const adicionarTarefa = () => {
  const tarefaAtual = {
    nome: inputAddTarefa.value.trim(),
    status: false,
  };
  validarTarefa(tarefaAtual) && listaTarefas.push(tarefaAtual);
};

const excluirTarefa = (id) => {
  listaTarefas.splice(id, 1);
};

const concluirTarefa = (id) => {
  const tarefa = listaTarefas[id].nome;
  const tarefaConcluirda = { nome: `<del>${tarefa}</del>`, status: true };

  listaTarefas.splice(id, 1, tarefaConcluirda);
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
    li.innerHTML = tarefa.nome;

    const buttonLixo = criarElemento("lixo");
    const buttonConcluir = criarElemento("concluir");

    const spanContainerImg = document.createElement("span");
    spanContainerImg.setAttribute("class", "containerImg");

    spanContainerImg.appendChild(buttonLixo);
    spanContainerImg.appendChild(buttonConcluir);

    if (tarefa.status) {
      buttonConcluir.style.display = "none";
    }

    li.appendChild(spanContainerImg);
    secaoTarefas.appendChild(li);

    buttonLixo.addEventListener("click", () => {
      excluirTarefa(index);
      exibirTarefas();
    });
    buttonConcluir.addEventListener("click", () => {
      concluirTarefa(index);
      exibirTarefas();

      buttonConcluir.style.display = "none";
      buttonConcluir.removeEventListener("click", concluirTarefa);
    });
  });
};

buttonAdd.addEventListener("click", () => {
  adicionarTarefa();
  exibirTarefas();
  inputAddTarefa.value = "";
});
