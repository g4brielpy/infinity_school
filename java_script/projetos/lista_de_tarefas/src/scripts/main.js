// < Projeto lista de tarefas v-1.0 - Gabriel Iuri >

// selecionando os elementos do HTML;
const buttonAdd = document.querySelector("#buttonAdd");
const inputAddTarefa = document.querySelector("#inputAddTarefa");
const sectionTarefas = document.querySelector("#listaDeTarefas");

// iniciando a lista de tarefas como um array;
let listaTarefas = [];

// função para exibir as tárefas válidas no HTML
const exibirTarefas = () => {
  // limpando as tarefas para não duplicar
  sectionTarefas.innerHTML = "";

  // iterando sobre a lista e exibindo todas as tarefas
  listaTarefas.forEach((tarefa, index) => {
    const containerTarefa = document.createElement("li");

    const buttonLixo = document.createElement("button");
    buttonLixo.setAttribute("class", "buttonLixo");
    buttonLixo.setAttribute("data-tarefa-id", index);

    const imgLixo = document.createElement("img");
    imgLixo.setAttribute("src", "src/image/lixo.png");
    imgLixo.setAttribute("alt", "Lixo");

    buttonLixo.appendChild(imgLixo);

    const estruturaHTML = tarefa.slice(0, 40);

    // set os atributos necessários, e add id único a cada tarefa
    containerTarefa.setAttribute("id", `tarefa_${index}`);
    containerTarefa.setAttribute("class", "boxTarefa");

    // definindo o conteúdo e adicionando a lista de tarefas
    containerTarefa.innerHTML = estruturaHTML;
    containerTarefa.appendChild(buttonLixo);
    sectionTarefas.appendChild(containerTarefa);
  });

  // add evento de click para deletar tarefa
  const listaButtonLixo = document.querySelectorAll(".buttonLixo");
  listaButtonLixo.forEach((button, index) => {
    button.addEventListener("click", () => {
      excluirTarefa(index);
    });
  });
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

const excluirTarefa = (id) => {
  listaTarefas.splice(id, 1);
  exibirTarefas();
};

// adicionar um observador de 'clicks' no elemento 'button' e 'lixeira'
buttonAdd.addEventListener("click", () => {
  // adicionar tarefa
  adicionarTarefa();
  // limpar o valor do input
  inputAddTarefa.value = "";
});
