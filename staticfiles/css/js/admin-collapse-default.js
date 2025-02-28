(function($) {
    $(document).ready(function() {
        // Remove 'collapse' class to make the fieldset open by default
        $('.collapse').removeClass('collapse');

        // Add a click event to toggle the 'collapse' class when the fieldset's legend is clicked
        $('.collapse fieldset legend').on('click', function() {
            $(this).parent().toggleClass('collapse');
        });
    });
})(django.jQuery);
