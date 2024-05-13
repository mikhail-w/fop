document.querySelector('#check').addEventListener('click', checkDay);
const result = document.querySelector('#placeToSee');
const daysOfWeek = [
  'sunday',
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday',
  'saturday',
];

function checkDay() {
  const day = document.querySelector('#day').value.toLowerCase();
  console.log(day);
  // logic goes here
  if (daysOfWeek.includes(day)) {
    if (day == daysOfWeek[0] || day == daysOfWeek[6]) {
      result.innerHTML = `<h2>${'weekend'}</h2>`;
    } else {
      result.innerHTML = `<h2>${' weekday'}</h2>`;
    }
  } else {
    result.innerHTML = `<h2>${'incorrect day of the week'}</h2>`;
  }
}
