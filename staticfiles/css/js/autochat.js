document.addEventListener("DOMContentLoaded", function() {
  var chatIcon = document.querySelector(".chat-icon");
  var chatWindow = document.querySelector(".chat-window");
  var closeButton = document.querySelector(".close-button");

  chatIcon.addEventListener("click", function() {
    chatWindow.classList.toggle("open");
  });

  closeButton.addEventListener("click", function() {
    chatWindow.classList.remove("open");
  });
});
