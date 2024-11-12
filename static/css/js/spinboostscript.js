document.addEventListener('DOMContentLoaded', function() {
    const spinOptions = [
        { value: 1, gradient: 'linear-gradient(to right, white, silver)', flameColor: '#e5e5e5' },
        { value: 2, gradient: 'linear-gradient(to right, silver, blue)', flameColor: '#93c5fd' },
        { value: 3, gradient: 'linear-gradient(to right, blue, green)', flameColor: '#86efac' },
        { value: 4, gradient: 'linear-gradient(to right, green, yellow)', flameColor: '#fde047' },
        { value: 5, gradient: 'linear-gradient(to right, yellow, red)', flameColor: '#fca5a5' },
        { value: 10, gradient: 'linear-gradient(to right, red, black)', flameColor: '#ef4444' }
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

    // Initialize with the first option
    updateBackground(spinOptions[0].gradient, spinOptions[0].flameColor);
    buttons[0].classList.add('selected');
});