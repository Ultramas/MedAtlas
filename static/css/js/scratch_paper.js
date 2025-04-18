document.getElementById('sell-everything-button').addEventListener('click', function() {
    if (confirm('Are you sure you want to sell all inventory items?')) {
        fetch("{% url 'showcase:sell_everything_inventory_objects' %}", {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
                'Content-Type': 'application/json',
            },
            credentials: 'same-origin',
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response data:', data);
            if (data.success) {
                console.log('Updating inventory...');
                document.getElementById('inventory-items-container').innerHTML = data.inventory_html;
                console.log('Inventory updated:', document.getElementById('inventory-items-container').innerHTML);
                document.getElementById('stock-count').textContent = data.stock_count;
                if (data.currency_amount) {
                    const currencyElement = document.getElementById('sellupdate');
                    if (currencyElement) {
                        currencyElement.textContent = data.currency_amount;
                    } else {
                        console.log('Currency element not found');
                    }
                }
                if (data.total_value) {
                    document.getElementById('total_value_element').textContent = data.total_value;
                }
            } else {
                console.log('Error:', data.error);
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            alert('An error occurred while processing your request.');
        });
    }
});