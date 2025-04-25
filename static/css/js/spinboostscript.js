document.addEventListener('DOMContentLoaded', function() {
    const spinOptions = [
        { value: 1, gradient: 'linear-gradient(to right, rgba(255, 255, 255, 0.3), rgba(192, 192, 192, 0.9))', flameColor: '#e5e5e5' },
        { value: 2, gradient: 'linear-gradient(to right, rgba(192, 192, 192, 0.5), rgba(24, 24, 226, 0.7))', flameColor: '#93c5fd' },
        { value: 3, gradient: 'linear-gradient(to right, rgba(24, 24, 226, 0.6), rgba(0, 255, 0, 0.7))', flameColor: '#86efac' },
        { value: 4, gradient: 'linear-gradient(to right, rgba(0, 255, 0, 0.6), rgba(255, 255, 0, 0.7))', flameColor: '#fde047' },
        { value: 5, gradient: 'linear-gradient(to right, rgba(255, 255, 0, 0.6), rgba(255, 0, 0, 0.7))', flameColor: '#fca5a5' },
        { value: 10, gradient: 'linear-gradient(to right, rgba(255, 0, 0, 0.6), rgba(0, 0, 0, 0.8))', flameColor: '#ef4444' }
    ];

    const selectionsDiv = document.querySelector('.selections');
    const buttons = document.querySelectorAll('.spin-option');
    const flameEffect = document.querySelector('.flame-effect');

    function updateBackground(gradient, flameColor) {
        selectionsDiv.style.background = gradient;
        document.documentElement.style.setProperty('--flame-color', flameColor);
    }

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const value = parseInt(this.dataset.value);
            const option = spinOptions.find(opt => opt.value === value);

            if (option) {
                updateBackground(option.gradient, option.flameColor);
                buttons.forEach(btn => btn.classList.remove('selected'));
                this.classList.add('selected');
            }
        });
    });

    updateBackground(spinOptions[0].gradient, spinOptions[0].flameColor);
    buttons[0].classList.add('selected');
});