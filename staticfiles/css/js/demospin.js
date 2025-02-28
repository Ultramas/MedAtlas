


document.addEventListener("DOMContentLoaded", function () {
    const spinButtons = document.querySelectorAll(".spin-option");
    const baseCostElement = document.getElementById("base-cost");
    const costDisplayElement = document.getElementById("cost-display");

    // Parse the base cost as a number (default to 0 if not a number)
    const baseCost = parseFloat(baseCostElement.textContent) || 0;

    spinButtons.forEach(button => {
        button.addEventListener("click", function () {
            const spinMultiplier = parseInt(this.dataset.value, 10); // Get the spin multiplier
            const totalCost = baseCost * spinMultiplier; // Calculate the total cost
            costDisplayElement.innerHTML = `<span id="base-cost">${totalCost}</span> 💎`; // Update the display
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    let selectedMultiplier = 1; // Default multiplier

    // Add event listener to each spin-option button
    document.querySelectorAll(".spin-option").forEach(button => {
        button.addEventListener("click", function () {
            selectedMultiplier = parseInt(this.getAttribute("data-value"));
            console.log("Selected multiplier:", selectedMultiplier); // For debugging
        });
    });

    // Add event listener to the spin button
    document.getElementById("start2").addEventListener("click", function () {
        console.log("Spin button clicked!"); // Debug log

        const button = this;
        const gameId = button.getAttribute("data-game-id");
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Fetch CSRF token

        console.log("Game ID:", gameId); // Debug log
        console.log("CSRF Token:", csrfToken); // Debug log
        console.log("Spin Multiplier:", selectedMultiplier); // Debug log

        // Perform the fetch request to initiate the spin
        fetch("{% url 'showcase:spin_game' %}", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify({
                game_id: gameId,
                spin_multiplier: selectedMultiplier
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Response data:", data); // Debug log
            //if box is not daily
            if (data.success) {
                // Update the currency amount automatically
                const currencyElement = document.getElementById("currency-amount");
                if (currencyElement) {
                    currencyElement.innerText = `${data.updated_currency_amount} ${data.currency_name}`;
                }
                // Optionally, display a success message
                console.log("Spin successful:", data.message);
            } else {
                alert(data.error); // Show error message if the spin fails
            }
        })
        .catch(error => {
            console.error("Error during fetch:", error); // Log any fetch errors
        });
    });
});



<script type="text/javascript">
$(document).ready(function() {
    console.log("jQuery is loaded.");

    let spinMultiplier = 1; // Default to 1 spin if no option is selected

    // Set spin multiplier based on selected option
    $('.spin-option').on('click', function() {
        $('.spin-option').removeClass('selected');
        $(this).addClass('selected');
        spinMultiplier = parseInt($(this).data('value'));
        console.log("Spin multiplier selected:", spinMultiplier);
    });

    $('#start2').on('click', function() {
        const gameId = $(this).data('game-id');
        const slug = $(this).data('slug');
        const csrfToken = '{{ csrf_token }}';
        const url = '{% url "showcase:create_outcome" "SLUG_PLACEHOLDER" %}'.replace('SLUG_PLACEHOLDER', slug);

        let completedSpins = 0;
        let allChoices = [];

        // Check if Quick Spin is active
        const isQuickSpin = $('#quickspin-checkbox').is(':checked');
        console.log("Quick Spin mode:", isQuickSpin);

        for (let i = 0; i < spinMultiplier; i++) {
            $.ajax({
                type: 'POST',
                url: url,
                data: {
                    csrfmiddlewaretoken: csrfToken,
                    game_id: gameId,
                    console.log('the game id is ', game_id);
                },
                success: function(response) {
                    if (response.status === 'success') {
                        completedSpins++;
                        allChoices = allChoices.concat(response.choices);
                        console.log('Choice received successfully for spin', i + 1);

                        // Update the UI only after all spins are completed
                        if (completedSpins === spinMultiplier) {
                            console.log('All spins completed.');
                            //updateWheelContents(allChoices); // Display all outcomes at once
                            initializeAnimation(response.nonce, isQuickSpin); // Pass Quick Spin mode to the animation
                        }
                    } else {
                        console.error(response.message);
                    }
                },
                error: function(error) {
                    console.error('Error during spin', i + 1, ':', error);
                }
            });
        }
    });

    function initializeAnimation(targetNonce, isQuickSpin) {
        // Disable the spin button to avoid multiple clicks
        $(".start2").prop('disabled', true);

        function addAnimation() {
            document.querySelectorAll('.slider').forEach(scroller => {
                scroller.style.animation = 'none';
                scroller.offsetHeight;
                const animationDuration = isQuickSpin ? '9s' : '18s'; // Adjust duration based on Quick Spin
                scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
                scroller.style.animationPlayState = 'running';
            });
        }

        function stopAtSelectedCard() {
            document.querySelectorAll('.cards').forEach(card => {
                const cardNonce = card.getAttribute('data-nonce');

                // Highlight and position the card with matching nonce
                if (cardNonce === targetNonce) {
                    $(card).addClass('highlighted');
                    card.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
                } else {
                    $(card).removeClass('highlighted');
                }
            });

            // Enable the button after animation ends
            $(".start2").prop('disabled', false);
        }

        // Start2 spinning
        addAnimation();

        // Stop the animation after a delay
        setTimeout(() => {
            document.querySelectorAll('.slider').forEach(scroller => {
                scroller.style.animationPlayState = 'paused';
            });

            // Find and stop at the selected card
            stopAtSelectedCard();
        }, isQuickSpin ? 4500 : 9000);  // Adjust time based on Quick Spin setting
    }
});

    const choicesWithNonce = {{ choices_with_nonce|safe }};



function createOutcome(gameId, slug) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch(`/create_outcome/${slug}/`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,  // Ensure csrf token is being sent
    },
    body: JSON.stringify({
        game_id: gameId,  // Pass the game_id as needed
        other_data: otherData,  // Add any additional data as needed
    })
})
}
.then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            const choiceFile = data.choice_file;

            if (choiceFile) {
                const slider = document.querySelector('.slider'); // Adjust selector as needed
                const newCard = document.createElement('div');
                newCard.className = 'cards';
                newCard.innerHTML = `
                    <div class="lootelement"
                         data-price="100"
                         data-nonce="${data.nonce}"
                         style="background: url('${choiceFile}'); padding: 6%; margin-left: 22px;">
                        <p><img src="${choiceFile}" alt="Generated Card"></p>
                    </div>
                    <h2 style="margin-left: 22px;">100 💎</h2>
                    <p>Nonce: ${data.nonce}</p>
                `;
                slider.appendChild(newCard);
            }
        } else {
            console.error('Error:', data.message);
        }
    })
    .catch(error => console.error('Fetch error:', error));


