// how to play
document.addEventListener('DOMContentLoaded', function() {
    const playBanner = document.getElementById('playBanner');
    const toggleButton = document.getElementById('togglePlayBanner');

    // Toggle banner when button is clicked
    toggleButton.addEventListener('click', function() {
        playBanner.classList.toggle('collapsed');

        // Store preference in localStorage
        if (playBanner.classList.contains('collapsed')) {
            localStorage.setItem('playBannerState', 'collapsed');
        } else {
            localStorage.setItem('playBannerState', 'expanded');
        }
    });

    // Check localStorage for returning users
    const savedState = localStorage.getItem('playBannerState');
    if (savedState) {
        if (savedState === 'collapsed') {
            playBanner.classList.add('collapsed');
        } else {
            playBanner.classList.remove('collapsed');
        }
    }
});