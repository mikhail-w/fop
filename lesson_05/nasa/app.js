const button = document.querySelector('button');
const image = document.querySelector('.image');
const text = document.querySelector('.container__explanation');
button.addEventListener('click', getImage);

function getImage() {
  let myDate = document.querySelector('.date').value;
  // console.log(myDate);
  fetch(
    `https://api.nasa.gov/planetary/apod?api_key=H8eVHDiMymCM9Y2d1ZCED1VvnZgLvFN4Lzwy64Rm&date=${myDate}`
  )
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data);
      console.log(data['url']);
      image.src = data['url'];
      text.innerHTML = `<p>${data['explanation']}</p>`;
    })
    .catch(err => {
      console.log(`error ${err}`);
    });
}
