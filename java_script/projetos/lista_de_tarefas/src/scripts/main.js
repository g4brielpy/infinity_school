// selecionando os elementos do HTML;
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
    for (const tarefa of listaTarefas) {
      sectionTarefas.innerHTML += `
          <div class="boxTarefa">
            <p class="tituloTarefa">${tarefa}</p>
            <div class="iconeOpcoes">
              <div class="boxImg">
                <img src="src/image/definicoes.png" alt="Definicoes" />
              </div>
              <div class="boxImg">
                <img src="src/image/lixo.png" alt="Lixo" />
              </div>
            </div>
          </div>
        `;
    }
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

// adicionar um observador de 'clicks' no elemento 'button'
buttonAdd.addEventListener("click", adcionarTarefa);
