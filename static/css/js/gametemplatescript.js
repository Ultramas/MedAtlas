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

        // Call the create_outcome endpoint
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

            // Clear existing cards
            clearCards();

            const attributes = {
                id: data.choice_id || 'N/A',
                nonce: data.nonce || 'N/A',
                text: data.choice_text || 'Unknown',
                color: data.choice_color || '#FFFFFF',
                file: data.choice_file || null,
                value: data.choice_value || 0,
                lowerNonce: data.lower_nonce || 'N/A',
                upperNonce: data.upper_nonce || 'N/A',
            };

            // Create the target card
            const targetCardElement = document.createElement('div');
            targetCardElement.classList.add('card', 'target-card');
            targetCardElement.setAttribute('id', `card-${attributes.id}`);
            targetCardElement.setAttribute('data-nonce', attributes.nonce);
            targetCardElement.setAttribute('data-color', attributes.color);
            targetCardElement.setAttribute('data-choice_value', attributes.value);
            targetCardElement.setAttribute('data-lower_nonce', attributes.lowerNonce);
            targetCardElement.setAttribute('data-upper_nonce', attributes.upperNonce);

            targetCardElement.innerHTML = `
                <div class="lge" style="background-color: white;">
                    <div class="lootelement" style="background-color: ${attributes.color};  padding: 6%; margin-left: 22px; margin-top: 12px;">
                        ${attributes.file ? `<img src="${attributes.file}" alt="${attributes.text}" width="100" height="100">` : ''}
                    </div>
                </div>
                <h5>${attributes.value} 💎</h5>
                <p>${attributes.text}</p>
                <p>Nonce: ${attributes.nonce}</p>
            `;

            selectedItems.push({
                id: attributes.id,
                nonce: attributes.nonce,
                text: attributes.text,
                color: attributes.color,
                src: attributes.file,
                value: attributes.value,
                lowerNonce: attributes.lowerNonce,
                upperNonce: attributes.upperNonce
            });

            // Get the container of the cards
            const cardContainer = document.querySelector('.slider'); // Adjust selector if necessary

            // Calculate the position to insert: 4 cards to the right of the middle
            const middleIndex = Math.floor(cardContainer.children.length / 2);
            const targetIndex = Math.min(
                cardContainer.children.length,
                middleIndex + 3
            );

            if (cardContainer.children[targetIndex]) {
                cardContainer.insertBefore(targetCardElement, cardContainer.children[targetIndex]);
            } else {
                cardContainer.appendChild(targetCardElement);
            }

            // Adjust the slider to center the new card
            //centerCard(targetCardElement);

            console.log("Target card inserted 3 cards to the right of the middle.");

            // Call create_inventory_object after the card is created
            const inventoryPayload = {
                choice_id: data.choice_id,  // Use choice_id from outcome response
                choice_value: data.choice_value,  // Use choice_value
                category: 'example_category',  // Additional data as needed
                price: 100,
                condition: 'New',
                quantity: 1
            };
            console.log("Calling /create_inventory_object/ with payload:", inventoryPayload);

            const inventoryResponse = await fetch('/create_inventory_object/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}', // Ensure CSRF token is correctly passed
                },
                body: JSON.stringify(inventoryPayload),
            });

            const inventoryData = await inventoryResponse.json();
            console.log("Response from /create_inventory_object/:", inventoryData);

            if (inventoryData.status === 'success') {
                console.log("Inventory object created successfully.");
            } else {
                console.error("Failed to create inventory object:", inventoryData.message);
            }

            return data; // Return the data for further use
        } else {
            console.error(`Error: ${data.message}`);
            return null;
        }
    } catch (error) {
        console.error(`Request failed: ${error}`);
        return null;
    }
}


// Function to clear all cards
function clearCards() {
    const cardContainer = document.querySelector('.slider');
    const targetCards = cardContainer.querySelectorAll('.target-card');

    targetCards.forEach(card => cardContainer.removeChild(card));

    console.log("All target cards removed.");
}

// Function to center the card in the slider
function centerCard(cardElement) {
    const slider = document.getElementById('slider');
    const cardOffset = cardElement.offsetLeft;
    const sliderWidth = slider.offsetWidth;
    const cardWidth = cardElement.offsetWidth;

    // Adjust margin-left to center the card
    slider.scrollTo({
        left: cardOffset - sliderWidth / 2 + cardWidth / 2,
        behavior: 'smooth',
    });
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

    //slider.style.transform = `translateX(${currentTranslateX + offset}px)`;
    //console.log(`Slider adjusted by offset: ${offset}px`);
}





 function spin() {
    $(".spin-option").prop('disabled', true);

    randomizeContents();
    addAnimation();

    const animationDuration = isQuickSpin ? 4500 : 9000;
    const buffer = 150;
    const audiobuffer = 300;
    const audio = new Audio('/static/css/sounds/roulette_sound_effect.mp3');

audio.addEventListener('loadedmetadata', () => {
    // Calculate the adjusted duration
    const adjustedDuration = (animationDuration + audiobuffer) / 1000; // Convert ms to seconds
    const originalDuration = audio.duration;

    // Adjust playback rate if the original duration is available
    if (originalDuration) {
        audio.playbackRate = originalDuration / adjustedDuration;
    }

    // Play the audio
    audio.play().catch(error => console.error('Error playing audio:', error));
});

// Handle audio load errors
audio.addEventListener('error', (e) => {
    console.error('Audio failed to load:', e);
});

// Call this function when the spin ends
setTimeout(() => {

    const animationDuration = isQuickSpin ? 4500 : 9000;
    document.querySelectorAll('.slider').forEach(scroller => {
        scroller.style.animationPlayState = 'paused';
    });

    //findSelectedCard();
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
        cardElement.innerHTML = `
            <div class="card-fire" data-color="${item.color}">
                <div class="card-flames">
                    <div class="card-flame"></div>
                </div>
            </div>
            <p>ID: ${item.id}</p>
            <p>Nonceword: ${item.nonce}</p>
            <img src="${item.src || ''}" alt="${item.id}" width=150 height=225>
            <p>Value: ${item.value} 💎</p>
            <p>Lower Nonce: ${item.lowerNonce}</p>
            <p>Upper Nonce: ${item.upperNonce}</p>
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