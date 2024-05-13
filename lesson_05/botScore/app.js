const buttons = document.querySelectorAll('button');
const localStorageValue = document.querySelector('.storage-value');
const resetButton = document.querySelector('.reset');

let getCount = localStorage.getItem('count');
console.log(`Local Storage Count: `, getCount);
let value = Number(getCount ? getCount : 0);
console.log(`Initial Value [${typeof value}]: `, value);
updateScreen(value);

buttons.forEach(button => {
  button.addEventListener('click', function (e) {
    let operator = e.target.classList[0];
    console.log(`Operator: `, operator);
    doCalculation(operator);
  });
});

resetButton.addEventListener('click', function () {
  console.log(`Inside resetButton Function:`);
  // localStorage.removeItem('count');
  value = 0;
  localStorage.setItem('count', value);
  getCount = localStorage.getItem('count');
  console.log(`\tLocal Storage Value after Reset: ${getCount}`);
  updateScreen(getCount);
});

function doCalculation(operator) {
  console.log(`Inside doCalculation Function:`);
  console.log(`Value variable when entering: ${value}`);
  operator == 'add' ? (value += 1) : (value -= 1);
  value < 0 ? setColor() : setColor(1);
  localStorage.setItem('count', value);
  getCount = localStorage.getItem('count');
  console.log(`\tLocal Storage Value after [${operator}]: ${getCount}`);
  updateScreen(getCount);
}

function updateScreen(getCount) {
  localStorageValue.innerText = getCount;
}

function setColor(pos = -1) {
  console.log(`In set Color`, pos);
  if (pos > 0) {
    console.log(`\tIn Pos`);
    localStorageValue.style.color = '#64ccc9';
  } else {
    localStorageValue.style.color = '#ee2737';
  }
}
