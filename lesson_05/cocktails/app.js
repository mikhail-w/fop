const searchInput = document.querySelector('input');
const button = document.querySelector('button');
const cocktailName = document.querySelector('h2');
const photo = document.querySelector('img');
const instructions = document.querySelector('h3');
let searchValue = '';
let imgSrc = '';
let inst = '';

searchInput.addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
    getResponse();
  }
});

button.addEventListener('click', function () {
  getResponse();
});

function getResponse() {
  searchValue = searchInput.value;
  console.log(searchValue);
  if (!searchValue) return;
  fetch(
    `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${searchValue}`
  )
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data);
      imgSrc = data.drinks[0].strDrinkThumb;
      inst = data.drinks[0].strInstructions;

      cocktailName.innerText = `Name: ${data.drinks[0].strDrink}`;

      setPhoto();
      setInstructions();
    })
    .catch(err => {
      console.log(`error ${err}`);
    });
}

function setName() {
  cocktailName.innerText = `Name: ${searchValue}`;
}

function setPhoto() {
  photo.src = imgSrc;
}

function setInstructions() {
  instructions.innerHTML = `
  <h3> Instructions </h3>
  <p>${inst}</p>
  `;
}
