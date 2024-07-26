document.addEventListener("DOMContentLoaded", () => {
  const openModalButtons = document.querySelectorAll(".open-button");
  const closeModalButtons = document.querySelectorAll(".close-button");
  const modals = document.querySelectorAll(".modal");

  openModalButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      console.log("Open modal button clicked!", index);
      console.log("Modal to be opened:", modals[index]);
      if (modals[index]) {
        modals[index].showModal();
        modals[index].style.display = "block"; // displaying modal
      } else {
        console.error("Modal not found for index:", index);
      }
    });
  });

  closeModalButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      console.log("Close modal button clicked!", index);
      if (modals[index]) {
        modals[index].close();
        modals[index].style.display = "none"; // Hiding modal
      } else {
        console.error("Modal not found for index:", index);
      }
    });
  });

  
  // Message/Notification timer
  const message_timeout = document.getElementById("message-timer");
  if (message_timeout) {
    setTimeout(function() {
      message_timeout.style.display = "none";
    }, 3000);
  } else {
    console.error("Message timer element not found!");
  }
});
