(function($) {
    $(document).ready(function() {
        // Get references to the fields
        var $dailyField = $('#id_daily');
        var $unlockingLevelField = $('.field-unlocking_level');

        // Function to toggle visibility of unlocking_level
        function toggleUnlockingLevel() {
            if ($dailyField.is(':checked')) {
                $unlockingLevelField.show();
            } else {
                $unlockingLevelField.hide();
            }
        }

        // Run on page load
        toggleUnlockingLevel();

        // Bind change event to the daily field
        $dailyField.change(toggleUnlockingLevel);
    });
})(django.jQuery);
