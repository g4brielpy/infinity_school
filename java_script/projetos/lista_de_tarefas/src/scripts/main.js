// selecionando os elementos do HTML;
const btnExcluirTarefa = document.querySelectorAll(".btnExcluirTarefa");
const buttonAdd = document.querySelector("#buttonAdd");
const inputAddTarefa = document.querySelector("#inputAddTarefa");
const sectionTarefas = document.querySelector("#sectionTarefas");
// iniciando a lista de tarefas como um array;
let listaTarefas = [];

// função base para adicionar as tarefas
const adcionarTarefa = () => {
  // tarefa há ser acresentada
  const tarefa = inputAddTarefa.value.trim();

  // função para exibir as tárefas válidas no HTML
  const exibirTarefas = () => {
    // limpando as tarefas para não duplicar
    sectionTarefas.innerHTML = "";

    // iterando sobre a lista e exibindo todas as tarefas
    listaTarefas.forEach((tarefa, index) => {
      const containerTarefa = document.createElement("div");
      const estruturaHTMLTarefa = `
            <p class="tituloTarefa">${tarefa}</p>
            <div class="iconeOpcoes">
              <div class="boxImg">
                <img src="src/image/definicoes.png" alt="Definicoes" />
              </div>
              <div class="boxImg btnExcluirTarefa" data-tarefa-id="${index}">
                <img src="src/image/lixo.png" alt="Lixo" />
              </div>
            </div>
      `;

      // set os atributos necessários, e add id único a cada tarefa
      containerTarefa.setAttribute("id", `tarefa_${index}`);
      containerTarefa.setAttribute("class", "boxTarefa");
      // definindo o conteúdo e adicionando a lista de tarefas
      containerTarefa.innerHTML = estruturaHTMLTarefa;
      sectionTarefas.appendChild(containerTarefa);
    });
  };

  // função para verifica se a tarefa é válida
  const verificarTarefaValida = () => {
    // verificar se a tarefa é vazia ou muito longa
    if (tarefa === "" || tarefa.length > 50) {
      return false;
    }

    // verificar se a tarefa já existe na lista
    for (const tarefaAtual of listaTarefas) {
      if (tarefaAtual === tarefa) {
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
  alert("Função excluir");
  console.log("ID da Tarefa a ser excluída: " + id);
};

// adicionar um observador de 'clicks' no elemento 'button' e 'lixeira'
buttonAdd.addEventListener("click", () => {
  // adicionar tarefa
  adcionarTarefa();
  // limpar o valor do input
  inputAddTarefa.value = "";
});

btnExcluirTarefa.forEach((button) => {
  console.log("Botão de exclusão selecionado:", button);

  button.addEventListener("click", () => {
    console.log("Teste");

    const indexExcluir = parseInt(button.getAttribute("data-tarefa-id"));
    excluirTarefa(indexExcluir);
  });
});
