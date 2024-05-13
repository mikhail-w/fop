document.querySelector('button').addEventListener('click', getFetch);
const nameText = document.querySelector('h2');
const image = document.querySelector('img');
const pokeType = document.querySelector('h3');
const shiny = document.getElementById('shiny');

async function getFetch() {
  const choice = document.querySelector('input').value.toLowerCase();
  const url = 'https://pokeapi.co/api/v2/pokemon/' + choice;

  let data = await fetch(url);
  let pokemonInfo = await data.json();

  console.log(pokemonInfo);
  console.log(pokemonInfo.types[0]['type']['name']);

  nameText.innerText = `Name: ${choice}`;

  if (shiny.checked) {
    console.log('Shiny Checked');
    image.src = `${pokemonInfo.sprites.front_shiny}`;
  } else {
    image.src = `${pokemonInfo.sprites.front_default}`;
  }

  pokeType.innerText = `Type: ${pokemonInfo.types[0]['type']['name']}`;
}
