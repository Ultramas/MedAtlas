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

        function randomizeContents() {
            const startButton = document.getElementById("start");
            const gameId = startButton.getAttribute("data-game-id"); // Retrieve gameId
            const nonce = startButton.getAttribute("data-nonce"); // Retrieve nonce
            const slug = startButton.getAttribute("data-slug"); // Retrieve slug

            // Log the values for debugging
            console.log("Game ID:", gameId);
            console.log("Nonce:", nonce);
            console.log("Slug:", slug);
            $('#slider .cards').sort(() => 0.5 - Math.random()).appendTo('#slider');
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

        document.addEventListener("DOMContentLoaded", () => {
            const startButton = document.getElementById("start");

            // Add event listener to start button
            startButton.addEventListener("click", () => {
                // Start the spinning process
                spin();
            });
        });

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


    function findSelectedCard() {

                    const selector = document.getElementById('selector').getBoundingClientRect();
        let currentSelection = null;

        document.querySelectorAll('.cards').forEach(card => {
            const cardRect = card.getBoundingClientRect();

            // here, make sure the correct card to the nonce is landed on
            // Check if the card overlaps with the selector
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

        // Only add the current selection if it exists
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
