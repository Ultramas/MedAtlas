function navToggle(that){
    let navbar = that.parentNode
    navbar.classList.toggle('show')
}
window.onload = function() {
  var navbar = document.querySelector('.navbar');
  navbar.style.top = '0';
}