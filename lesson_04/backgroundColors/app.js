const buttons = document.querySelectorAll('li');
const rand = document.querySelector('#random');
const arr = ['red', 'blue', 'green', 'yellow', 'orange'];

buttons.forEach(button => {
  button.addEventListener('click', function (e) {
    changeColor(e.target.classList[0]);
  });
});

function changeColor(cl) {
  if (cl == 'random') {
    cl = arr[Math.floor(Math.random() * (arr.length - 1)) + 1];
    rand.style.backgroundColor = `${cl}`;
  }
  document.querySelector('body').style.backgroundColor = `${cl}`;
}

// document.querySelector('#turnBlue').addEventListener('click', turnBlueFunction);
// document
//   .querySelector('#turnGreen')
//   .addEventListener('click', turnGreenFunction);
// document.querySelector('#turnRed').addEventListener('click', turnRedFunction);
// document
//   .querySelector('#turnYellow')
//   .addEventListener('click', turnYellowFunction);
// document
//   .querySelector('#turnOrange')
//   .addEventListener('click', turnOrangeFunction);
// document.querySelector('#random').addEventListener('click', randomFunction);

// function turnBlueFunction() {
//   document.querySelector('body').style.backgroundColor = 'skyblue';
// }

// function turnGreenFunction() {
//   document.querySelector('body').style.backgroundColor = 'green';
// }

// function turnRedFunction() {
//   document.querySelector('body').style.backgroundColor = 'red';
// }

// function turnYellowFunction() {
//   document.querySelector('body').style.backgroundColor = 'gold';
// }

// function turnOrangeFunction() {
//   document.querySelector('body').style.backgroundColor = 'orange';
// }

// function randomFunction() {
//   document.querySelector('body').style.backgroundColor = 'purple';
// }
