const characterId = document.getElementById("characterId");
const btnGo = document.getElementById("btnGo");
const content = document.getElementById("content");
const img = document.getElementById("img");
const btnReset = document.getElementById("btnReset");


const fetchApi = (value) => {
  const resultado = fetch(`https://rickandmortyapi.com/api/character/${value}`)
    .then((response) => response.json())
    .then((data) => {
      // console.log(data, "console de data");
      return data;
    });
  console.log(resultado, "console de resultado");
  return resultado;
};

btnGo.addEventListener("click", async (event) => {
  event.preventDefault();
  if (characterId.value === "") {
    return (content.textContent = "É necessário fazer um filtro!");
  } else {
    const result = await fetchApi(characterId.value);
    content.textContent = `${JSON.stringify(result.name, undefined, 4)}`;
    img.src = `${result.image}`;
  }
});

btnReset.addEventListener("click", () => location.reload());
