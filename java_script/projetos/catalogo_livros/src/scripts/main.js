// Buttons para add e buscar livro;
const buttonAdd = document.querySelector("#button-add");
const buttonBuscar = document.querySelector("#button-buscar");

// Catalogos onde os livros vão ser exibidos;
const catalogoLivros = document.querySelector(
  "#secao-catalogo-livros .resultados"
);
const catalogoBusca = document.querySelector(
  "#secao-buscar-livros .resultados"
);

/* 
  Inicializar a lista geral dos livros;

  Onde a lista é um Array de JSON's, cada livro
  é representado pelo objeto de notação, contendo:
   titulo, autor, genero, ano de publicacao e avaliacao;
*/
const listaLivros = [];

const exibirLivro = (livro, lista) => {
  /* 
    Função para exibir um novo livro adicionado;

    A função recebe o novo livro e o catalogo onde
    o livro deve ser exibido, podendo ser na section geral
    ou na section de buscas;
  */

  const li = document.createElement("li");

  li.textContent = `
  ${livro["titulo"]} por ${livro["autor"]} - 
  Gênero: ${livro["genero"]} 
  [Publicado em ${livro["anoPublicacao"]}] 
  [Avaliação: ${livro["avaliacao"]}]`;

  lista.appendChild(li);
};

const adicionarLivro = () => {
  /*
    Função para adicionar um novo livro na lista;

    A função adiciona e retorna um arquivo JSON 
    contendo todas as informações do novo livro;
  */
  const novoLivro = {
    titulo: document.getElementById("titulo").value.trim(),
    autor: document.getElementById("autor").value.trim(),
    genero: document.getElementById("genero").value.trim(),
    anoPublicacao: document.getElementById("ano-publicacao").value.trim(),
    avaliacao: document.getElementById("avaliacao").value.trim(),
  };

  listaLivros.push(JSON.stringify(novoLivro));
  return novoLivro;
};

const buscarLivros = (query) => {
  const resultado = listaLivros.filter((livro) => {
    return (
      livro.titulo.toLowerCase().includes(query.toLowerCase()) ||
      livro.autor.toLowerCase().includes(query.toLowerCase()) ||
      livro.genero.toLowerCase().includes(query.toLowerCase())
    );
  });
  return resultado;
};

buttonAdd.addEventListener("click", () => {
  const livro = adicionarLivro();
  exibirLivro(livro, catalogoLivros);
});

buttonBuscar.addEventListener("click", () => {
  const query = document.querySelector("#nome-livro").value;
  const resultado = buscarLivros(query);
  alert(resultado);
});
