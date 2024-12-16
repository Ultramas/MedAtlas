/*global gettext*/
'use strict';
{
    window.addEventListener('load', function() {
        // Show all collapsible fieldsets by default
        const fieldsets = document.querySelectorAll('fieldset.collapse');
        for (const elem of fieldsets) {
            // Ensure fieldset is expanded by removing the 'collapsed' class
            elem.classList.remove('collapsed');

            const h2 = elem.querySelector('h2');
            const link = document.createElement('a');
            link.className = 'collapse-toggle';
            link.href = '#';
            link.textContent = gettext('Hide');
            h2.appendChild(document.createTextNode(' ('));
            h2.appendChild(link);
            h2.appendChild(document.createTextNode(')'));
        }

        // Add toggle to hide/show anchor tag
        const toggleFunc = function(ev) {
            if (ev.target.matches('.collapse-toggle')) {
                ev.preventDefault();
                ev.stopPropagation();
                const fieldset = ev.target.closest('fieldset');
                if (fieldset.classList.contains('collapsed')) {
                    // Show
                    ev.target.textContent = gettext('Hide');
                    fieldset.classList.remove('collapsed');
                } else {
                    // Hide
                    ev.target.textContent = gettext('Show');
                    fieldset.classList.add('collapsed');
                }
            }
        };

        // Enable toggle functionality for fieldsets
        document.querySelectorAll('fieldset.module').forEach(function(el) {
            el.addEventListener('click', toggleFunc);
        });
    });
}
