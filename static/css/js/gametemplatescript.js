document.addEventListener('DOMContentLoaded', () => {
    const slider = document.getElementById('slider');
    const popup = document.getElementById('popup');
    const closeButton = popup.querySelector('.close');
    const fire = popup.querySelector('.fire');
    const textContainer = popup.querySelector('.text');

    let animationStopped = false;
    let selectedItems = [];
    let totalSpins = 1;
    let currentSpin = 0;

    const persistSpin = localStorage.getItem('persistSpinChecked') === 'true';
    const quickSpin = localStorage.getItem('quickSpinChecked') === 'true';

    // Persist settings on checkbox change
    $('#persist-spin-checkbox').change(function () {
        localStorage.setItem('persistSpinChecked', $(this).prop('checked').toString());
    });

    $('#quickspin-checkbox').change(function () {
        localStorage.setItem('quickSpinChecked', $(this).prop('checked').toString());
    });

    // Update total spins when a spin option is clicked
    $(".spin-option").click(function () {
        $(".spin-option").removeClass("selected");
        $(this).addClass("selected");
        totalSpins = parseInt($(this).data("value"));
        sessionStorage.setItem("totalSpins", totalSpins);
    });

    // Start animation on button click
    $(".start").click(function () {
        sessionStorage.setItem("startAnimation", "true");
        sessionStorage.setItem("isQuickSpin", $("#quickspin-checkbox").is(":checked"));

        // Reset current spin count and initialize the animation
        currentSpin = 0;
        initializeAnimation();
    });

    function initializeAnimation() {
        $(".start").prop('disabled', true);
        const isQuickSpin = sessionStorage.getItem("isQuickSpin") === "true";
        selectedItems = [];

 async function randomizeContents() {
    const startButton = document.getElementById("start");
    const gameId = startButton.getAttribute("data-game-id");
    const nonce = startButton.getAttribute("data-nonce");
    const slug = startButton.getAttribute("data-slug");

    console.log("Game ID:", gameId);
    console.log("Nonce:", nonce);
    console.log("Slug:", slug);

    try {
        const payload = { game_id: gameId };
        console.log("Payload sent to server:", payload);

        const response = await fetch(`/create_outcome/${slug}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();
        console.log("Response from server:", data);

        if (data.status === 'success') {
            startButton.setAttribute('data-nonce', data.nonce);
            console.log(`Nonce updated: ${data.nonce}`);

            // Create the target card
            const attributes = {
                id: data.choice_id,
                nonce: data.nonce,
                text: data.choice_text,
                color: data.choice_color,
                file: data.choice_file,
            };

            const targetCardElement = document.createElement('div');
            targetCardElement.classList.add('card', 'target-card'); // Add a class to distinguish the target card
            targetCardElement.setAttribute('id', `card-${attributes.id}`);
            targetCardElement.setAttribute('data-nonce', attributes.nonce);
            targetCardElement.setAttribute('data-color', attributes.color);

            targetCardElement.innerHTML = `
                <div class="card-content" style="background-color: ${attributes.color}">
                    <p>Nonce: ${attributes.nonce}</p>
                    <p>${attributes.text}</p>
                    ${attributes.file ? `<img src="${attributes.file}" alt="${attributes.text}">` : ''}
                </div>
            `;

            const slider = document.getElementById('slider');
            slider.appendChild(targetCardElement); // Append the card to the slider

            // Immediately center the card after appending it
            alignCardWithSpinner();

            //make sure instead of the end, it gets put in the middle
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


        function addAnimation() {
            document.querySelectorAll('.slider').forEach(scroller => {
                scroller.style.animation = 'none';
                scroller.offsetHeight;  // Trigger reflow
                let animationDuration = isQuickSpin ? '9s' : '18s';
                scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
                scroller.style.animationPlayState = 'running';
            });
        }

function alignCardWithSpinner() {
    const spinnerTick = document.getElementById('selector'); // The spinner tick element
    const slider = document.getElementById('slider');
    const targetCard = document.querySelector('.target-card'); // The new card to align

    if (!targetCard || !spinnerTick) {
        console.error('Target card or spinner tick not found!');
        return;
    }

    // Get the center position of the spinner tick
    const spinnerTickRect = spinnerTick.getBoundingClientRect();
    const spinnerTickCenter = spinnerTickRect.left + spinnerTickRect.width / 2;

    // Get the center position of the target card
    const targetCardRect = targetCard.getBoundingClientRect();
    const targetCardCenter = targetCardRect.left + targetCardRect.width / 2;

    // Calculate the offset needed to align the card with the spinner tick
    const offset = spinnerTickCenter - targetCardCenter;

    // Update the slider's translateX value
    const currentTransform = getComputedStyle(slider).transform;
    const matrix = new DOMMatrix(currentTransform); // Use DOMMatrix for robust transformation parsing
    const currentTranslateX = matrix.m41 || 0;

    slider.style.transform = `translateX(${currentTranslateX + offset}px)`;
    console.log(`Slider adjusted by offset: ${offset}px`);
}





 function spin() {
    $(".spin-option").prop('disabled', true);

    randomizeContents();
    addAnimation();

    const animationDuration = isQuickSpin ? 4500 : 9000;
    const buffer = 150;
    const audio = new Audio('/static/css/sounds/roulette_sound_effect.mp3');
    audio.play().catch(error => console.error('Error playing audio:', error));

// Call this function when the spin ends
setTimeout(() => {

    const animationDuration = isQuickSpin ? 4500 : 9000;
    document.querySelectorAll('.slider').forEach(scroller => {
        scroller.style.animationPlayState = 'paused';
    });

    findSelectedCard();
    currentSpin++;

    if (currentSpin < totalSpins) {
        setTimeout(spin, buffer); // Queue the next spin
    } else {
        animationStopped = true; // Spin has ended
        showPopup();
        $(".start").prop('disabled', false);
        $(".spin-option").prop('disabled', false);
    }
}, animationDuration);
}
   spin();
    }


function findSelectedCard() {
    const selector = document.getElementById('selector').getBoundingClientRect();
    let currentSelection = null;

    document.querySelectorAll('.cards').forEach(card => {
        const cardRect = card.getBoundingClientRect();

        if (
            !(selector.right < cardRect.left ||
              selector.left > cardRect.right ||
              selector.bottom < cardRect.top ||
              selector.top > cardRect.bottom)
        ) {
            currentSelection = {
                id: card.id,
                src: card.querySelector('img')?.src || '',
                price: card.dataset.price,
                color: card.dataset.color,
                value: card.dataset.value,
                text: card.dataset.text, // Include additional data like text
            };

            // Highlight the target card specifically
            if (card.classList.contains('target-card')) {
                card.classList.add('highlight'); // Apply a class for visual indication
                console.log('Target card landed:', currentSelection);
            }
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
        selectedItems.forEach((item, index) => {
            const cardElement = document.createElement('div');
            cardElement.classList.add('popup-card');
            cardElement.innerHTML = `
                <div class="card-fire" data-color="${item.color}">
                    <div class="card-flames">
                        <div class="card-flame"></div>
                    </div>
                </div>
                <p>ID: ${item.id}</p>
                <p>Nonce: ${item.nonce}</p>
                <img src="${item.src}" alt="${item.id}">
                <p>Price: $${item.price}</p>
                <p>Value: ${item.value}</p> <!-- Display the value field here -->
            `;

            cardsContainer.appendChild(cardElement);

            if (index === 0) {
                const fire = document.querySelector('.fire');
                fire.setAttribute('data-color', item.color);
            }
        });

        popup.style.display = 'block';

        // Trigger the fire animation
        setTimeout(() => {
            const fire = document.querySelector('.fire');
            fire.classList.add('active');
        }, 100);

        const closeBtn = textContainer.querySelector('.close');
        closeBtn.addEventListener('click', () => {
            const fire = document.querySelector('.fire');
            fire.style.opacity = '0';
            document.querySelectorAll('.card-fire').forEach(fire => {
                fire.style.opacity = '0';
            });

            setTimeout(() => {
                popup.style.display = 'none';
            }, 500);

            $(".spin-option").prop('disabled', false);
            $(".start").prop('disabled', false);

            if (!persistSpin) {
                totalSpins = 1;
                sessionStorage.setItem("totalSpins", totalSpins);
                $(".spin-option").removeClass("selected");
                $(".spin-option[data-value='1']").addClass("selected");
            }
        });
    }
});