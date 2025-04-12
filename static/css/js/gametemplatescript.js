document.addEventListener('DOMContentLoaded', () => {
    const slider = document.getElementById('slider');
    const popup = document.getElementById('popup');
    const buttons = popup.querySelectorAll('.close, .sell-button');
    const fire = popup.querySelector('.fire');
    const textContainer = popup.querySelector('.text');

    let animationStopped = false;
    let selectedItems = [];
    let totalSpins = 1;
    let currentSpin = 0;

    const persistSpin = localStorage.getItem('persistSpinChecked') === 'true';
    const quickSpin = localStorage.getItem('quickSpinChecked') === 'true';

    const popuep = document.querySelector('.popup');
    const closewBtn = popup.querySelector('.close');

    let touchStartX = 0;
    let touchEndX = 0;

    popuep.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    });

    popuep.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    });

    function handleSwipe() {
      const swipeDistance = touchEndX - touchStartX;
      if (Math.abs(swipeDistance) > 50) {
        closewBtn.click();
      }
    }

    if (persistSpin) {
        $('#persist-spin-checkbox').prop('checked', true);
    }

    $('#persist-spin-checkbox').change(function () {
        localStorage.setItem('persistSpinChecked', $(this).prop('checked').toString());
    });

    $('#quickspin-checkbox').change(function () {
        localStorage.setItem('quickSpinChecked', $(this).prop('checked').toString());
    });

    $(".spin-option").click(function () {
        $(".spin-option").removeClass("selected");

        let audio = new Audio("/static/css/sounds/bubble_selection.mp3");
        audio.play();

        $(this).addClass("selected");
        totalSpins = parseInt($(this).data("value"));
        sessionStorage.setItem("totalSpins", totalSpins);
    });


    $(".start").click(function (event) {
        const buttonId = event.target.id;
        console.log(`Button clicked: ${buttonId}`);
        sessionStorage.setItem("startAnimation", "true");
        sessionStorage.setItem("isQuickSpin", $("#quickspin-checkbox").is(":checked"));


        let currentSpin = 0;
        console.log('current spin set to 0')
        initializeAnimation(buttonId);
    });

    function initializeAnimation(buttonId) {
        $(".start").prop('disabled', true);
        const isQuickSpin = sessionStorage.getItem("isQuickSpin") === "true";
        selectedItems = [];
        console.log(`Initializing animation for button: ${buttonId}`);



let requestInProgress = false;
const requestQueue = [];
const requestDelay = 300;

async function processQueue() {
    if (requestQueue.length === 0 || requestInProgress) return;

    requestInProgress = true;
    const nextRequest = requestQueue.shift();

    try {
        const result = await nextRequest();
        requestInProgress = false;
        setTimeout(processQueue, requestDelay);
        return result;
    } catch (error) {
        requestInProgress = false;
        setTimeout(processQueue, requestDelay);
        throw error;
    }
}

async function randomizeContents(buttonId, choiceColor) {
    const startButton = document.getElementById("start");
    const gameId = startButton.getAttribute("data-game-id");
    const nonce = startButton.getAttribute("data-nonce");
    const slug = startButton.getAttribute("data-slug");

    const executeRequest = async () => {
        const payload = {
            game_id: gameId,
            button_id: buttonId,
            color: choiceColor
        };

        await new Promise(resolve => setTimeout(resolve, Math.random() * 100));

        const response = await fetch(`/create_outcome/${slug}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            if (response.status === 500 && response.statusText.includes("database is locked")) {
                throw new Error("database_locked");
            }
            throw new Error(`HTTP error ${response.status}`);
        }

        const data = await response.json();

        if (data.status === 'success') {
            startButton.setAttribute('data-nonce', data.nonce);

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

            const targetCardElement = document.createElement('div');
            targetCardElement.classList.add('card', 'target-card', 'sellattribute');
            targetCardElement.setAttribute('id', `card-${attributes.id}`);
            targetCardElement.setAttribute('data-nonce', attributes.nonce);
            targetCardElement.setAttribute('data-color', attributes.color);
            targetCardElement.setAttribute('data-choice_value', attributes.value);
            targetCardElement.setAttribute('data-lower_nonce', attributes.lowerNonce);
            targetCardElement.setAttribute('data-upper_nonce', attributes.upperNonce);

            targetCardElement.innerHTML = `
                <div class="cards" style="background: url(/static/css/images/${attributes.color}.png);">
                    <div class="lootelement"
                        data-price="${attributes.value || ''}"
                        data-currency-file="${attributes.currencyFile || ''}"
                        data-currency-symbol="${attributes.currencySymbol || ''}"
                        style="display: flex; flex-direction: column; align-items: center; height: 100%; align-self: flex-start; border-top: none; width: 10em;">
                        ${attributes.file ? `<div class="sliderImg" style="background-image: url(${attributes.file}); background-repeat: no-repeat; background-position: center; background-size: contain; height: 10em; width: 100%;"></div>` : ''}
                        <div class="sliderPrice" style="color: white;">${attributes.value} 💎targetcard </div>
                    </div>
                </div>
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

            const cardContainer = document.querySelector('.slider');

            function updateCardPosition() {
                const windowWidth = window.innerWidth;
                const randomDivisor = Math.random() * (1.3375 - 1.3265) + 1.3265;
                const cardContainer = document.querySelector('.slider');
                const middleIndex = Math.floor(cardContainer.children.length / 1.327);
                const targetIndex = Math.min(cardContainer.children.length, middleIndex);

                if (cardContainer.children[targetIndex]) {
                    cardContainer.insertBefore(targetCardElement, cardContainer.children[targetIndex]);
                } else {
                    cardContainer.appendChild(targetCardElement);
                }
            }

            window.addEventListener('resize', updateCardPosition);
            updateCardPosition();

            try {
                const inventoryPayload = {
                    choice_id: data.choice_id,
                    choice_value: data.choice_value,
                    category: data.category,
                    price: 100,
                    condition: 'New',
                    quantity: 1,
                    buttonId: buttonId,
                };

                const inventoryResponse = await fetch('/create_inventory_object/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    body: JSON.stringify(inventoryPayload),
                });

                const inventoryData = await inventoryResponse.json();

                if (inventoryData.status === 'success') {
                    if (inventoryData.button_id === "start") {
                        let inventory_pk = inventoryData.inventory_object_id;
                        window.inventory_pk = inventory_pk;
                        targetCardElement.setAttribute('data-inventory_pk', window.inventory_pk);

                        window.sellUrl = `/inventory/${inventory_pk}/sell/`;
                        const sellForm = document.getElementById(`sell-form-${window.inventory_pk}`);

                        if (sellForm) {
                            sellForm.addEventListener('submit', function(event) {
                                event.preventDefault();
                                const pk = this.querySelector('[name="pk"]').value;

                                $(".spin-option").removeClass("selected");
                                $(this).addClass("selected");
                                totalSpins = parseInt($(this).data("value"));
                                sessionStorage.setItem("totalSpins", totalSpins);
                                sellInventory(pk);
                            });
                        }
                    }
                }
            } catch (inventoryError) {
                console.error(`Inventory creation error: ${inventoryError}`);
            }

            return data;
        } else {
            if (data.message && data.message.includes("database is locked")) {
                throw new Error("database_locked");
            }
            throw new Error(data.message || "Unknown error");
        }
    };

    const executeWithRetry = async () => {
        const maxRetries = 3;
        let retryCount = 0;

        while (retryCount < maxRetries) {
            try {
                return await executeRequest();
            } catch (error) {
                retryCount++;

                if (error.message === "database_locked" && retryCount < maxRetries) {
                    await new Promise(resolve => setTimeout(resolve, 500 * retryCount));
                    continue;
                }

                throw error;
            }
        }
    };

    return new Promise((resolve, reject) => {
        requestQueue.push(async () => {
            try {
                const result = await executeWithRetry();
                resolve(result);
                return result;
            } catch (error) {
                reject(error);
                throw error;
            }
        });

        if (!requestInProgress) {
            processQueue();
        }
    });
}

