// main.js — Global JS functions

// Live search for products (used in billing page)
function initProductSearch() {
    const searchInput = document.getElementById('product-search');
    const resultsDiv = document.getElementById('search-results');
    
    if (!searchInput || !resultsDiv) return;

    searchInput.addEventListener('input', function() {
        const query = this.value.trim();
        if (query.length < 2) {
            resultsDiv.innerHTML = '';
            return;
        }

        fetch(`/search/products/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = '';
                if (data.results.length === 0) {
                    resultsDiv.innerHTML = '<div class="p-2 text-muted">No products found</div>';
                    return;
                }
                
                data.results.forEach(product => {
                    const div = document.createElement('div');
                    div.className = 'p-2 border-bottom cursor-pointer hover:bg-light';
                    div.style.cursor = 'pointer';
                    div.innerHTML = `
                        <strong>${product.name}</strong><br>
                        <small>SKU: ${product.sku} | $${product.price.toFixed(2)}</small>
                    `;
                    div.onclick = function() {
                        addToCart(product.id, product.name, product.price);
                        searchInput.value = '';
                        resultsDiv.innerHTML = '';
                    };
                    resultsDiv.appendChild(div);
                });
            })
            .catch(error => {
                console.error('Search error:', error);
                resultsDiv.innerHTML = '<div class="p-2 text-danger">Search failed</div>';
            });
    });
}

// Mobile menu toggle
function initMobileMenu() {
    const toggleButton = document.querySelector('[data-bs-toggle="offcanvas"]');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            const offcanvas = document.getElementById('sidebar');
            if (offcanvas) {
                const bsOffcanvas = new bootstrap.Offcanvas(offcanvas);
                bsOffcanvas.show();
            }
        });
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initProductSearch();
    initMobileMenu();
});