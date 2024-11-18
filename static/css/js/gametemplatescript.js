document.addEventListener('DOMContentLoaded', () => {
    const slider = document.getElementById('slider');
    const popup = document.getElementById('popup');
    const fire = popup.querySelector('.fire');
    const textContainer = popup.querySelector('.text');
    const persistSpinCheckbox = document.getElementById('persist-spin-checkbox');
    const quickSpinCheckbox = document.getElementById('quickspin-checkbox');
    const startButton = document.getElementById('start');

    let animationStopped = false;
    let selectedItems = [];
    let totalSpins = 1;
    let currentSpin = 0;

    const persistSpin = localStorage.getItem('persistSpinChecked') === 'true';
    const quickSpin = localStorage.getItem('quickSpinChecked') === 'true';

    // Initialize checkboxes from localStorage
    persistSpinCheckbox.checked = persistSpin;
    quickSpinCheckbox.checked = quickSpin;

    // Persist settings on checkbox change
    persistSpinCheckbox.addEventListener('change', () => {
        localStorage.setItem('persistSpinChecked', persistSpinCheckbox.checked.toString());
    });

    quickSpinCheckbox.addEventListener('change', () => {
        localStorage.setItem('quickSpinChecked', quickSpinCheckbox.checked.toString());
    });

    // Update total spins when a spin option is clicked
    document.querySelectorAll('.spin-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.spin-option').forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            totalSpins = parseInt(option.dataset.value);
            sessionStorage.setItem('totalSpins', totalSpins);
        });
    });

    // Start animation on button click
    startButton.addEventListener('click', () => {
        sessionStorage.setItem('startAnimation', 'true');
        sessionStorage.setItem('isQuickSpin', quickSpinCheckbox.checked);

        // Reset current spin count and initialize the animation
        currentSpin = 0;
        initializeAnimation();
    });

async function randomizeContents() {
    const gameId = startButton.getAttribute('data-game-id');
    const slug = startButton.getAttribute('data-slug');

    console.log("Game ID:", gameId);
    console.log("Slug:", slug);

    try {
        const payload = { game_id: gameId };
        console.log("Payload sent to server:", payload);

        const response = await fetch(`/create_outcome/${slug}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}', // Ensure CSRF token is included
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();
        console.log("Response from server:", data);

        if (data.status === 'success') {
            startButton.setAttribute('data-nonce', data.nonce);
            console.log(`Nonce updated: ${data.nonce}`);
            return data; // Return the entire data object
        } else {
            console.error(`Error: ${data.message}`);
            return null;
        }
    } catch (error) {
        console.error(`Request failed: ${error}`);
        return null;
    }
}



    function initializeAnimation() {
        startButton.disabled = true;
        const isQuickSpin = sessionStorage.getItem('isQuickSpin') === 'true';
        selectedItems = [];

        spin(isQuickSpin);
    }

function alignCardToSelector(card) {
    const slider = document.getElementById('slider');
    const sliderWidth = slider.offsetWidth; // Width of the slider container
    const cardWidth = card.offsetWidth; // Width of the card
    const cardPosition = card.offsetLeft; // Card's position relative to the slider

    // Calculate the target scroll position to center the card
    const targetPosition = cardPosition - (sliderWidth / 2) + (cardWidth / 2);
    console.log('targetPosition: ' + targetPosition)
    // Smoothly scroll the slider to the target position
    slider.scrollTo({
        left: targetPosition,
        behavior: 'smooth',
    });
    console.log('location set successfully ')
}

function spin() {
            $(".spin-option").prop('disabled', true);

            randomizeContents();
            addAnimation();

            const animationDuration = isQuickSpin ? 4500 : 9000;
            const buffer = 150; // Buffer to handle timing issues
            const audio = new Audio('/static/css/sounds/roulette_sound_effect.mp3');
            audio.play().catch(error => console.error('Error playing audio:', error));

            setTimeout(() => {
                // Pause animation after it completes
                document.querySelectorAll('.slider').forEach(scroller => {
                    scroller.style.animationPlayState = 'paused';
                });

                // Find the selected card
                findSelectedCard();
                currentSpin++;

                if (currentSpin < totalSpins) {
                    // Schedule the next spin
                    setTimeout(spin, buffer); // Add slight delay before calling spin again

                } else {
                    // Final spin logic
                    animationStopped = true;
                    setTimeout(buffer); // Add slight delay before calling spin again
                    showPopup();

                    if (!persistSpin) {
                        totalSpins = 1;
                        sessionStorage.setItem("totalSpins", totalSpins);
                    }

                    $(".start").prop('disabled', false);
                    $(".spin-option").prop('disabled', false);
                }
            }, animationDuration); // Align with animation duration
        }




        spin();
    }

    function addAnimation(isQuickSpin) {
        document.querySelectorAll('.slider').forEach(scroller => {
            scroller.style.animation = 'none';
            scroller.offsetHeight; // Trigger reflow
            let animationDuration = isQuickSpin ? '9s' : '18s';
            scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
            scroller.style.animationPlayState = 'running';
        });
    }


    function findSelectedCard() {
        const selector = document.getElementById('selector').getBoundingClientRect();
        let currentSelection = null;

        document.querySelectorAll('.card').forEach(card => {
            const cardRect = card.getBoundingClientRect();
            if (
                !(selector.right < cardRect.left ||
                  selector.left > cardRect.right ||
                  selector.bottom < cardRect.top ||
                  selector.top > cardRect.bottom)
            ) {
                currentSelection = {
                    id: card.id,
                    src: card.querySelector('img').src,
                    price: card.dataset.price,
                    color: card.dataset.color,
                    value: card.dataset.value
                };
            }
        });

        if (currentSelection) {
            selectedItems.push(currentSelection);
        }
    }

    function showPopup() {
        textContainer.innerHTML = `
            <h2>Congratulations!</h2>
            <p>You got:</p>
            <div class="cards-container"></div>
            <button class="close">Collect</button>
        `;

        const cardsContainer = textContainer.querySelector('.cards-container');
        selectedItems.forEach(item => {
            const cardElement = document.createElement('div');
            cardElement.classList.add('popup-card');
            cardElement.innerHTML = `
                <div class="card-fire" data-color="${item.color}">
                    <div class="card-flames">
                        <div class="card-flame"></div>
                    </div>
                </div>
                <p>ID: ${item.id}</p>
                <img src="${item.src}" alt="${item.id}">
                <p>Price: $${item.price}</p>
                <p>Value: ${item.value}</p>
            `;
            cardsContainer.appendChild(cardElement);
        });

        popup.style.display = 'block';
        fire.classList.add('active');

        popup.querySelector('.close').addEventListener('click', () => {
            fire.classList.remove('active');
            popup.style.display = 'none';
        });
    }
});
