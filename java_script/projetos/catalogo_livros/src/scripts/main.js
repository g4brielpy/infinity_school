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

  li.innerHTML = `
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
  /*
    Função para buscar livros pelo título, autor ou gênero

    A função recebe um parâmetro e faz a busca na lista de livros
    através do método 'filter', a cada iteração do método, o item
    é convertido do JSON para Objeto. É retornado um Array com 
    os resultados da busca.
  */
  const busca = listaLivros.filter((livro) => {
    livro = JSON.parse(livro);
    return (
      livro.titulo.toLowerCase().includes(query.toLowerCase()) ||
      livro.autor.toLowerCase().includes(query.toLowerCase()) ||
      livro.genero.toLowerCase().includes(query.toLowerCase())
    );
  });

  return busca;
};

document
  .getElementById("formulario-add-livro")
  .addEventListener("submit", (event) => {
    event.preventDefault();

    // Catalogos onde os livros vão ser exibidos;
    const catalogoLivros = document.querySelector(
      "#secao-catalogo-livros .resultados"
    );

    const livro = adicionarLivro();
    exibirLivro(livro, catalogoLivros);

    // Limpar inputs depois do envio do formulário;
    document.getElementById("formulario-add-livro").reset();
  });

document
  .getElementById("formulario-buscar-livro")
  .addEventListener("submit", (event) => {
    event.preventDefault();

    // Catalogos onde os livros vão ser exibidos;
    const catalogoBusca = document.querySelector(
      "#secao-buscar-livros .resultados"
    );

    const query = document.querySelector("#nome-livro").value;
    const resultado = buscarLivros(query);

    catalogoBusca.innerHTML = "";
    resultado.forEach((livro) => {
      livro = JSON.parse(livro);
      exibirLivro(livro, catalogoBusca);
    });

    // Limpar inputs depois do envio do formulário;
    document.getElementById("formulario-buscar-livro").reset();
  });
