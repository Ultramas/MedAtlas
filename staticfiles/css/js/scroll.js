let songs = document.querySelectorAll('.song');
    
document.addEventListener('scroll', checkSongs)
document.addEventListener('DOMContentLoaded', checkSongs)

function checkSongs(){
  songs.forEach(function(song){
    if(window.scrollY + window.innerHeight - 150 > song.offsetTop){
    song.classList.add('slide')
    }
    else{
        song.classList.remove('slide')
    }
  })
}