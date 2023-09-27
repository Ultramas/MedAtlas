function navToggle(that){
    let navbar = that.parentNode
    navbar.classList.toggle('show')
}
window.onload = function() {
    var navbar = document.querySelector('.navbarx');
    if (navbar) {
        navbar.style.top = '0';
    } else {
        console.error('Navbar element with class "navbarx" not found.');
    }
};
