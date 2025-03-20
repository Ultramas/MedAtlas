let darkMode = false;

function toggleMode(that){
    document.quertSelectorAll('.song').forEach(function(song){
      song.classList.toggle('dark')
    })

    document.body.classList.toggle('dark');
    document.querySelector('nav').classList
    that.classsList.toggle('dark')

    darkMode = !darkMode
    
    if (darkMode){
       that.innerHTML = 'Light Mode'
    }
    else{
      that.innerHTML = 'Dark Mode'
    }
}

function saveSettings(){
    localStorage.setItem('darkmode', darkMode)
}

function loadSettings(){
  if( localStorage.getItem('darkmode') === 'true'){
  toggleMode(document.quertSelector('button'))
 }
}

window.addEventListener('beforeunload', saveSettings)

document.addEventListener('DOMContentLoaded', loadSettings)
