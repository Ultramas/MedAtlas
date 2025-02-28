$(document).ready(function () {
    let animationStopped = false;
    let selectedItems = [];
    let totalSpins = sessionStorage.getItem("totalSpins") || 1; // Retrieve stored spins, default to 1
    let currentSpin = 0;

    if (sessionStorage.getItem("startAnimation") === "true") {
        sessionStorage.removeItem("startAnimation");
        initializeAnimation();
    }

    $(".start").click(function () {
        totalSpins = parseInt($("#spinCount").val()); // Get selected number of spins
        sessionStorage.setItem("startAnimation", "true");
        sessionStorage.setItem("totalSpins", totalSpins); // Store spins in sessionStorage
        location.reload();
    });

    function initializeAnimation() {
        $(".start").prop('disabled', true);

        let randomizeFlag = true;

        function randomizeContents() {
            if (randomizeFlag) {
                $('#slider .cards').sort(() => 0.5 - Math.random()).appendTo('#slider');
            }
        }

        function addAnimation() {
            const scrollers = document.querySelectorAll('.slider');
            scrollers.forEach(scroller => {
                scroller.setAttribute('data-animated', 'true');
            });
        }

        function spin() {
            randomizeContents();
            addAnimation();

            setTimeout(() => {
                randomizeFlag = false;
            }, 9000);

            setTimeout(function () {
                const scrollers = document.querySelectorAll('.slider');
                scrollers.forEach(scroller => {
                    const computedStyle = window.getComputedStyle(scroller);
                    const matrix = computedStyle.getPropertyValue('transform');
                    scroller.style.transform = matrix;
                    scroller.style.animationPlayState = 'paused';
                });

                findSelectedCard();
                currentSpin++;

                if (currentSpin < totalSpins) {
                    randomizeFlag = true;
                    setTimeout(spin, 1000); // Delay between spins
                } else {
                    animationStopped = true;
                    showPopup();
                    sessionStorage.removeItem("totalSpins"); // Clear spins after completion
                }
            }, 9000);
        }

        spin();

        $('.close').click(function () {
            $('#popup').hide();
            $(".start").prop('disabled', false);
        });
    }

    function findSelectedCard() {
        const selector = document.getElementById('selector').getBoundingClientRect();
        let selectedPokemon = 'A New Pokemon!';

        document.querySelectorAll('.cards').forEach(card => {
            const cardRect = card.getBoundingClientRect();
            if (!(selector.right < cardRect.left ||
                  selector.left > cardRect.right ||
                  selector.bottom < cardRect.top ||
                  selector.top > cardRect.bottom)) {
                selectedPokemon = card.id;
                selectedItems.push(selectedPokemon);

                const cardImage = document.getElementById('cardImage');
                cardImage.src = `${selectedPokemon}.png`;
                cardImage.alt = selectedPokemon;
            }
        });
    }

    function showPopup() {
        const resultsContainer = document.createElement("div");
        selectedItems.forEach((item) => {
            const itemElement = document.createElement("p");
            const imgElement = document.createElement("img");
            imgElement.src = `${item}.png`;
            imgElement.alt = item;
            imgElement.style.width = "50px";
            imgElement.style.height = "auto";
            itemElement.textContent = item;
            itemElement.appendChild(imgElement);
            resultsContainer.appendChild(itemElement);
        });

        const popupContents = document.querySelector(".popup .text");
        popupContents.innerHTML = "<h1>Congratulations!</h1><h2>You got:</h2>";
        popupContents.appendChild(resultsContainer);

        $('#popup').show();
    }
});
