const addButton = document.querySelector('.add');
const inputText = document.querySelector('input');
const listContainer = document.querySelector('.container');
const deleteButton = document.querySelector('.delete');
addButton.addEventListener('click', createItem);
deleteButton.addEventListener('click', function (e) {
  console.log(e.target);
});

function createItem() {
  let text = inputText.value;

  console.log(text);
  const markup = `
 <div class="list-Item">
    <span>
        ${text}
    </span>
<button onclick = "myFunction()" class='delete'>${'delete'}</button>
 </div>
`;

  listContainer.insertAdjacentHTML('afterend', markup);
}

// function deleteItem(){

// };

document.addEventListener('DOMContentLoaded', Createtbl, false);

function myFunction() {
  console.log('Clicked');
  console.log();
}
