let container = document.querySelector(".container");
let btn = document.getElementById("spin");
let number = Math.ceil(Math.random() * 10000);

let options = document.querySelectorAll(".container div").length;
let degree = 360 / options;

for (let i = 0; i < options; i++) {
  document.querySelectorAll(".container div")[i].style.transform = `rotate(${degree * i}deg)`;
}

let nonce = Math.floor(Math.random() * 1000000);
let prize;

// Adjust the conditions to divide the nonce into equal ranges
for (let i = 0; i < options; i++) {
  if (nonce >= (1000000/options)*i && nonce < (1000000/options)*(i+1)) {
    prize = i+1;
  }
}

// Map the prizes to labels
let prizeToLabel = {
  1: 'a',
  2: 'b',
  3: 'c',
  4: 'd',
  5: 'e',
  6: 'f'
};

let prizeLabel = prizeToLabel[prize];

let flash = document.querySelector(".container div");

// Add a transitionend event listener to the container
container.addEventListener('transitionend', function() {
  // Enable the button when the spinning ends
  btn.disabled = false;
});

btn.onclick = function () {
  // Disable the button when it is clicked
  btn.disabled = true;

  container.style.transform = "rotate(" + number + "deg)";
  number += Math.ceil(Math.random() * 10000);
}
