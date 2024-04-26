// Armazena os livros em memória para começar
let books = [];

// Carrega os livros de um arquivo JSON (se existir)
function loadBooks() {
  const data = localStorage.getItem("books"); // LocalStorage como alternativa a um arquivo JSON
  if (data) {
    books = JSON.parse(data);
  }
}

// Salva os livros em um arquivo JSON (ou LocalStorage neste exemplo)
function saveBooks() {
  localStorage.setItem("books", JSON.stringify(books));
}

// Adiciona um novo livro ao catálogo
function addBook(book) {
  books.push(book);
  saveBooks();
  renderBookList();
}

// Exibe todos os livros no catálogo
function renderBookList() {
  const bookList = document.getElementById("book-list");
  bookList.innerHTML = "";
  books.forEach((book) => {
    const li = document.createElement("li");
    li.textContent = `${book.title} por ${book.author} - Gênero: ${
      book.genre
    } (Publicado em ${book.year}) - Avaliação: ${book.rating || "N/A"}`;
    bookList.appendChild(li);
  });
}

// Busca livros por título, autor ou gênero
function searchBooks(query) {
  const results = books.filter(
    (book) =>
      book.title.toLowerCase().includes(query.toLowerCase()) ||
      book.author.toLowerCase().includes(query.toLowerCase()) ||
      book.genre.toLowerCase().includes(query.toLowerCase())
  );
  return results;
}

// Renderiza os resultados da busca
function renderSearchResults(results) {
  const searchResults = document.getElementById("search-results");
  searchResults.innerHTML = "";
  results.forEach((book) => {
    const li = document.createElement("li");
    li.textContent = `${book.title} por ${book.author} - Gênero: ${
      book.genre
    } (Publicado em ${book.year}) - Avaliação: ${book.rating || "N/A"}`;
    searchResults.appendChild(li);
  });
}

// Classifica livros por diferentes critérios
function sortBooks(criterion) {
  if (criterion === "title") {
    books.sort((a, b) => a.title.localeCompare(b.title));
  } else if (criterion === "author") {
    books.sort((a, b) => a.author.localeCompare(b.author));
  } else if (criterion === "rating") {
    books.sort((a, b) => (a.rating || 0) - (b.rating || 0));
  }
  renderBookList();
}

// Eventos para adicionar livro
document.getElementById("add-book-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const book = {
    title: document.getElementById("title").value,
    author: document.getElementById("author").value,
    genre: document.getElementById("genre").value,
    year: parseInt(document.getElementById("year").value),
    rating: parseInt(document.getElementById("rating").value) || null,
  };
  addBook(book);
  e.target.reset();
});

// Eventos para buscar livros
document.getElementById("search-button").addEventListener("click", () => {
  const query = document.getElementById("search-query").value;
  const results = searchBooks(query);
  renderSearchResults(results);
});

// Eventos para classificar livros
document.getElementById("sort-books-section").addEventListener("click", (e) => {
  const sortCriterion = e.target.getAttribute("data-sort");
  if (sortCriterion) {
    sortBooks(sortCriterion);
  }
});

// Carrega os livros quando a página é carregada
window.addEventListener("load", () => {
  loadBooks();
  renderBookList();
});
