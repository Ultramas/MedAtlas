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

    if (sessionStorage.getItem("totalSpins")) {
        totalSpins = parseInt(sessionStorage.getItem("totalSpins"));
    }

    if (sessionStorage.getItem("startAnimation") === "true") {
        sessionStorage.removeItem("startAnimation");
        initializeAnimation();
    }

    if (persistSpin) {
        $('#persist-spin-checkbox').prop('checked', true);
    }

    $('#quickspin-checkbox').prop('checked', quickSpin);

    $('#persist-spin-checkbox').change(function () {
        localStorage.setItem('persistSpinChecked', $(this).prop('checked').toString());
    });

    $('#quickspin-checkbox').change(function () {
        localStorage.setItem('quickSpinChecked', $(this).prop('checked').toString());
    });

    $(".spin-option").click(function () {
        $(".spin-option").removeClass("selected");
        $(this).addClass("selected");
        totalSpins = parseInt($(this).data("value"));
        sessionStorage.setItem("totalSpins", totalSpins);
    });

    if (sessionStorage.getItem("totalSpins")) {
        totalSpins = parseInt(sessionStorage.getItem("totalSpins"));
        $(`.spin-option[data-value="${totalSpins}"]`).addClass("selected");
    } else {
        $(".spin-option").first().addClass("selected");
    }

    $(".start").click(function () {
        sessionStorage.setItem("startAnimation", "true");
        sessionStorage.setItem("isQuickSpin", $("#quickspin-checkbox").is(":checked"));
        location.reload();
    });

    function initializeAnimation() {
        $(".start").prop('disabled', true);
        const isQuickSpin = sessionStorage.getItem("isQuickSpin") === "true";
        selectedItems = [];

        function randomizeContents() {
            $('#slider .cards').sort(() => 0.5 - Math.random()).appendTo('#slider');
        }

        function addAnimation() {
            document.querySelectorAll('.slider').forEach(scroller => {
                scroller.style.animation = 'none';
                scroller.offsetHeight;
                let animationDuration = isQuickSpin ? '9s' : '18s';
                scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
                scroller.style.animationPlayState = 'running';
            });
        }

        function spin() {
            $(".spin-option").prop('disabled', true);

            randomizeContents();
            addAnimation();

            setTimeout(() => {
                document.querySelectorAll('.slider').forEach(scroller => {
                    scroller.style.animationPlayState = 'paused';
                });

                findSelectedCard();
                currentSpin++;

                if (currentSpin < totalSpins) {
                    setTimeout(spin, 1000);
                } else {
                    animationStopped = true;
                    showPopup();

                    if (!persistSpin) {
                        totalSpins = 1;
                        sessionStorage.setItem("totalSpins", totalSpins);
                    }

                    $(".start").prop('disabled', false);
                    $(".spin-option").prop('disabled', false);
                }
            }, isQuickSpin ? 4500 : 9000);
        }

        spin();
    }

    function findSelectedCard() {
        const selector = document.getElementById('selector').getBoundingClientRect();
        document.querySelectorAll('.cards').forEach(card => {
            const cardRect = card.getBoundingClientRect();
            if (!(selector.right < cardRect.left || selector.left > cardRect.right || selector.bottom < cardRect.top || selector.top > cardRect.bottom)) {
                selectedItems.push({
                    id: card.id,
                    src: card.querySelector('img').src,
                    price: card.dataset.price,
                    color: card.dataset.color,
                    value: card.dataset.value  // Access the value field here
                });
            }
        });
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

    // Remove old event listener if it exists
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