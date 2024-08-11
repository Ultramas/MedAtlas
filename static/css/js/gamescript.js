$(".start").click(function () {
    const button = $(this);
    button.prop('disabled', true); // Disable the button when clicked

    let randomizeFlag = true; // Flag to track randomization
    const slider = document.querySelector('.slider');
    const popup = document.querySelector('.popup'); // Assuming you have a popup element
    let Touching = ''; // Initialize Touching with an empty string

    // Function to randomly change the order of elements
    function randomizeContents() {
        if (randomizeFlag) {
            $('div#slider').each(function(){
                var $div_parent = $(this);
                var $divsArr = $div_parent.children('div.cards');
                $divsArr.sort(function(a, b){
                    var temp = parseInt(Math.random() * 10);
                    var isOddOrEven = temp % 2;
                    var isPosOrNeg = temp > 5 ? 1 : -1;
                    return (isOddOrEven * isPosOrNeg);
                }).appendTo($div_parent);
            });

            setTimeout(randomizeContents, 2000); // Randomize again after 2 seconds
        }
    }

    // Call randomizeContents initially
    randomizeContents();

    // Stop randomization after 9 seconds
    setTimeout(() => {
        randomizeFlag = false;
    }, 9000);

    // AJAX call to create outcome
    createOutcome(button.data('game-id'), button.data('slug'))
        .then(data => {
            if (data.status === 'success') {
                // Render the response data to the UI
                renderChoiceDetails(data);

                // Determine which card is "touching" (if this logic is necessary)
                const touchingDivs = findTouchingDivs();
                console.log(touchingDivs);

                // Example logic to handle touching divs and set Touching variable
                if (findTouchingDivs(div5, div1)) {
                    console.log('Mewtwo is selected');
                    Touching = 'Mewtwo';
                } else if (findTouchingDivs(div5, div2)) {
                    console.log('Venusaur is selected');
                    Touching = 'Venusaur';
                } else if (findTouchingDivs(div5, div3)) {
                    console.log('Charizard is selected');
                    Touching = 'Charizard';
                } else if (findTouchingDivs(div5, div4)) {
                    console.log('Blastoise is selected');
                    Touching = 'Blastoise';
                }

                // Update the final selection on the UI
                document.getElementById('cardname').innerHTML = Touching;

                // Re-enable the button after the animation finishes
                button.prop('disabled', false);

            } else {
                console.error('Error:', data.message);
                button.prop('disabled', false); // Re-enable the button if there's an error
            }
        })
        .catch(error => {
            console.error('Error:', error);
            button.prop('disabled', false); // Re-enable the button if there's an error
        });

    // Slide animation and duplication logic
    const scrollers = document.querySelectorAll('.slider');
    if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
        addAnimation();
    }

    function addAnimation(){
        scrollers.forEach(scroller => {
            scroller.setAttribute('data-animated', true);
        });
    };

    const scrollerInner = document.querySelector('.slider');
    const scrollerContent = Array.from(scrollerInner.children);

    scrollerContent.forEach(item =>{
        const duplicatedItem = item.cloneNode(true);
        duplicatedItem.setAttribute('aria-hidden', true);
        scrollerInner.appendChild(duplicatedItem);
    });

    // Popup box logic
    setTimeout(function() {
        popup.style.display = 'block';
    }, 9000);

    const closeButton = document.querySelector('.close');
    closeButton.addEventListener('click', function() {
        popup.style.display = 'none';
    });

    // Function to find touching divs
    function findTouchingDivs() {
        const divs = document.querySelectorAll('.card');
        const touchingDivs = [];

        for (let i = 0; i < divs.length; i++) {
            const div1 = divs[i];

            for (let j = i + 1; j < divs.length; j++) {
                const div2 = divs[j];

                const rect1 = div1.getBoundingClientRect();
                const rect2 = div2.getBoundingClientRect();

                if (!(rect1.right < rect2.left ||
                    rect1.left > rect2.right ||
                    rect1.bottom < rect2.top ||
                    rect1.top > rect2.bottom)) {
                    touchingDivs.push([div1, div2]);
                }
            }
        }

        return touchingDivs;
    }
});

// Function to render the choice details in the UI
function renderChoiceDetails(choice) {
    // Update the text fields with the choice data
    document.getElementById('choice-id').innerText = `Selected Choice ID: ${choice.choice_id || 'N/A'}`;
    document.getElementById('choice-text').innerText = `Selected Choice Text: ${choice.choice_text || 'N/A'}`;
    document.getElementById('choice-color').innerText = `Selected Choice Color: ${choice.choice_color || 'N/A'}`;

    // Handle the image field
    const choiceFileElement = document.getElementById('choice-file');
    if (choice.choice_file) {
        choiceFileElement.src = choice.choice_file; // Set the image source
        choiceFileElement.style.display = 'block'; // Display the image if available
    } else {
        choiceFileElement.style.display = 'none'; // Hide the image if not available
    }
}

// Function to make the AJAX request
function createOutcome(gameId, slug) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    return fetch(`/your-url/${slug}/create_outcome/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: new URLSearchParams({
            'game_id': gameId
        })
    })
    .then(response => response.json());
}
