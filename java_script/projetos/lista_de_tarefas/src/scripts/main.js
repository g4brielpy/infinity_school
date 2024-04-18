const inputAddTarefa = document.querySelector("input#inputAddTarefa");
const buttonAdd = document.querySelector("button#buttonAdd");
const secaoTarefas = document.querySelector("ol#listaDeTarefas");
const listaTarefas = [];

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
  listaTarefas.splice(id, 1);
  exibirTarefas();
};

const exibirTarefas = () => {
  secaoTarefas.innerHTML = "";
  listaTarefas.forEach((tarefa, index) => {
    // Estrutura de cada item da tarefa:

    //     <li class="boxTarefa">
    //     'Nome da Nota'
    //     <button class="buttonLixo">
    //       <img src="src\image\lixo.png" alt="Lixo" title="Excluir" />
    //     </button>
    //   </li>

    const li = document.createElement("li");
    li.setAttribute("class", "boxTarefa");
    li.textContent = tarefa;

    const imgLixo = document.createElement("img");
    imgLixo.setAttribute("src", "src/image/lixo.png");
    imgLixo.setAttribute("alt", "Lixo");
    imgLixo.setAttribute("title", "Excluir");

    const buttonLixo = document.createElement("button");
    buttonLixo.setAttribute("class", "buttonLixo");
    buttonLixo.appendChild(imgLixo);

    li.appendChild(buttonLixo);
    secaoTarefas.appendChild(li);

    buttonLixo.addEventListener("click", () => {
      excluirTarefa(index);
    });
  });
};

buttonAdd.addEventListener("click", () => {
  adicionarTarefa();
  inputAddTarefa.value = "";
});
