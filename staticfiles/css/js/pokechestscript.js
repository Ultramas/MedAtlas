$(document).ready(function (){
// randomize
    $('div#slider').each(function(){

        var $div_parent = $(this);
        var $divsArr = $div_parent.children('div.cards');
        $divsArr.sort(function(a,b){
              var temp = parseInt( Math.random()*10 );
              var isOddOrEven = temp%2;
              var isPosOrNeg = temp>5 ? 1 : -1;
              return( isOddOrEven*isPosOrNeg );
        })
        .appendTo($div_parent);
  });


// slide
const scrollers= document.querySelectorAll('.slider');

if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
      addAnimation();
}

function addAnimation(){
      scrollers.forEach(scroller => {
          scroller.setAttribute('data-animated', true);
      });
};

const scrollerInner=document.querySelector('.slider');
const scrollerContent= Array.from(scrollerInner.children);

scrollerContent.forEach(item =>{
      const duplicatedItem= item.cloneNode(true);
      duplicatedItem.setAttribute('aria-hidden', true);
      scrollerInner.appendChild(duplicatedItem);
})

function stopAnimation() {
      scrollerInner.setAttribute('data-animated', 'slow');
  }

  // Call the function to stop the animation after a delay
  setTimeout(stopAnimation, 9000); // Stop the animation after 9 seconds


//   popupbox

  setTimeout(function() {
      popup.style.display = 'block';
    }, 10000);

    const closeButton = document.querySelector('.close');

    closeButton.addEventListener('click', function() {
      popup.style.display = 'none';
});


// yougot: indicator

const div1 = document.getElementById('Mewtwo');
const div2 = document.getElementById('Venusaur');
const div3 = document.getElementById('Charizard');
const div4 = document.getElementById('Blastoise');
const div5 = document.getElementById('selector');
let Touching = 'A Card';




function isTouching(element1, element2) {
      const rect1 = element1.getBoundingClientRect();
      const rect2 = element2.getBoundingClientRect();

      return !(
          rect1.right < rect2.left ||
          rect1.left > rect2.right ||
          rect1.bottom < rect2.top ||
          rect1.top > rect2.bottom
      );

  }


  if (isTouching(div5, div1)) {
      console.log('Mewtwo is selected');
      console.log('ID of Div 1:', div1.id);
      Touching='Mewtwo'
  } else {
      console.log('Mewtwo is not selected');
  };

  if (isTouching(div5, div2)) {
      console.log('Venusaur is selected');
      console.log('ID of Div 2:', div2.id);
      Touching='Venusaur'
  } else {
      console.log('Venusaur is not selected');};

if (isTouching(div5, div3)) {
      console.log('Charizard is selected');
      console.log('ID of Div 3:', div3.id);
      Touching='Charizard'
  } else {
      console.log('Charizard is not selected');};

if (isTouching(div5, div4)) {
      console.log('Blastoise is selected');
      console.log('ID of Div 4:', div4.id);
      Touching='Blastoise'
  } else {
      console.log('Blastoise is not selected');};

      document.getElementById('cardname').innerHTML = Touching;

});


