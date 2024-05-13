const image = document.querySelector('img');
const getPictureButton = document.querySelector('.get-picture');
const getListButton = document.querySelector('.get-list');
document.querySelector('#app').addEventListener('click', getPictureButton);
const list = document.querySelector('.list');
let dogBreeds;

getPictureButton.addEventListener('click', function () {
  fetch('https://dog.ceo/api/breeds/image/random')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data);
      image.src = data.message;
    })
    .catch(err => {
      console.log(`error ${err}`);
    });
});

getListButton.addEventListener('click', function () {
  fetch('https://dog.ceo/api/breeds/list/all')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      dogBreeds = data.message;
      console.log(dogBreeds);
      createList();
    })
    .catch(err => {
      console.log(`error ${err}`);
    });
});

function createList() {
  for (key in dogBreeds) {
    console.log(`Key: `, key);
    let li = document.createElement('li');
    li.innerText = key;
    list.appendChild(li);
  }
}
