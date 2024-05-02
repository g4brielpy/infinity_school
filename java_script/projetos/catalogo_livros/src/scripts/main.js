/* 
  Inicializar a lista geral dos livros;

  Onde a lista é um Array de Object's, cada livro
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

    A função adiciona e retorna um arquivo Object 
    contendo todas as informações do novo livro;
  */
  const novoLivro = {
    titulo: document.getElementById("titulo").value.trim(),
    autor: document.getElementById("autor").value.trim(),
    genero: document.getElementById("genero").value.trim(),
    anoPublicacao: document.getElementById("ano-publicacao").value.trim(),
    avaliacao: Number(document.getElementById("avaliacao").value.trim()),
  };

  listaLivros.push(novoLivro);
  return novoLivro;
};

const buscarLivros = (query) => {
  /*
    Função para buscar livros pelo título, autor ou gênero

    A função recebe um parâmetro e faz a busca na lista de livros
    através do método 'filter'. É retornado um Array com 
    os resultados da busca.
  */
  const busca = listaLivros.filter((livro) => {
    return (
      livro.titulo.toLowerCase().includes(query.toLowerCase()) ||
      livro.autor.toLowerCase().includes(query.toLowerCase()) ||
      livro.genero.toLowerCase().includes(query.toLowerCase())
    );
  });

  return busca;
};

const classificarLivro = (campoOrdenar) => {
  listaLivros.sort((a, b) => {
    if (campoOrdenar == "avaliacao") {
      return a[campoOrdenar] - b[campoOrdenar];
    } else {
      return a[campoOrdenar]
        .toLowerCase()
        .localeCompare(b[campoOrdenar].toLowerCase());
    }
  });

  const catalogoLivros = document.querySelector(
    "#secao-catalogo-livros .resultados"
  );
  catalogoLivros.innerHTML = "";

  listaLivros.forEach((livro) => {
    exibirLivro(livro, catalogoLivros);
  });
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
    if (resultado.length > 0) {
      resultado.forEach((livro) => {
        exibirLivro(livro, catalogoBusca);
      });
    } else {
      const li = document.createElement("li");
      li.innerHTML = `Nenhum resultado encontrado com a busca "${query}"!`;
      li.style.listStyleType = "none";

      catalogoBusca.appendChild(li);
    }

    // Limpar inputs depois do envio do formulário;
    document.getElementById("formulario-buscar-livro").reset();
  });

document.querySelectorAll("#box-buttons .button").forEach((button) => {
  // iterar sobre essa lista de buttons e add um evento em cada um
  button.addEventListener("click", (event) => {
    event.preventDefault();

    const ordenar = button.getAttribute("data-ordenar");
    classificarLivro(ordenar);
  });
});
