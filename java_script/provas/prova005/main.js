// [JS-A05] Você foi convidado(a) a desenvolver um aplicativo web para ajudar a gerenciar as tarefas domésticas de uma família agitada.
// O objetivo é criar um "Gerenciador de Tarefas Domésticas" que permita que todos os membros da família adicionem, removam e atualizem suas tarefas diárias, garantindo que tudo seja feito de forma organizada.

import input from "readline-sync";

let lista_tarefas = [];

const adicionarTarefa = (nome, descricao, tarefas = lista_tarefas) => {
  //   verificar se a tarefa já existe.
  for (let tarefa of tarefas) {
    if (tarefa.Nome == nome || nome == "") {
      return false;
    }
  }

  // estrutura padrão para adicionar a lista de tarefas.
  let dadosTarefas = { Nome: nome, Descricao: descricao };
  return dadosTarefas;
};

const atualizarTarefas = (
  nomeTarefaAtualizar,
  novoNome,
  tarefas = lista_tarefas
) => {
  //   localizar a tarefa para fazer a alteração.
  for (let i = 0; i < tarefas.length; i++) {
    if (tarefas[i].Nome == nomeTarefaAtualizar) {
      lista_tarefas[i].Nome = novoNome;
      return true;
    }
  }

  //   retorna false caso a tarefa não exista
  return false;
};

const deletarTarefa = (nomeTarefaDeletar, tarefas = lista_tarefas) => {
  //   localizar a tarefa para fazer a deletar.
  for (let i = 0; i < tarefas.length; i++) {
    if (tarefas[i].Nome == nomeTarefaDeletar) {
      lista_tarefas.splice(i, 1);
      return [true, i];
    }
  }

  //   retorna false caso a tarefa não exista
  return false;
};

const menu = () => {
  // menu de opção para gerenciar as tarefas.
  console.log("\nGERENCIADOR DE TAREFAS DOMÉSTICAS");
  console.log("[1] - Adicionar Tarefa");
  console.log("[2] - Atualizar Tarefa");
  console.log("[3] - Remover Tarefa");
  console.log("[4] - Listar Tarefas");
  console.log("[q] - Sair");
};

let controle = true;
while (controle) {
  menu();
  const opcao = input.question("=> ");

  switch (opcao) {
    case "1":
      let nome = input.question("Nome da Tarefa: ").trim();
      let descricao = input.question("Descricao da Tarefa: ").trim();
      let tarefaValida = adicionarTarefa(nome, descricao);

      tarefaValida
        ? lista_tarefas.push(tarefaValida)
        : console.log("Tarefa Inválida!");
      tarefaValida && console.log("Tarefa Adicionada!");
      break;

    case "2":
      let nomeTarefaAlterar = input
        .question("Nome da Tarefa para Atualizar: ")
        .trim();
      let novoNome = input.question("Novo Nome da Tarefa: ").trim();
      let tarefaAtualizada = atualizarTarefas(nomeTarefaAlterar, novoNome);

      tarefaAtualizada
        ? console.log("Tarefa Atualizada!")
        : console.log("Tarefa Inválida!");
      break;

    case "3":
      let nomeTarefaDeletar = input
        .question("Nome da Tarefa para Deletar: ")
        .trim();
      let tarefaDeletada = deletarTarefa(nomeTarefaDeletar);

      tarefaDeletada[0]
        ? lista_tarefas.splice(tarefaDeletada[1], tarefaDeletada[1])
        : console.log("Tarefa Inválida!");
      tarefaDeletada[0] && console.log("Tarefa Deletada!");
      break;

    case "4":
      console.log(lista_tarefas);
      break;
    case "q":
      console.log("Exit\n");
      controle = false;
    default:
      console.log("Opção inválida, Digite novamente!\n");
      break;
  }
}
