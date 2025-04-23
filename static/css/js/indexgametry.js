//both randomizecontents & randomizedcontents
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

    let persistSpin = localStorage.getItem('persistSpinChecked') === 'true';
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

    $('#persist-spin-checkbox').change(function() {
        const isChecked = $(this).prop('checked');
        localStorage.setItem('persistSpinChecked', isChecked.toString());
        persistSpin = isChecked;
        console.log("persistSpin updated to:", persistSpin);
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
        console.log('the value of totalspins at step 1 is ' + totalSpins)
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

observer.observe(document.querySelector('#card-container'), { childList: true });

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

async function randomizeContents() {
    const startButton = document.getElementById("start");
    const gameId = startButton.getAttribute("data-game-id");
    const nonce = startButton.getAttribute("data-nonce");
    const slug = startButton.getAttribute("data-slug");

    const executeRequest = async () => {
        const payload = {
            game_id: gameId,
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

        if (data.status !== 'success') {
            if (data.message && data.message.includes("database is locked")) {
                throw new Error("database_locked");
            }
            throw new Error(data.message || "Unknown error");
        }

        startButton.setAttribute('data-nonce', data.nonce);
        clearCards();

        const attributes = {
            id:          data.choice_id || 'N/A',
            nonce:       data.nonce || 'N/A',
            text:        data.choice_text || 'Unknown',
            color:       data.choice_color || '#FFFFFF',
            file:        data.choice_file || null,
            value:       data.choice_value || 0,
            lowerNonce:  data.lower_nonce || 'N/A',
            upperNonce:  data.upper_nonce || 'N/A',
        };

        const targetCardElement = document.createElement('div');
        targetCardElement.classList.add('card', 'target-card', 'sellattribute');
        targetCardElement.id = `card-${attributes.id}`;
        targetCardElement.dataset.nonce = attributes.nonce;
        targetCardElement.setAttribute('data-color', attributes.color);
        targetCardElement.dataset.choiceValue = attributes.value;
        targetCardElement.dataset.lowerNonce = attributes.lowerNonce;
        targetCardElement.dataset.upperNonce = attributes.upperNonce;

        targetCardElement.innerHTML = `
            <div class="cards" style="background: url(/static/css/images/${attributes.color}.png);">
                <div class="lootelement"
                    data-price="${attributes.value}"
                    style="display: flex; flex-direction: column; align-items: center; height: 100%; width: 10em; border-top: none;">
                    ${attributes.file ? `<div class="sliderImg" style="background-image: url(${attributes.file}); background-repeat: no-repeat; background-position: center; background-size: contain; height: 10em; width: 100%;"></div>` : ''}
                    <div class="sliderPrice" style="color: white;"><b class="innerprice">${attributes.value}</b> 💎 targetcard</div>
                </div>
            </div>
        `;

        selectedItems.push({
            id:         attributes.id,
            nonce:      attributes.nonce,
            text:       attributes.text,
            color:      attributes.color,
            src:        attributes.file,
            value:      attributes.value,
            lowerNonce: attributes.lowerNonce,
            upperNonce: attributes.upperNonce
        });

        const cardContainer = document.querySelector('.slider');
        const middleIndex = Math.floor(cardContainer.children.length / 1.3275);
        const insertIndex = Math.min(cardContainer.children.length, middleIndex);

        if (cardContainer.children[insertIndex]) {
            cardContainer.insertBefore(targetCardElement, cardContainer.children[insertIndex]);
        } else {
            cardContainer.appendChild(targetCardElement);
        }

        window.addEventListener('resize', () => {
            const idx = Math.floor(cardContainer.children.length / 1.3275);
            if (cardContainer.children[idx]) {
                cardContainer.insertBefore(targetCardElement, cardContainer.children[idx]);
            } else {
                cardContainer.appendChild(targetCardElement);
            }
        });

        try {
            const buttonId = startButton.id;
            const inventoryPayload = {
                choice_id:    data.choice_id,
                choice_value: data.choice_value,
                category:     data.category,
                price:        data.choice_value,
                condition:    data.condition,
                quantity:     1,
                buttonId:     buttonId,
            };

            console.log("Payload being sent:", inventoryPayload);

            const inventoryResponse = await fetch('/create_inventory_object/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                body: JSON.stringify(inventoryPayload),
            });

            const inventoryData = await inventoryResponse.json();
            console.log("Response from /create_inventory_object/:", inventoryData);

            if (inventoryData.status === 'success') {
                if (inventoryData.button_id === "start") {
                    const inventory_pk = inventoryData.inventory_object_id;
                    window.inventory_pk = inventory_pk;
                    targetCardElement.dataset.inventoryPk = inventory_pk;
                    window.sellUrl = `/inventory/${inventory_pk}/sell/`;
                    const sellForm = document.getElementById(`sell-form-${inventory_pk}`);
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
                } else if (inventoryData.button_id === "start2") {
                    console.log("Temporary inventory object created without user. ID:", inventoryData.inventory_object_id);
                }
            } else {
                console.error("Failed to create inventory object:", inventoryData.message);
            }

            return data;
        } catch (inventoryError) {
            console.error(`Inventory creation error: ${inventoryError}`);
            return null;
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

let removedCards = [];

// Modified clearCards function to store removed cards
function clearCards() {
    removedCards = []; // Clear previous removed cards
    const cardContainer = document.querySelector('.slider');
    if (!cardContainer) {
        console.error('Slider container not found.');
        return;
    }

    const targetCards = cardContainer.querySelectorAll('.target-card');
    targetCards.forEach(card => {
        removedCards.push(card);
        cardContainer.removeChild(card);
    });

    console.log("All target cards removed.");
}

function restoreCards() {
    const cardContainer = document.querySelector('.slider');
    if (!cardContainer) {
        console.error('Slider container not found.');
        return;
    }

    removedCards.forEach(card => {
        cardContainer.appendChild(card);
    });

    removedCards = []; // Clear after restoring
    console.log("All target cards restored.");
}

function addAnimation() {

    document.querySelectorAll('.slider').forEach(scroller => {
        scroller.style.animation = 'none';
        scroller.offsetHeight;
        let animationDuration;

        if (!window.USER?.isAuthenticated) {
          currentSpintype = "C";
          console.log('updated currentspintype using guest')
        } else {
          if (typeof currentSpintype === "undefined" || currentSpintype === null) {
            console.error("currentSpintype is not set");
            return;
          }
        }
        switch (currentSpintype) {
          case "I":
            animationDuration = isQuickSpin ? 1000 : 2000;
            break;
          case "S":
            animationDuration = isQuickSpin ? 8000 : 16000;
            break;
          case "C":
          default:
            animationDuration = isQuickSpin ? 9000 : 18000;
            break;
        }

        scroller.style.animation = `slideshow ${animationDuration}ms cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
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

    const middlePosition = Math.floor(nonTargetCards.length / 2);

    for (let i = 0; i < nonTargetCards.length; i++) {
        if (i === middlePosition && targetCard) {
            slider.appendChild(targetCard);
        }
        slider.appendChild(nonTargetCards[i]);
    }

    if (targetCard && !slider.querySelector('.target-card')) {
        const allCards = Array.from(slider.children);
        const middleIndex = Math.floor(allCards.length / 2);

        slider.insertBefore(targetCard, allCards[middleIndex]);
    }

    console.log("Slider contents randomized with target card positioned in the middle.");
}

function spin(buttonId) {
    if (currentSpin === totalSpins || animationStopped) {
        currentSpin = 0;
        animationStopped = false;
        console.log('the value of totalspins at step 3 is ' + totalSpins)
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
        if (!window.USER?.isAuthenticated) {
          currentSpintype = "C";
          console.log('currentspintype with guest')
        } else {
          if (typeof currentSpintype === "undefined" || currentSpintype === null) {
            console.error("currentSpintype is not set");
            return;
          }
        }
    if (currentSpintype === 'I') {
                animationDuration = isQuickSpin ? 500 : 1000;
            } else if (currentSpintype === 'S') {
                animationDuration = isQuickSpin ? 4000 : 8000;
            } else if (currentSpintype === 'C') {
                animationDuration = isQuickSpin ? 4500 : 9000;
            } else {
                animationDuration = isQuickSpin ? 4500 : 9000;
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
                console.log('gray hit')
            playThump();

        } else if (choiceColor === 'green') {
                console.log('green hit')
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
    }, 150);
    } else {
        animationStopped = true;
        console.log(`The spins have ended.`);
        setTimeout(() => {
        restoreCards();
        showPopup(buttonId);
    }, 250);

               if (!persistSpin) {
    totalSpins = 1;
    console.log("persistSpin not enabled; reset spins to 1");
    sessionStorage.setItem("totalSpins", totalSpins);
    $(".spin-option").removeClass("selected active");
    $(".spin-option[data-value='1']").addClass("selected active");

    const baseCost = document.getElementById('spin-container').getAttribute('data-base-cost');
    console.log('Base cost:', baseCost);

    const totalCost = parseInt(baseCost) * totalSpins;
    const costDisplay = document.getElementById('cost-display');
    if (costDisplay) {
    costDisplay.innerHTML = `<span id="total-cost">${totalCost}</span> 💎`;
    }
}
             else {
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

function createCelebrationEffects(container, color) {
  // Convert named colors to hex
  const colorMap = {
    red: "#FF0000",
    green: "#00FF00",
    blue: "#0000FF",
    yellow: "#FFFF00",
    orange: "#FFA500",
    black: "#000000",
    gray: "#808080",
    redblack: "#8B0000",
    redgold: "#FFD700",
  }

  const hexColor = colorMap[color.toLowerCase()] || color

  // Function to lighten a color
  function lightenColor(color, percent) {
    const hex = color.replace("#", "")
    const r = Number.parseInt(hex.substring(0, 2), 16)
    const g = Number.parseInt(hex.substring(2, 4), 16)
    const b = Number.parseInt(hex.substring(4, 6), 16)

    const factor = 1 + percent / 100
    const rNew = Math.min(255, Math.round(r * factor))
    const gNew = Math.min(255, Math.round(g * factor))
    const bNew = Math.min(255, Math.round(b * factor))

    return `#${rNew.toString(16).padStart(2, "0")}${gNew.toString(16).padStart(2, "0")}${bNew.toString(16).padStart(2, "0")}`
  }

  // Function to darken a color
  function darkenColor(color, percent) {
    const hex = color.replace("#", "")
    const r = Number.parseInt(hex.substring(0, 2), 16)
    const g = Number.parseInt(hex.substring(2, 4), 16)
    const b = Number.parseInt(hex.substring(4, 6), 16)

    const factor = 1 - percent / 100
    const rNew = Math.max(0, Math.round(r * factor))
    const gNew = Math.max(0, Math.round(g * factor))
    const bNew = Math.max(0, Math.round(b * factor))

    return `#${rNew.toString(16).padStart(2, "0")}${gNew.toString(16).padStart(2, "0")}${bNew.toString(16).padStart(2, "0")}`
  }

  // Function to create contrasting color
  function createContrastColor(color) {
    const hex = color.replace("#", "")
    const r = Number.parseInt(hex.substring(0, 2), 16)
    const g = Number.parseInt(hex.substring(2, 4), 16)
    const b = Number.parseInt(hex.substring(4, 6), 16)

    // Calculate luminance - if dark, return white; if light, return black
    const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return luminance > 0.5 ? "#000000" : "#FFFFFF"
  }

  const brightColor = lightenColor(hexColor, 30)
  const glowColor = lightenColor(hexColor, 50)
  const darkColor = darkenColor(hexColor, 30)
  const contrastColor = createContrastColor(hexColor)

  // Internal function to create a single fire particle with enhanced animation
  function createFireParticle(container, color, glowColor) {
    const particle = document.createElement("div")
    particle.className = "fire-particle"
    particle.style.position = "absolute"
    particle.style.bottom = "0"
    particle.style.width = `${5 + Math.random() * 12}px` // Varied sizes
    particle.style.height = `${10 + Math.random() * 20}px` // Taller for more flame-like appearance
    particle.style.borderRadius = "50% 50% 20% 20%" // More flame-like shape
    particle.style.filter = "blur(3px)" // Softer edges
    particle.style.backgroundColor = color
    particle.style.boxShadow = `0 0 18px 10px ${glowColor}` // Stronger glow
    particle.style.left = `${Math.random() * 100}%`
    particle.style.opacity = "0.9"
    particle.style.zIndex = "5" // Ensure flames appear above other elements

    // Add more randomness to the particle movement but limit the range
    const xOffset = (Math.random() - 0.5) * 60 // Wider horizontal movement
    const scaleVar = 0.7 + Math.random() * 1.3 // More varied scaling

    // Animate the particle with more dynamic movement
    const duration = 2.2 + Math.random() * 2.8 // Varied duration
    const delay = Math.random() * 0.8

    particle.style.transition = `transform ${duration}s cubic-bezier(0.1, 0.8, 0.2, 1) ${delay}s, opacity ${duration}s ease-out ${delay}s`

    // Add to container first, then start animation after a small delay
    container.appendChild(particle)

    setTimeout(() => {
      // More dynamic upward movement with some horizontal drift and rotation
      particle.style.transform = `translateY(-${90 + Math.random() * 70}px) translateX(${xOffset}px) scale(${scaleVar}) rotate(${(Math.random() - 0.5) * 25}deg)`
      particle.style.opacity = "0"
    }, 10)

    // Remove the particle after animation completes
    setTimeout(
      () => {
        if (document.body.contains(particle)) {
          particle.remove()
        }
      },
      (duration + delay) * 1000,
    )
  }

  // Internal function to create a single falling particle with animation
  function createFallingParticle(container, color, glowColor) {
    const particle = document.createElement("div")
    particle.className = "confetti-particle"
    particle.style.position = "absolute"
    particle.style.top = "-5%"
    particle.style.width = `${2 + Math.random() * 4}px` // Smaller particles
    particle.style.height = `${2 + Math.random() * 4}px`
    particle.style.borderRadius = "50%"
    particle.style.filter = "blur(1px)"
    particle.style.backgroundColor = color
    particle.style.boxShadow = `0 0 3px 1px ${glowColor}`
    particle.style.left = `${Math.random() * 100}%`
    particle.style.opacity = "1"
    particle.style.zIndex = "3"

    // Animate the particle
    const duration = 2.5 + Math.random() * 1.5 // Shorter duration
    const delay = Math.random() * 2

    particle.style.transition = `transform ${duration}s ease-in ${delay}s, opacity ${duration}s ease-in ${delay}s`

    // Add to container first, then start animation after a small delay
    container.appendChild(particle)

    setTimeout(() => {
      // Limit the fall distance to container height
      const fallDistance = Math.min(container.offsetHeight, 300) + 20
      particle.style.transform = `translateY(${fallDistance}px) rotate(${Math.random() > 0.5 ? 360 : -360}deg)`
      particle.style.opacity = "0"
    }, 10)

    // Remove the particle after animation completes
    setTimeout(
      () => {
        if (document.body.contains(particle)) {
          particle.remove()
        }
      },
      (duration + delay) * 1000,
    )
  }

  // Create a hypnotic spiral that matches the reference image
  function createHypnoticSpiral(cardContainer, color) {
    // Get the color from the card if available
    let cardColor = color
    const cardFireElement = cardContainer.querySelector('.card-fire')
    if (cardFireElement && cardFireElement.dataset.color) {
      cardColor = cardFireElement.dataset.color
    }

    const brightCardColor = lightenColor(cardColor, 30)
    const darkCardColor = darkenColor(cardColor, 30)
    const contrastCardColor = createContrastColor(cardColor)

    // Create spiral container
    const spiralContainer = document.createElement("div")
    spiralContainer.className = "spiral-container"
    spiralContainer.style.position = "absolute"
    spiralContainer.style.top = "0"
    spiralContainer.style.left = "0"
    spiralContainer.style.width = "100%"
    spiralContainer.style.height = "100%"
    spiralContainer.style.pointerEvents = "none"
    spiralContainer.style.zIndex = "1" // Behind content but above background
    spiralContainer.style.overflow = "hidden" // Prevent overflow

    // Create the SVG for the spiral
    const svgNS = "http://www.w3.org/2000/svg"
    const svg = document.createElementNS(svgNS, "svg")
    svg.setAttribute("width", "100%")
    svg.setAttribute("height", "100%")
    svg.setAttribute("viewBox", "-50 -50 100 100")
    svg.style.position = "absolute"
    svg.style.top = "50%"
    svg.style.left = "50%"
    svg.style.transform = "translate(-50%, -50%)"
    svg.style.opacity = "0.85"

    // Create a mask for the spiral to fade out toward the center
    const mask = document.createElementNS(svgNS, "mask")
    const maskId = `spiral-mask-${Math.random().toString(36).substring(2, 9)}`
    mask.setAttribute("id", maskId)

    // Create a radial gradient for the mask
    const maskGradient = document.createElementNS(svgNS, "radialGradient")
    const maskGradientId = `mask-gradient-${Math.random().toString(36).substring(2, 9)}`
    maskGradient.setAttribute("id", maskGradientId)

    // Add stops to create a fade effect (1 is visible, 0 is invisible)
    const stop1 = document.createElementNS(svgNS, "stop")
    stop1.setAttribute("offset", "0%")
    stop1.setAttribute("stop-color", "white")
    stop1.setAttribute("stop-opacity", "0.2") // Center is more transparent

    const stop2 = document.createElementNS(svgNS, "stop")
    stop2.setAttribute("offset", "40%")
    stop2.setAttribute("stop-color", "white")
    stop2.setAttribute("stop-opacity", "0.6") // Middle is semi-transparent

    const stop3 = document.createElementNS(svgNS, "stop")
    stop3.setAttribute("offset", "100%")
    stop3.setAttribute("stop-color", "white")
    stop3.setAttribute("stop-opacity", "1") // Outer edge is fully visible

    maskGradient.appendChild(stop1)
    maskGradient.appendChild(stop2)
    maskGradient.appendChild(stop3)

    // Create a rectangle that uses the gradient for the mask
    const maskRect = document.createElementNS(svgNS, "rect")
    maskRect.setAttribute("x", "-50")
    maskRect.setAttribute("y", "-50")
    maskRect.setAttribute("width", "100")
    maskRect.setAttribute("height", "100")
    maskRect.setAttribute("fill", `url(#${maskGradientId})`)

    mask.appendChild(maskRect)

    // Create multiple spiral paths for a more complex effect
    const spiralCount = 2; // Number of spiral arms
    const spirals = [];

    for (let s = 0; s < spiralCount; s++) {
      const spiral = document.createElementNS(svgNS, "path")

      // Generate the spiral path
      let pathData = "M 0,0 "
      const turns = 5 // Number of turns in the spiral
      const pointsPerTurn = 30 // Points per turn for smoothness
      const totalPoints = turns * pointsPerTurn
      const startAngle = (s / spiralCount) * Math.PI * 2 // Offset each spiral arm

      for (let i = 1; i <= totalPoints; i++) {
        const angle = startAngle + (i / pointsPerTurn) * Math.PI * 2
        const radius = (i / totalPoints) * 45 // Max radius of 45 (viewBox is -50 to 50)
        const x = radius * Math.cos(angle)
        const y = radius * Math.sin(angle)
        pathData += `L ${x},${y} `
      }

      spiral.setAttribute("d", pathData)
      spiral.setAttribute("fill", "none")
      spiral.setAttribute("stroke-width", "3.5")
      spiral.setAttribute("mask", `url(#${maskId})`)

      spirals.push(spiral);
    }

    // Create gradient for the spiral
    const gradient = document.createElementNS(svgNS, "linearGradient")
    const gradientId = `spiral-gradient-${Math.random().toString(36).substring(2, 9)}` // Unique ID
    gradient.setAttribute("id", gradientId)
    gradient.setAttribute("gradientUnits", "userSpaceOnUse")

    // Add stops to the gradient - use contrasting colors for better visibility
    const gradStop1 = document.createElementNS(svgNS, "stop")
    gradStop1.setAttribute("offset", "0%")
    gradStop1.setAttribute("stop-color", contrastCardColor)

    const gradStop2 = document.createElementNS(svgNS, "stop")
    gradStop2.setAttribute("offset", "50%")
    gradStop2.setAttribute("stop-color", brightCardColor)

    const gradStop3 = document.createElementNS(svgNS, "stop")
    gradStop3.setAttribute("offset", "100%")
    gradStop3.setAttribute("stop-color", contrastCardColor)

    gradient.appendChild(gradStop1)
    gradient.appendChild(gradStop2)
    gradient.appendChild(gradStop3)

    // Add the gradient and mask to the SVG
    const defs = document.createElementNS(svgNS, "defs")
    defs.appendChild(gradient)
    defs.appendChild(maskGradient)
    defs.appendChild(mask)
    svg.appendChild(defs)

    // Apply the gradient to the spirals and add them to the SVG
    spirals.forEach(spiral => {
      spiral.setAttribute("stroke", `url(#${gradientId})`)
      svg.appendChild(spiral)
    })

    // Add the SVG to the container
    spiralContainer.appendChild(svg)

    // Add animation for rotation - slower for a more hypnotic effect
    const animationDuration = 12 + Math.random() * 4
    const animationDirection = Math.random() > 0.5 ? "normal" : "reverse"
    svg.style.animation = `rotate-spiral ${animationDuration}s linear infinite ${animationDirection}`

    // Add a pulsing effect to the opacity
    svg.style.animation += `, pulse-opacity 4s ease-in-out infinite`

    // Insert the spiral container before the background element
    const background = cardContainer.querySelector(".background")
    if (background) {
      cardContainer.insertBefore(spiralContainer, background)
    } else {
      cardContainer.appendChild(spiralContainer)
    }

    return spiralContainer
  }

  // Add a style element for the animations
  const styleElement = document.createElement("style")
  styleElement.textContent = `
    @keyframes rotate-spiral {
      0% { transform: translate(-50%, -50%) rotate(0deg); }
      100% { transform: translate(-50%, -50%) rotate(360deg); }
    }

    @keyframes pulse-opacity {
      0% { opacity: 0.85; }
      50% { opacity: 0.5; }
      100% { opacity: 0.85; }
    }

    @keyframes flame-flicker {
      0%, 100% { opacity: 0.95; transform: scale(1.0) translateY(0); }
      25% { opacity: 0.8; transform: scale(1.05) translateY(-2px); }
      50% { opacity: 1.0; transform: scale(0.95) translateY(1px); }
      75% { opacity: 0.9; transform: scale(1.02) translateY(-1px); }
    }
  `
  document.head.appendChild(styleElement)

  // Create enhanced fire animation container with controlled height
  const fireContainer = document.createElement("div")
  fireContainer.className = "fire-animation-container"
  fireContainer.style.position = "absolute"
  fireContainer.style.bottom = "0"
  fireContainer.style.left = "0"
  fireContainer.style.width = "100%"
  fireContainer.style.height = "160px" // Adjusted height to prevent overflow
  fireContainer.style.pointerEvents = "none"
  fireContainer.style.zIndex = "4" // Ensure flames appear above other elements

  // Create enhanced fire base with gradient
  const fireBase = document.createElement("div")
  fireBase.className = "fire-base"
  fireBase.style.position = "absolute"
  fireBase.style.bottom = "-20px"
  fireBase.style.left = "0"
  fireBase.style.width = "100%"
  fireBase.style.height = "70px" // Increased height for more dramatic effect
  fireBase.style.borderRadius = "50% 50% 0 0"
  fireBase.style.filter = "blur(10px)" // Increased blur for softer effect
  fireBase.style.background = `radial-gradient(ellipse at center, ${glowColor} 0%, ${hexColor} 60%, transparent 100%)`
  fireBase.style.animation = "flame-flicker 3s infinite ease-in-out"

  fireContainer.appendChild(fireBase)

  // Create fire particles - more particles for a more intense effect
  for (let i = 0; i < 40; i++) { // Increased particle count
    createFireParticle(fireContainer, brightColor, glowColor)
  }

  // Create falling particles container
  const particlesContainer = document.createElement("div")
  particlesContainer.className = "falling-particles-container"
  particlesContainer.style.position = "absolute"
  particlesContainer.style.top = "0"
  particlesContainer.style.left = "0"
  particlesContainer.style.width = "100%"
  particlesContainer.style.height = "100%"
  particlesContainer.style.overflow = "hidden"
  particlesContainer.style.pointerEvents = "none"
  particlesContainer.style.zIndex = "3"

  // Create falling particles
  for (let i = 0; i < 25; i++) { // Moderate particle count
    createFallingParticle(particlesContainer, brightColor, glowColor)
  }

  // Create spiral effects for each card
  const cardContainers = container.querySelectorAll(".card-container")
  const spiralElements = []

  cardContainers.forEach((cardContainer) => {
    // Get the color from the card if available
    let cardColor = color
    const cardFireElement = cardContainer.querySelector('.card-fire')
    if (cardFireElement && cardFireElement.dataset.color) {
      cardColor = cardFireElement.dataset.color
    }

    spiralElements.push(createHypnoticSpiral(cardContainer, cardColor))
  })

  // Add containers to the main container
  container.prepend(particlesContainer)
  container.prepend(fireContainer)

  // Continue adding particles with controlled intervals
  const fireInterval = setInterval(() => {
    if (document.body.contains(fireContainer)) {
      // Add 1-3 particles at once for a more dynamic flame
      const particleCount = 1 + Math.floor(Math.random() * 3)
      for (let i = 0; i < particleCount; i++) {
        createFireParticle(fireContainer, brightColor, glowColor)
      }
    } else {
      clearInterval(fireInterval)
    }
  }, 120) // Faster interval for more particles

  const particlesInterval = setInterval(() => {
    if (document.body.contains(particlesContainer)) {
      createFallingParticle(particlesContainer, brightColor, glowColor)
    } else {
      clearInterval(particlesInterval)
    }
  }, 450) // Moderate interval for particles

  // Return a cleanup function
  return function cleanup() {
    // Clear all intervals
    clearInterval(fireInterval)
    clearInterval(particlesInterval)

    // Remove style element
    if (document.head.contains(styleElement)) {
      styleElement.remove()
    }

    // Remove containers
    if (document.body.contains(fireContainer)) {
      fireContainer.remove()
    }
    if (document.body.contains(particlesContainer)) {
      particlesContainer.remove()
    }

    // Remove all spiral elements
    spiralElements.forEach(element => {
      if (document.body.contains(element)) {
        element.remove()
      }
    })
  }
}


// Add CSS styles to the document
function addCelebrationStyles() {
  if (document.getElementById("celebration-styles")) return

  const styleElement = document.createElement("style")
  styleElement.id = "celebration-styles"
  styleElement.textContent = `
    .scrollablecontainer {
      position: relative;
      background-color: #1a1a1a;
      border-radius: 12px;
      padding: 24px;
      overflow: hidden;
      max-width: 90%;
      width: 500px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      color: white;
      text-align: center;
    }

    .congratulations {
      font-size: 28px;
      margin-bottom: 16px;
      background: linear-gradient(45deg, #ff8a00, #ff0058, #00ff8a, #00cfff);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: gradient-shift 3s ease infinite;
    }

    .treasure-subtitle {
      font-size: 22px;
      margin-bottom: 16px;
      color: #f5f5f5;
    }

    .cards-container {
      display: flex;
      justify-content: center;
      overflow-x: auto;
      margin: 20px 0;
      padding: 10px 0;
    }

    .inner-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
    }

    .card-container {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 0 10px;
    }

    .background {
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s ease;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    .background:hover {
      transform: translateY(-5px);
    }

    .background img {
      display: block;
      object-fit: contain;
    }

    .card-container p {
      margin-top: 8px;
      font-weight: bold;
      font-size: 18px;
    }

    .popup-actions {
      margin-top: 20px;
      display: flex;
      justify-content: center;
    }

    .finish-buttons {
      display: flex;
      flex-direction: row;
      gap: 15px;
      justify-content: center;
    }

    .close,
    .popup-button {
      padding: 10px 20px;
      border-radius: 50px;
      border: none;
      background-color: #4a4a4a;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .close:hover,
    .popup-button:hover {
      background-color: #5a5a5a;
      transform: translateY(-2px);
    }

    /* Card Fire Effect */
    .card-fire {
      position: absolute;
      top: -40px;
      width: 100%;
      height: 60px;
      border-radius: 50% 50% 0 0;
      filter: blur(8px);
      opacity: 0.9;
      z-index: 1;
    }

    .card-flames {
      position: relative;
      width: 100%;
      height: 100%;
    }

    .card-flame {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 80%;
      height: 120%;
      background: radial-gradient(ellipse at center, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0) 70%);
      border-radius: 50% 50% 0 0;
      filter: blur(4px);
      animation: powerful-flicker 1s infinite alternate;
    }

    /* Spiral animation */
    .spiral-container {
      position: absolute;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }

    @keyframes powerful-flicker {
      0% {
        opacity: 1;
        height: 120%;
        width: 80%;
      }
      25% {
        opacity: 0.95;
        height: 130%;
        width: 75%;
      }
      50% {
        opacity: 0.9;
        height: 110%;
        width: 85%;
      }
      75% {
        opacity: 0.95;
        height: 125%;
        width: 70%;
      }
      100% {
        opacity: 1;
        height: 120%;
        width: 80%;
      }
    }

    @keyframes gradient-shift {
      0% {
        background-position: 0% 50%;
      }
      50% {
        background-position: 100% 50%;
      }
      100% {
        background-position: 0% 50%;
      }
    }

    @media (max-width: 600px) {
      .scrollablecontainer {
        width: 95%;
        padding: 16px;
      }

      .congratulations {
        font-size: 24px;
      }

      .inner-container {
        gap: 10px;
      }

      .background img {
        width: 120px;
        height: 180px;
      }
    }
  `

  document.head.appendChild(styleElement)
}




async function showPopup(buttonId) {
  // Add the celebration styles to the document
  addCelebrationStyles()

  if (buttonId === "start") {
    console.log("Show Regular Start")
    window.csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value
    console.log("Sell Imported CSRFToken:", window.csrfToken)

    $(document).ready(() => {
      $(document).on("submit", "#sell-form-" + window.inventory_pk, function (e) {
        e.preventDefault()
        console.log("Submitting sell request")

        var form = $(this)
        var cardContainer = document.querySelector(".slider")
        var sellCards = cardContainer.querySelectorAll(".sellattribute")

        console.log("Sell cards before modification:")
      })

      $(document).on("click", ".sell-button", () => {
        const cardContainer = document.querySelector(".slider")
        const sellCards = cardContainer.querySelectorAll(".sellattribute")

        if (sellCards.length === 0) {
          console.log("No items to sell.")
          return
        }

        const itemsToSell = []
        sellCards.forEach((card) => {
          const inventory_pk = card.getAttribute("data-inventory-pk")
          if (!inventory_pk) {
            console.error("Card missing inventory_pk:", card)
            return
          }
          itemsToSell.push({
            inventory_pk: inventory_pk,
            price: card.getAttribute("data-price"),
            currencySymbol: card.getAttribute("data-currency-symbol"),
          })
        })

        console.log("Selling items:", itemsToSell)

        if (itemsToSell.length === 0) {
          console.error("No valid items to sell.")
          return
        }

        const sellUrl = `/sell/`
        console.log("Sell URL:", sellUrl)

        $.ajax({
          type: "POST",
          url: sellUrl,
          data: JSON.stringify({ items: itemsToSell }),
          contentType: "application/json",
          headers: { "X-CSRFToken": window.csrfToken },
          success: (response) => {
            console.log("Sell request succeeded:", response)

            if (response.success) {
              sellCards.forEach((card) => {
                console.log("Removing sold item:", {
                  inventory_pk: card.getAttribute("data-inventory-pk"),
                  price: card.getAttribute("data-price"),
                  currencySymbol: card.getAttribute("data-currency-symbol"),
                })
                card.remove()
              })
              console.log(`Sold ${itemsToSell.length} items.`)
            }
            if (response.html) {
              $("#updated-content-container").html(response.html)
            }
          },
          error: (error) => {
            console.error("Sell request failed:", error)
          },
        })
      })
    })

    function adjustCardsContainer() {
      const container = document.querySelector(".cards-container")
      const innerContainer = document.querySelector(".inner-container")
      if (!container || !innerContainer) return

      innerContainer.style.display = "flex"
      innerContainer.style.width = `${innerContainer.scrollWidth}px`

      const maxLimit = 600

      console.log(
        `Checked the size of the inner container (Width: ${innerContainer.scrollWidth}px, Max Width: ${maxLimit}px)`,
      )

      if (innerContainer.scrollWidth > maxLimit) {
        container.style.justifyContent = "flex-start"
        console.log(`Inner-container exceeds 600px → Align Left`)
      } else {
        container.style.justifyContent = "center"
        console.log(`Inner-container within 600px → Centering`)
      }
    }

    const textContainer = document.querySelector(".text")
    textContainer.classList.add("scrollablecontainer")
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
        <button type="submit" class="action-button sell-button" data-inventory-pk="${window.inventory_pk}"
          style="background-color: #c2fbd7; border-radius: 100px; box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset, rgba(44, 187, 99, .15) 0 1px 2px, rgba(44, 187, 99, .15) 0 2px 4px, rgba(44, 187, 99, .15) 0 4px 8px, rgba(44, 187, 99, .15) 0 8px 16px, rgba(44, 187, 99, .15) 0 16px 32px; color: green; cursor: pointer; display: inline-block; font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif; padding: 7px 20px; text-align: center; text-decoration: none; transition: all 250ms; border: 0; font-size: 16px; user-select: none; -webkit-user-select: none; touch-action: manipulation;">
            Sell
        </button>
      <button class="close">Collect</button>
      </div>
      </form>
    `

    setTimeout(() => {
      adjustCardsContainer()
    }, 100)

    window.addEventListener("resize", adjustCardsContainer)
  } else if (buttonId === "start2") {
    console.log("Show Demo Start")

    const textContainer = document.querySelector(".text")
    textContainer.classList.add("scrollablecontainer")
    textContainer.innerHTML = `
        <h4 class="treasure-subtitle">You could hit:</p>
        <div class="cards-container">
          <div class="inner-container"></div>
        </div>
        <div class="popup-actions" style="display: flex; flex-direction: row;">
            <a href="/gamehub/123/">
                <button class="popup-button secondary closer">More!</button>
            </a>
             <a href="{{game.get_absolute_url}}">
                <button class="popup-button secondary closer">More!</button>
            </a>
        </div>
    `
  }

  const popup = document.getElementById("popup")
  const textContainer = popup.querySelector(".text")
  const cardsContainer = textContainer.querySelector(".inner-container")

  // Get the main color from the first item for the fire animation
  const mainColor = selectedItems.length > 0 ? selectedItems[0].color : "yellow"

  // Create the celebration effects - this single call now handles all animations
  const cleanupEffects = createCelebrationEffects(textContainer, mainColor)

  // Add cards to the container
  selectedItems.forEach((item, index) => {
    const cardElement = document.createElement("div")
    cardElement.className = "card-container"
    cardElement.innerHTML = `
      <div class="card-fire" data-color="${item.color}" style="background-color: ${item.color}">
        <div class="card-flames">
          <div class="card-flame"></div>
        </div>
      </div>
      <div class="background" style="background-color: ${item.color}; padding: 10px; border-radius: 3px;">
        <img src="${item.src || ""}" alt="${item.id}" width=150 height=225>
      </div>
      <p>${item.value} 💎</p>
    `

    if (cardsContainer) {
      cardsContainer.appendChild(cardElement)
    } else {
      console.error("cardsContainer not found in DOM")
    }

    if (index === 0) {
      const fire = document.querySelector(".fire")
      if (fire) {
        fire.setAttribute("data-color", item.color)
      }
    }
  })

  popup.style.display = "block"

  setTimeout(() => {
    const fire = document.querySelector(".fire")
    if (fire) {
      fire.classList.add("active")
    }
  }, 100)

  // Add swipe to close functionality
  let touchStartX = 0
  let touchEndX = 0

  popup.addEventListener(
    "touchstart",
    (e) => {
      touchStartX = e.changedTouches[0].screenX
    },
    { once: true },
  )

  popup.addEventListener(
    "touchend",
    (e) => {
      touchEndX = e.changedTouches[0].screenX
      const swipeDistance = touchEndX - touchStartX
      if (Math.abs(swipeDistance) > 50) {
        const closeBtn = textContainer.querySelector(".close")
        if (closeBtn) {
          closeBtn.click()
        }
      }
    },
    { once: true },
  )

  // Set up close button
  const closeBtn = textContainer.querySelector(".close")
  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      // Clean up the celebration effects
      cleanupEffects()

      const audio = new Audio("/static/css/sounds/collect.mp3")
      audio.play()

      const fire = document.querySelector(".fire")
      if (fire) {
        fire.style.opacity = "0"
      }

      document.querySelectorAll(".card-fire").forEach((fire) => {
        fire.style.opacity = "0"
      })

      setTimeout(() => {
        popup.style.display = "none"
      }, 200)

      $(".spin-option").prop("disabled", false)
      $(".start").prop("disabled", false)
    })
  }

  // Set up sell button
  const sellBtn = textContainer.querySelector(".sell-button")
  if (sellBtn) {
    sellBtn.addEventListener("click", () => {
      // Clean up the celebration effects
      cleanupEffects()

      const audio = new Audio("/static/css/sounds/collect.mp3")
      audio.play()

      const fire = document.querySelector(".fire")
      if (fire) {
        fire.style.opacity = "0"
      }

      document.querySelectorAll(".card-fire").forEach((fire) => {
        fire.style.opacity = "0"
      })

      setTimeout(() => {
        popup.style.display = "none"
      }, 0)

      $(".spin-option").prop("disabled", false)
      $(".start").prop("disabled", false)

      setTimeout(() => {
        $.ajax({
          url: window.location.href,
          type: "GET",
          success: (response) => {
            const tempDiv = document.createElement("div")
            tempDiv.innerHTML = response
            const newContent = $(tempDiv).find(".sellupdate").html()
            $(".sellupdate").html(newContent)
          },
          error: (xhr, status, error) => {
            console.error("Ajax reload failed: " + xhr.status + " " + xhr.statusText)
          },
        })
      }, 0)
    })
  }
}

});