$(".start2").click(function () {
    const button = $(this);
    button.prop('disabled', true); // Disable the button when clicked

    // Step 1: Create the outcome and get the relevant choice
   createOutcome(button.data('game-id'), button.data('slug'))
    .then(data => {
        if (data.status === 'success') {
            const choice = {
                id: data.choice_id,
                choice_text: data.choice_text,
                color: data.choice_color,
                file: data.choice_file,
                value: data.choice_value || 0,
                lowerNonce: data.lower_nonce || 'N/A',
                upperNonce: data.upper_nonce || 'N/A',
            };

            // Log the choice object to verify its structure
            console.log('Choice Object:', choice);

            renderChoiceDetails(choice);

            // Other code to handle the outcome...
        } else {
            console.error('Error:', data.message);
            button.prop('disabled', false); // Re-enable the button if there's an error
        }
    })
    .catch(error => {
        console.error('Error:', error);
        button.prop('disabled', false); // Re-enable the button if there's an error
    });

                // Log the values to ensure they are correct
                console.log('Nonce:', chosenNonce);
                console.log('Choice ID:', choiceId);
                console.log('Choice Text:', choiceText);
                console.log('Choice Color:', choiceColor);
                console.log('Choice File:', choiceFile);

                // Step 2: Set the animation to randomize the cards
                let randomizeFlag = true;

                function randomizeContents() {
                    if (randomizeFlag) {
                        $('div#slider').each(function () {
                            var $div_parent = $(this);
                            var $divsArr = $div_parent.children('div.cards');
                            $divsArr.sort(function (a, b) {
                                var temp = parseInt(Math.random() * 10);
                                var isOddOrEven = temp % 2;
                                var isPosOrNeg = temp > 5 ? 1 : -1;
                                return (isOddOrEven * isPosOrNeg);
                            }).appendTo($div_parent);
                        });
                        setTimeout(randomizeContents, 2000);
                    }
                }

                randomizeContents();

                setTimeout(() => {
                    randomizeFlag = false;

                    // Step 3: Control the final stop based on the nonce or choiceId
                    const slider = document.querySelector('.slider');
                    const cards = slider.querySelectorAll('.card');

                    // Calculate the position to center the chosen card
                    let targetCard = null;
                    cards.forEach(card => {
                        if (parseInt(card.dataset.choiceId) === choiceId) {
                            targetCard = card;
                        }
                    });

                    if (targetCard) {
                        const targetOffsetLeft = targetCard.offsetLeft;
                        const sliderWidth = slider.offsetWidth;
                        const cardWidth = targetCard.offsetWidth;
                        const targetScrollPosition = targetOffsetLeft - (sliderWidth / 2) + (cardWidth / 2);

                        slider.scrollTo({
                            left: targetScrollPosition,
                            behavior: 'smooth'
                        });

                        // Assuming 'choice' is an object you receive via AJAX or another method
                        function renderChoiceDetails(choice) {
                            document.getElementById('choice-id').innerText = `Selected Choice ID: ${choice.id || 'N/A'}`;
                            document.getElementById('choice-text').innerText = `Selected Choice Text: ${choice.choice_text || 'N/A'}`;
                            document.getElementById('choice-color').innerText = `Selected Choice Color: ${choice.color || 'N/A'}`;

                            // Handle the file field
                            const choiceFileElement = document.getElementById('choice-file');
                            if (choice.file) {
                                choiceFileElement.src = choice.file; // Assuming file is a URL
                                choiceFileElement.style.display = 'block'; // Show the image
                            } else {
                                choiceFileElement.style.display = 'none'; // Hide the image if there's no file
                            }
                        }


                        const choiceFileElement = document.getElementById('choice-file');
                        if (choiceFile) {
                            choiceFileElement.src = choiceFile;
                            choiceFileElement.style.display = 'block';
                        } else {
                            choiceFileElement.style.display = 'none';
                        }

                    } else {
                        console.error('Error: Target card not found.');
                    }

                    // Re-enable the button after the animation finishes
                    button.prop('disabled', false);

                }, 9000); // Stop after 9 seconds (adjustable)

            } else {
                console.error('Error:', data.message);
                button.prop('disabled', false); // Re-enable the button if there's an error
            }
        })
        .catch(error => {
            console.error('Error:', error);
            button.prop('disabled', false); // Re-enable the button if there's an error
        });
});


