const formURL = document.getElementById("form-url");
const inputURL = document.getElementById("input-url");

const trocarImg = (url) => {
  const imagens = document.querySelectorAll("img");
  imagens.forEach((image) => {
    image.src = url;
  });
};

formURL.addEventListener("submit", async (e) => {
  e.preventDefault();

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: trocarImg,
    args: [inputURL.value],
  });
});
