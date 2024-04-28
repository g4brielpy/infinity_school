const buttonAdd = document.querySelector("#button-add");
const buttonBuscar = document.querySelector("#button-buscar");
const listaLivros = [];

const adicionarLivro = () => {
  const novoLivro = {
    titulo: document.getElementById("titulo").value,
    autor: document.getElementById("autor").value,
    genero: document.getElementById("genero").value,
    anoPublicacao: document.getElementById("ano-publicacao").value,
    avaliacao: document.getElementById("avaliacao").value,
  };

  listaLivros.push(JSON.stringify(novoLivro));
};

buttonAdd.addEventListener("click", () => {
  adicionarLivro();
});
