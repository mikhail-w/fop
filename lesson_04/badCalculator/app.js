const numbers = document.querySelectorAll('.number');
const output = document.querySelector('#placeToPutResult');
const calculations = document.querySelectorAll('.symbol');
let total = 0;
let numberString = '';

console.log({ numbers });
console.log({ calculations });

calculations.forEach(calc => {
  calc.addEventListener('click', function (e) {});
  console.log(calc.innerText);
});

numbers.forEach(number => {
  number.addEventListener('click', function (e) {
    let num = e.target.innerText;
    // console.log(e.target.innerText);
    numberString += num;
    setOutput(e.target.innerText);
  });
});

function setOutput(val) {
  output.innerText = val;
  console.log(numberString);
}
