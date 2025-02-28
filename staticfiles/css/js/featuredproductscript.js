let slideIndex = 1;
let slideIndex2 = 1;
const slides = document.getElementsByClassName("mySlidesesesesfade");
const dots = document.getElementsByClassName("dotttted");
const slides2 = document.getElementsByClassName("mySlides2");
const dots2 = document.getElementsByClassName("dot2");

showSlides(slideIndex);
showSlides2(slideIndex2);

// Automatic slideshow
let intervalID = setInterval(function() {
  plusSlides(1);
}, 5000);

// Automatic slideshow
let intervalID2 = setInterval(function() {
  plusSlides2(1);
}, 5000);

// Manual slideshow
function plusSlides(n) {
  clearInterval(intervalID);
  slideIndex += n;
  showSlides(slideIndex);
}

// Manual slideshow
function plusSlides2(n) {
  clearInterval(intervalID2);
  slideIndex2 += n;
  showSlides2(slideIndex2);
}

// Thumbnail image controls
function currentSlide(n) {
  clearInterval(intervalID);
  slideIndex = n;
  showSlides(slideIndex);
}

// Thumbnail image controls
function currentSlide2(n) {
  clearInterval(intervalID2);
  slideIndex2 = n;
  showSlides2(slideIndex2);
}

function showSlides(index) {
  let i;
  let currentSlideIndex = index || slideIndex;
  if (currentSlideIndex > slides.length - 3) {
    currentSlideIndex = 0;
  }
  if (currentSlideIndex < 0) {
    currentSlideIndex = slides.length - 3;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    slides[i].style.filter = "brightness(100%)"; // reset opacity for all slides
  }

  for (i = currentSlideIndex; i < currentSlideIndex + 3; i++) {
    slides[i].style.display = "block";
    if (i === currentSlideIndex) {
      slides[i + 2].style.filter = "brightness(50%)"; // reduce opacity for right slide
    } else if (i === currentSlideIndex + 2) {
      slides[i - 2].style.filter = "brightness(50%)"; // reduce opacity for left slide
    }
  }
}

function showSlides2(index) {
  let i;
  let currentSlideIndex = index || slideIndex2;
  if (currentSlideIndex > slides2.length - 3) {
    currentSlideIndex = 0;
  }
  if (currentSlideIndex < 0) {
    currentSlideIndex = slides2.length - 3;
  }
  for (i = 0; i < slides2.length; i++) {
    slides2[i].style.display = "none";
    slides2[i].style.filter = "brightness(100%)"; // reset opacity for all slides
  }

  for (i = currentSlideIndex; i < currentSlideIndex + 3; i++) {
    slides2[i].style.display = "block";
    if (i === currentSlideIndex) {
      slides2[i + 2].style.filter = "brightness(50%)"; // reduce opacity for right slide
    } else if (i === currentSlideIndex + 2) {
      slides2[i - 2].style.filter = "brightness(50%)"; // reduce opacity for left slide
    }
  }
}
