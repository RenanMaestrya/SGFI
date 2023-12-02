// You might also want to handle the "marcar como impresso" button here
const cards = document.querySelectorAll(".request-card");

// Function to open the modal for a specific card
function openModal(cardId) {
  const modal = document.querySelector(`#modal-${cardId}`);
  const closeButton = modal.querySelector(`.modal-btn-close`);
  modal.style.display = "flex";

  closeButton.addEventListener("click", function () {
    closeModal(modal);
  });
}

function closeModal(modal) {
  modal.style.display = "none";
}

// Attach click event listener to each card
cards.forEach(function (card) {
  card.addEventListener("click", function () {
    const cardId = card.getAttribute("id");

    openModal(cardId);
  });
});

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
