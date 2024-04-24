{
  // Estrutura do quiz dentro do main#container-perguntas:
  /* <h2 id="pergunta">Qual é a camada mais externa da Terra?</h2>
      <ol id="lista-opcoes" type="A">
        <li class="opcao"><button>Crosta</button></li>
        <li class="opcao"><button>Manto</button></li>
        <li class="opcao"><button>Núcleo Externo</button></li>
        <li class="opcao"><button>Núcleo Interno</button></li>
      </ol> */
}

const tituloPergunta = document.querySelector("h2#pergunta");
const itensOpcoes = document.querySelectorAll("li.opcao button");
const buttonReload = document.querySelector("button#reload");
const resposta = document.querySelector("p#resposta");

const questoes = [
  {
    pergunta: "Qual é a camada mais externa da Terra?",
    opcoes: ["Crosta", "Manto", "Núcleo Externo", "Núcleo Interno"],
    resposta: "Crosta",
  },
  {
    pergunta: "Quem pintou o famoso quadro 'Mona Lisa'?",
    opcoes: [
      "Michelangelo",
      "Vincent van Gogh",
      "Leonardo da Vinci",
      "Claude Monet",
    ],
    resposta: "Leonardo da Vinci",
  },
  {
    pergunta: "Qual país é conhecido como 'terra do sol nascente'?",
    opcoes: ["China", "Japão", "Índia", "Coreia do Sul"],
    resposta: "Japão",
  },
  {
    pergunta:
      "Em que ano ocorreu a primeira viagem à Lua pela missão Apollo 11?",
    opcoes: ["1965", "1969", "1972", "1975"],
    resposta: "1969",
  },
];

const exibirResultado = (opcaoEscolhida, respostaCorreta) => {
  if (opcaoEscolhida == respostaCorreta) {
    resposta.innerHTML = "Acertou!!!";
  } else {
    resposta.innerHTML = "Errou, reposta correta é: " + respostaCorreta;
  }
  resposta.style.display = "block";
};

const gerarQuestionario = (titulo, opcoes, resposta) => {
  tituloPergunta.innerHTML = titulo;

  opcoes.forEach((opcao, index) => {
    itensOpcoes[index].textContent = opcao;

    itensOpcoes[index].addEventListener("click", () => {
      exibirResultado(opcao, resposta);
    });
  });
};

const getQuestao = () => {
  const index = Math.floor(Math.random() * questoes.length);

  const tituloQuestao = questoes[index].pergunta;
  const opcoes = questoes[index].opcoes;
  const respostaCorreta = questoes[index].resposta;

  gerarQuestionario(tituloQuestao, opcoes, respostaCorreta);
};

getQuestao();
buttonReload.addEventListener("click", () => {
  location.reload();
});
