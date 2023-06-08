// Get necessary DOM elements
const form = document.getElementById('add-item-form');
const input = document.getElementById('item-input');
const itemList = document.getElementById('item-list');

// Add event listener to the form submission
form.addEventListener('submit', (e) => {
  e.preventDefault(); // Prevent form submission

  const itemText = input.value.trim();
  if (itemText !== '') {
    // Create a new list item
    const listItem = document.createElement('li');
    listItem.className = 'item';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const itemTextSpan = document.createElement('span');
    itemTextSpan.textContent = itemText;

    listItem.appendChild(checkbox);
    listItem.appendChild(itemTextSpan);

    // Add event listener to the checkbox
    checkbox.addEventListener('change', () => {
      listItem.classList.toggle('done');
    });

    // Append the list item to the item list
    itemList.appendChild(listItem);

    // Clear the input field
    input.value = '';
  }
});
