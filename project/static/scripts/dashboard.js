const cards = document.querySelectorAll(".request-card");

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

cards.forEach(function (card) {
  card.addEventListener("click", function () {
    const cardId = card.getAttribute("id");

    openModal(cardId);
  });
});

const markAsPrintedButton = document.getElementById("modal-btn-printed");

if (markAsPrintedButton) {
  markAsPrintedButton.addEventListener("click", function () {
    closeModal();
  });
}