function clearCards() {
    const cardContainer = document.querySelector('.slider');
    const targetCards = cardContainer.querySelectorAll('.target-card');

    targetCards.forEach(card => {

        card.querySelectorAll('*').forEach(child => {
            child.style.display = 'none';
        });
    });

    console.log("All target cards modified (class removed, child elements hidden, but kept 'sellattribute').");
}

        function addAnimation() {
            document.querySelectorAll('.slider').forEach(scroller => {
                scroller.style.animation = 'none';
                scroller.offsetHeight;
                let animationDuration;
                if (isQuickSpinInteractive) {
                    animationDuration = isQuickSpin ? '1s' : '2s';
                } else {
                    animationDuration = isQuickSpin ? '9s' : '18s';
                }

                scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
                scroller.style.animationPlayState = 'running';
            });
        }

function alignCardWithSpinner() {
    const spinnerTick = document.getElementById('selector');
    const slider = document.getElementById('slider');
    const targetCard = document.querySelector('.target-card');

    if (!targetCard || !spinnerTick) {
        console.error('Target card or spinner tick not found!');
        return;
    }

    const spinnerTickRect = spinnerTick.getBoundingClientRect();
    const spinnerTickCenter = spinnerTickRect.left + spinnerTickRect.width / 2;

    const targetCardRect = targetCard.getBoundingClientRect();
    const targetCardCenter = targetCardRect.left + targetCardRect.width / 2;

    const offset = spinnerTickCenter - targetCardCenter;

    const currentTransform = getComputedStyle(slider).transform;
    const matrix = new DOMMatrix(currentTransform);
    const currentTranslateX = matrix.m41 || 0;

    slider.style.transform = `translateX(${currentTranslateX + offset}px)`;
    //console.log(`Slider adjusted by offset: ${offset}px`);
}



