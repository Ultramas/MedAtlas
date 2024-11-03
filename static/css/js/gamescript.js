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

function createOutcome(gameId, slug) {
    return $.ajax({
        url: `/create_outcome/${slug}/`,  // Use the correct endpoint for your route
        method: 'POST',
        data: { game_id: gameId },
        dataType: 'json'
    });
}

// Call the function when needed
createOutcome(button.data('game-id'), button.data('slug'))
    .then(data => {
        console.log('AJAX Response:', data);
        if (data.status === 'success') {
            // Display choice details in the template
            document.getElementById('choice-id').innerText = `Choice ID: ${data.choice_id}`;
            document.getElementById('choice-text').innerText = `Choice Text: ${data.choice_text}`;
            document.getElementById('choice-color').innerText = `Choice Color: ${data.choice_color}`;

            const choiceImage = document.getElementById('choice-file');
            if (data.choice_file) {
                choiceImage.src = data.choice_file;
                choiceImage.style.display = 'block'; // Show image if file URL exists
            } else {
                choiceImage.style.display = 'none'; // Hide if no file URL
            }

            // Enable button if needed
            button.prop('disabled', false);
        } else {
            console.error('Error:', data.message);
            button.prop('disabled', false); // Re-enable button on error
        }
    })
    .catch(error => {
        console.error('Error:', error);
        button.prop('disabled', false); // Re-enable button on error
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
    console.log('Rendering Choice:', choice); // Log choice details to verify data

    document.getElementById('choice-id').innerText = `Selected Choice ID: ${choice.choice_id || 'N/A'}`;
    document.getElementById('choice-text').innerText = `Selected Choice Text: ${choice.choice_text || 'N/A'}`;
    document.getElementById('choice-color').innerText = `Selected Choice Color: ${choice.choice_color || 'N/A'}`;

    const choiceFileElement = document.getElementById('choice-file');
    if (choice.choice_file) {
        choiceFileElement.src = choice.choice_file;
        choiceFileElement.style.display = 'block';
    } else {
        choiceFileElement.style.display = 'none';
    }
}

