// Function to open the modal
function openModal() {
  const modal = document.querySelector(".modal");
  modal.setAttribute("origin", "{% origin %}");
  modal.style.display = "flex";
}

// Function to close the modal
function closeModal() {
  const modal = document.querySelector(".modal");
  modal.style.display = "none";
}

// Add click event listeners to your card elements
const cardElements = document.querySelectorAll(".request-card"); // Replace with the actual class of your card elements

cardElements.forEach(function (card) {
  card.addEventListener("click", function () {
    openModal();
  });
});

// Close the modal when the close button is clicked
const closeButton = document.getElementById("modal-btn-close"); // Replace with the actual ID of your modal's close button

if (closeButton) {
  closeButton.addEventListener("click", function () {
    closeModal();
  });
}

// You might also want to handle the "marcar como impresso" button here
const markAsPrintedButton = document.getElementById("modal-btn-printed"); // Replace with the actual ID of your button

if (markAsPrintedButton) {
  markAsPrintedButton.addEventListener("click", function () {
    closeModal();
  });
}

// Function to open the "Cadastrar novo aviso" modal
function openNewAlertModal() {
  // Update the modal origin to 'new_alert'
  const modal = document.querySelector(".modal-alert");
  modal.style.display = "flex";
}

// Add a click event listener to the "Cadastrar novo aviso" button
const openNewAlertButton = document.getElementById("openNewAlertModal");

if (openNewAlertButton) {
  openNewAlertButton.addEventListener("click", function () {
    openNewAlertModal();
  });
}