$(".start").click(function (event) {
    const buttonId = event.target.id;
    console.log(`Button clicked: ${buttonId}`);

});


const casinoThump = new Audio('/static/css/sounds/thump.mp3');
const casinoGreen = new Audio('/static/css/sounds/money.mp3');
const casinoYellow = new Audio('/static/css/sounds/retro_video_game_col.mp3');
const casinoOrange = new Audio('/static/css/sounds/click-nice.mp3');
const casinoRed = new Audio('/static/css/sounds/redwin.mp3');
const casinoBlack = new Audio('/static/css/sounds/blackwin.mp3');
const casinoRedBlack = new Audio('/static/css/sounds/rap.mp3');
const casinoRedGold = new Audio('/static/css/sounds/ultimatewin.mp3');

function playThump() {
    casinoThump.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoGreenSound() {
    casinoGreen.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoYellowSound() {
    casinoYellow.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoOrangeSound() {
    casinoOrange.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoRedSound() {
    casinoRed.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoBlackSound() {
    casinoBlack.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoRedBlackSound() {
    casinoRedBlack.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function playCasinoRedGoldSound() {
    casinoRedGold.play().catch((error) => {
        console.error('Error playing casino-win audio:', error);
    });
}

function createTopHit(data, buttonId) {
    data.demonstration = buttonId === "start2";

    fetch('/top-hits/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((result) => {
        if (result.error) {
            console.error('Error creating Top Hit:', result.error);
        } else {
            console.log('Top Hit created successfully:', result);
        }
    })
    .catch((error) => {
        console.error('Network error:', error);
    });
}



function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring('csrftoken='.length, cookie.length);
        }
    }
    return null;
}

const targetCard = document.querySelector('.target-card');
let choiceColor = targetCard ? targetCard.getAttribute('data-color') : 'gray';

console.log('Given the choice color:', choiceColor);

function randomizedContents() {
    const slider = document.querySelector('.slider');
    const children = Array.from(slider.children);

    // Find the target card
    const targetIndex = children.findIndex(child => child.classList.contains('target-card'));
    let targetCard = null;
    if (targetIndex !== -1) {
        targetCard = children[targetIndex];
    }

    // Get all non-target cards
    const nonTargetCards = children.filter(child => !child.classList.contains('target-card'));

    // Shuffle non-target cards
    for (let i = nonTargetCards.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [nonTargetCards[i], nonTargetCards[j]] = [nonTargetCards[j], nonTargetCards[i]];
    }

    // Clear the slider
    slider.innerHTML = '';

    // Calculate middle position
    const middlePosition = Math.floor(nonTargetCards.length / 2);

    // Add cards to the slider with target card in the middle
    for (let i = 0; i < nonTargetCards.length; i++) {
        if (i === middlePosition && targetCard) {
            // Insert target card in the middle position
            slider.appendChild(targetCard);
        }
        slider.appendChild(nonTargetCards[i]);
    }

    // If we haven't added the target card yet (in case the middle position calculation was off)
    if (targetCard && !slider.querySelector('.target-card')) {
        const allCards = Array.from(slider.children);
        const middleIndex = Math.floor(allCards.length / 2);

        // Insert target card in the exact middle
        slider.insertBefore(targetCard, allCards[middleIndex]);
    }

    console.log("Slider contents randomized with target card positioned in the middle.");
}




function spin(buttonId) {
    if (currentSpin === totalSpins || animationStopped) {
        currentSpin = 0;
        animationStopped = false;
    }

    $(".spin-option").prop('disabled', true);

    randomizeContents();
    if (
        !userContext.isSignedIn ||
        !userContext.hasPreference ||
        userContext.preferenceValue !== "I"
    )
    {   console.log('not an instant spin')
        randomizedContents();
        addAnimation();
        }

        else{
         console.log('actually instant spin')
        randomizedContents();
        addAnimation();
        }


    if (buttonId === "start") {
        console.log("Regular Spin triggered");
    } else if (buttonId === "start2") {
        console.log("Demo Spin triggered");
    }

let animationDuration;

if (
    !userContext.isSignedIn ||
    !userContext.hasPreference ||
    userContext.preferenceValue !== "I"
) {
    animationDuration = isQuickSpin ? 4500 : 9000;
} else {
    animationDuration = isQuickSpin ? 500 : 1000;
}


    const buffer = 150;
    const audiobuffer = 100;
    const audio = new Audio('/static/css/sounds/roulette_sound_effect.mp3');

    audio.addEventListener('loadedmetadata', () => {
        const adjustedDuration = (animationDuration + audiobuffer) / 1000;
        const originalDuration = audio.duration;

        if (originalDuration) {
            audio.playbackRate = originalDuration / adjustedDuration;
        }

        audio.play().catch((error) => console.error('Error playing audio:', error));
    });

    audio.addEventListener('error', (e) => {
        console.error('Audio failed to load:', e);
    });

setTimeout(() => {
    document.querySelectorAll('.slider').forEach((scroller) => {
        scroller.style.animationPlayState = 'paused';


    const targetCard = document.querySelector('.target-card');

    const startButton = document.getElementById('start');


    if (targetCard) {
        let choiceColor = targetCard.getAttribute('data-color') || 'gray';
        let choiceId = targetCard.getAttribute('id');
        let gameId = startButton.getAttribute("data-game-id");


        console.log('The choice color is:', choiceColor);
        console.log('The choice id is:', choiceId);
        console.log('The game id is:', gameId);
        if (choiceColor === 'gray') {
            playThump();

        } else if (choiceColor === 'green') {
            playCasinoGreenSound();
            $(".start").prop('disabled', true);
        } else if (choiceColor === 'yellow') {
                console.log('yellow hit')
            playCasinoGreenSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        } else if (choiceColor === 'orange') {
                console.log('orange hit')
            playCasinoYellowSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        } else if (choiceColor === 'red') {
                console.log('red hit')
            playCasinoRedSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        } else if (choiceColor === 'black') {
                console.log('black hit')
            playCasinoBlackSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        } else if (choiceColor === 'redblack') {
                console.log('redblack hit')
            playCasinoRedBlackSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        } else if (choiceColor === 'redgold') {
                console.log('redgold hit')
            playCasinoRedGoldSound();
                const topHitData = {
                    choice_id: targetCard.getAttribute('id').split('-')[1],
                    color: choiceColor,
                    game_id: gameId,
                };
                createTopHit(topHitData);
                $(".start").prop('disabled', true);
                console.log('processed the top hit')
        }
        }

    });

function randomizedContents() {
    const slider = document.querySelector('.slider');
    const children = Array.from(slider.children);

    const targetIndex = children.findIndex(child => child.classList.contains('target-card'));
    let targetCard = null;
    if (targetIndex !== -1) {
        targetCard = children[targetIndex];
    }

    const nonTargetCards = children.filter(child => !child.classList.contains('target-card'));

    for (let i = nonTargetCards.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [nonTargetCards[i], nonTargetCards[j]] = [nonTargetCards[j], nonTargetCards[i]];
    }

    slider.innerHTML = '';

    const totalCards = nonTargetCards.length + (targetCard ? 1 : 0);
    for (let i = 0, j = 0; i < totalCards; i++) {
        if (i === targetIndex && targetCard) {
            slider.appendChild(targetCard);
        } else {
            slider.appendChild(nonTargetCards[j]);
            j++;
        }
    }

    console.log("Slider contents randomized without affecting target card position.");
}

    currentSpin++;
    console.log(`Spin #${currentSpin} completed for Button ID: ${buttonId}`);

    if (currentSpin < totalSpins) {
        setTimeout(() => spin(buttonId), buffer);
         setTimeout(() => {
        randomizedContents();
    }, 500);
    } else {
        animationStopped = true;
        console.log(`The spins have ended.`);
        setTimeout(() => {
        showPopup(buttonId);
    }, 250);

                if (!persistSpin) {
                    totalSpins = 1;
                    console.log("persistSpin disabled; reset spins to 1");
                    sessionStorage.setItem("totalSpins", totalSpins);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                } else {
                    const currentSelectionValue = parseInt($(".spin-option.selected").data("value") || 1, 10);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                    setTimeout(() => {
                        $(".spin-option").removeClass("selected active");
                        $(".spin-option[data-value='" + currentSelectionValue + "']")
                            .addClass("selected active");

                        totalSpins = currentSelectionValue;
                        console.log("Reverted spin to:", totalSpins);
                    }, 0);
                }

        $(".spin-option").prop('disabled', false);
    }
}, animationDuration);

}
spin(buttonId);

}


    const sellAudio = new Audio("{% static 'css/sounds/sell_coin.mp3' %}");
    document.querySelectorAll('.sell-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            sellAudio.play();
            console.log('')
            handleAjaxFormSubmission(form);
        });
    });

    function handleAjaxFormSubmission(form) {
        const formData = new FormData(form);
        const actionUrl = form.getAttribute('action');

        fetch(actionUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('stock-count').textContent = data.number_of_cards;
            } else {
                console.error(data.error);
            }
        });
    }

 async function showPopup(buttonId) {
    function adjustCardsContainer() {
        const container = document.querySelector('.cards-container');
        const innerContainer = document.querySelector('.inner-container');
        if (!container || !innerContainer) return;

        innerContainer.style.display = "flex";
        innerContainer.style.width = `${innerContainer.scrollWidth}px`;

        const maxLimit = 600;

        console.log(`Checked the size of the inner container (Width: ${innerContainer.scrollWidth}px, Max Width: ${maxLimit}px)`);

        if (innerContainer.scrollWidth > maxLimit) {
            container.style.justifyContent = 'flex-start';
            console.log(`Inner-container exceeds 600px → Align Left`);
        } else {
            container.style.justifyContent = 'center';
            console.log(`Inner-container within 600px → Centering`);
        }
    }

    textContainer.classList.add('scrollablecontainer');
    textContainer.innerHTML = `
      <h2 class='congratulations'>Congratulations!</h2>
      <p>You got:</p>
      <div class="cards-container">
        <div class="inner-container"></div>
      </div>
      <form id="sell-form-${window.inventory_pk}" action="${window.sellUrl}" method="post" class="ajax-form">
        <input type="hidden" name="csrfmiddlewaretoken" value="${window.csrfToken}">
        <input type="hidden" name="action" value="sell">
        <input type="hidden" name="pk" value="${window.inventory_pk}">
        <div class="finish-buttons" style="display: flex; flex-direction: row; gap: 15px; justify-content: center;">
        <button type="submit" class="action-button sell-button" data-inventory_pk="${window.inventory_pk}"
          style="background-color: #c2fbd7; border-radius: 100px; box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset, rgba(44, 187, 99, .15) 0 1px 2px, rgba(44, 187, 99, .15) 0 2px 4px, rgba(44, 187, 99, .15) 0 4px 8px, rgba(44, 187, 99, .15) 0 8px 16px, rgba(44, 187, 99, .15) 0 16px 32px; color: green; cursor: pointer; display: inline-block; font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif; padding: 7px 20px; text-align: center; text-decoration: none; transition: all 250ms; border: 0; font-size: 16px; user-select: none; -webkit-user-select: none; touch-action: manipulation;">
            Sell
        </button>
      <button class="close">Collect</button>
      </div>
      </form>
    `;

       setTimeout(() => {
            adjustCardsContainer();
        }, 100);

    window.addEventListener('resize', adjustCardsContainer);


if (buttonId === "start") {
  console.log("Show Regular Start");
  window.csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  console.log("Sell Imported CSRFToken:", window.csrfToken);

$(document).ready(function() {
    $(document).on("submit", "#sell-form-" + window.inventory_pk, function(e) {
        e.preventDefault();
        console.log('Submitting sell request');

        var form = $(this);
        var cardContainer = document.querySelector('.slider');
        var sellCards = cardContainer.querySelectorAll('.sellattribute');

        console.log("Sell cards before modification:");
        sellCards.forEach(card => {
            console.log({
                price: card.getAttribute("data-price"),
                currencyFile: card.getAttribute("data-currency-file"),
                currencySymbol: card.getAttribute("data-currency-symbol"),
                background: card.style.background,
            });

                const targetCards = cardContainer.querySelectorAll('.target-card');
                targetCards.forEach(card => {
                    card.querySelectorAll('*').forEach(child => {
                        child.style.display = 'none';
                    });
                });
        });

        $.ajax({
            type: "POST",
            url: form.attr("action"),
            data: form.serialize(),
            success: function(response) {
                console.log('Sell request succeeded:', response);
                if (response.html) {
                    $("#updated-content-container").html(response.html);
                }
            },
            error: function(error) {
                console.error("Sell request failed:", error);
            }
        });
    });

$(document).on("click", ".sell-button, .close", function() {
    const cardContainer = document.querySelector('.slider');
    const sellCards = cardContainer.querySelectorAll('.sellattribute');

    if (sellCards.length === 0) {
        console.log("No items to sell.");
        return;
    }

    let itemsToSell = [];
    sellCards.forEach(card => {
        const inventory_pk = card.getAttribute("data-inventory_pk");
        if (!inventory_pk) {
            console.error("Card missing inventory_pk:", card);
            return;
        }
        itemsToSell.push({
            inventory_pk: inventory_pk,
            price: card.getAttribute("data-price"),
            currencySymbol: card.getAttribute("data-currency-symbol")
        });
    });

    console.log("Selling items:", itemsToSell);

    if (itemsToSell.length === 0) {
        console.error("No valid items to sell.");
        return;
    }

    let sellUrl = `/sell/`;
    console.log("Sell URL:", sellUrl);

    $.ajax({
        type: "POST",
        url: sellUrl,
        data: JSON.stringify({ items: itemsToSell }),
        contentType: "application/json",
        headers: { "X-CSRFToken": window.csrfToken },
        success: function(response) {
            console.log("Sell request succeeded:", response);

            if (response.success) {
                sellCards.forEach(card => {
                    console.log("Removing sold item:", {
                        inventory_pk: card.getAttribute("data-inventory_pk"),
                        price: card.getAttribute("data-price"),
                        currencySymbol: card.getAttribute("data-currency-symbol")
                    });
                    card.remove();
                });
                console.log(`Sold ${itemsToSell.length} items.`);
            }
            if (response.html) {
                $("#updated-content-container").html(response.html);
            }
        },
        error: function(error) {
            console.error("Sell request failed:", error);
        }
    });
});

});



   textContainer.innerHTML = `
    <h2>Congratulations!</h2>
    <p>You got:</p>
    <div class="cards-container"></div>
    <form id="sell-form-${window.inventory_pk}" action="${window.sellUrl}" method="post" class="ajax-form">
      <input type="hidden" name="csrfmiddlewaretoken" value="${window.csrfToken}">
      <input type="hidden" name="action" value="sell">
      <input type="hidden" name="pk" value="${window.inventory_pk}">
      <div class="finish-buttons" style="display: flex; flex-direction: row; gap: 15px; justify-content: center;">
        <button type="submit" class="action-button sell-button" data-inventory_pk="${window.inventory_pk}"
          style="background-color: #c2fbd7; border-radius: 100px; box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset, rgba(44, 187, 99, .15) 0 1px 2px, rgba(44, 187, 99, .15) 0 2px 4px, rgba(44, 187, 99, .15) 0 4px 8px, rgba(44, 187, 99, .15) 0 8px 16px, rgba(44, 187, 99, .15) 0 16px 32px; color: green; cursor: pointer; display: inline-block; font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif; padding: 7px 20px; text-align: center; text-decoration: none; transition: all 250ms; border: 0; font-size: 16px; user-select: none; -webkit-user-select: none; touch-action: manipulation;">
            Sell
        </button>
      <button class="close">Collect</button>
      </div>
    </form>

`;

  } else if (buttonId === "start2") {
      console.log("Show Demo Start");

      textContainer.innerHTML = `
            <h2></h2>
            <p>You would have hit:</p>
            <div class="cards-container"></div>

            <button class="close">I see</button>
        `;
  }


     const cardsContainer = textContainer.querySelector('.cards-container');
     selectedItems.forEach((item, index) => {
         const cardElement = document.createElement('div');
         cardElement.innerHTML = `
            <div class="card-fire" data-color="${item.color}" style="background-color: ${item.color}">
              <div class="card-flames">
                <div class="card-flame"></div>
              </div>
            </div>
            <!--<p>ID: ${item.id}</p>
            <p>Nonceword: ${item.nonce}</p>-->
            <div class="background" style="background-color: ${item.color}; padding: 10px; border-radius: 3px;">
            <img src="${item.src || ''}" alt="${item.id}" width=150 height=225>
            </div>
            <p>${item.value} 💎</p>
            <!--<p>Lower Nonce: ${item.lowerNonce}</p>
            <p>Upper Nonce: ${item.upperNonce}</p>-->
        `;


            cardsContainer.appendChild(cardElement);

            if (index === 0) {
                const fire = document.querySelector('.fire');
                fire.setAttribute('data-color', item.color);
            }
        });

        popup.style.display = 'block';

        setTimeout(() => {
            const fire = document.querySelector('.fire');
            fire.classList.add('active');
        }, 100);

        const closeBtn = textContainer.querySelector('.close');
        closeBtn.addEventListener('click', () => {




        $(this).addClass("selected");
        totalSpins = parseInt($(this).data("value"));
        sessionStorage.setItem("totalSpins", totalSpins);
        const audio = new Audio('/static/css/sounds/collect.mp3');
        audio.play();

            const fire = document.querySelector('.fire');
            fire.style.opacity = '0';
            document.querySelectorAll('.card-fire').forEach(fire => {
                fire.style.opacity = '0';
            });

            setTimeout(() => {
                popup.style.display = 'none';
            }, 200);

            $(".spin-option").prop('disabled', false);
            $(".start").prop('disabled', false);

 if (!persistSpin) {
                    totalSpins = 1;
                    console.log("persistSpin disabled; reset spins to 1");
                    sessionStorage.setItem("totalSpins", totalSpins);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                } else {
                    const currentSelectionValue = parseInt($(".spin-option.selected").data("value") || 1, 10);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                    setTimeout(() => {
                        $(".spin-option").removeClass("selected active");
                        $(".spin-option[data-value='" + currentSelectionValue + "']")
                            .addClass("selected active");

                        totalSpins = currentSelectionValue;
                        console.log("Reverted spin to:", totalSpins);
                    }, 0);
                }
        });

const sellBtn = textContainer.querySelector('.sell-button');
sellBtn.addEventListener('click', () => {
    const audio = new Audio('/static/css/sounds/collect.mp3');
    audio.play();

    const fire = document.querySelector('.fire');
    fire.style.opacity = '0';
    document.querySelectorAll('.card-fire').forEach(fire => {
        fire.style.opacity = '0';
    });

    setTimeout(() => {
        popup.style.display = 'none';
    }, 0);

    $(".spin-option").prop('disabled', false);
    $(".start").prop('disabled', false);

    if (!persistSpin) {
                    totalSpins = 1;
                    console.log("persistSpin disabled; reset spins to 1");
                    sessionStorage.setItem("totalSpins", totalSpins);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                } else {
                    const currentSelectionValue = parseInt($(".spin-option.selected").data("value") || 1, 10);

                    $(".spin-option").removeClass("selected active");
                    $(".spin-option[data-value='1']").addClass("selected active");

                    setTimeout(() => {
                        $(".spin-option").removeClass("selected active");
                        $(".spin-option[data-value='" + currentSelectionValue + "']")
                            .addClass("selected active");

                        totalSpins = currentSelectionValue;
                        console.log("Reverted spin to:", totalSpins);
                    }, 0);
                }

    setTimeout(() => {
        $.ajax({
            url: window.location.href,
            type: 'GET',
            success: function(response) {
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = response;
                const newContent = $(tempDiv).find('.sellupdate').html();
                $('.sellupdate').html(newContent);
            },
            error: function(xhr, status, error) {
                console.error("Ajax reload failed: " + xhr.status + " " + xhr.statusText);
            }
        });
    }, 0);
});



    }
});

