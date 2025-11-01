// cart.js
let cart = [];

function addToCart(productId, productName, price) {
    const qtyInput = document.getElementById(`qty-${productId}`);
    const qty = parseInt(qtyInput.value) || 1;
    
    if (qty <= 0) {
        alert("Quantity must be at least 1");
        qtyInput.value = 1;
        return;
    }

    const existing = cart.find(item => item.product_id === productId);
    
    if (existing) {
        existing.quantity += qty;
    } else {
        cart.push({
            product_id: productId,
            product_name: productName,
            unit_price: parseFloat(price),
            quantity: qty
        });
    }
    
    qtyInput.value = 1; // Reset input
    updateCart();
}

function updateCart() {
    const tbody = document.getElementById('cart-items');
    const totalElement = document.getElementById('grand-total');
    
    if (!tbody || !totalElement) return;

    tbody.innerHTML = '';
    let total = 0;

    cart.forEach((item, index) => {
        const subtotal = item.unit_price * item.quantity;
        total += subtotal;
        tbody.innerHTML += `
            <tr>
                <td>${item.product_name}</td>
                <td>$${item.unit_price.toFixed(2)}</td>
                <td>
                    <input type="number" min="1" value="${item.quantity}" 
                           onchange="updateCartItem(${index}, this.value)" class="form-control form-control-sm w-50 d-inline">
                </td>
                <td>$${subtotal.toFixed(2)}</td>
                <td><button class="btn btn-sm btn-danger" onclick="removeFromCart(${index})">Remove</button></td>
            </tr>
        `;
    });

    totalElement.innerText = total.toFixed(2);
}

function updateCartItem(index, newQty) {
    if (newQty <= 0) return;
    cart[index].quantity = parseInt(newQty);
    updateCart();
}

function removeFromCart(index) {
    cart.splice(index, 1);
    updateCart();
}

function generateInvoice() {
    if (cart.length === 0) {
        alert("Please add at least one product to cart!");
        return;
    }

    const customerData = {
        name: document.getElementById('customer-name')?.value || '',
        phone: document.getElementById('customer-phone')?.value || '',
        email: document.getElementById('customer-email')?.value || '',
        address: document.getElementById('customer-address')?.value || ''
    };

    if (customerData.phone.trim() === '' && customerData.name.trim() !== '') {
        alert("Phone number is required if providing customer details.");
        return;
    }

    const data = {
        customer: customerData,
        items: cart.map(item => ({
            product_id: item.product_id,
            quantity: item.quantity,
            unit_price: item.unit_price,
            subtotal: item.unit_price * item.quantity
        })),
        total_amount: parseFloat(document.getElementById('grand-total').innerText),
        payment_method: document.getElementById('payment-method').value
    };

    fetch('', {  // POST to same URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Invoice generated successfully!");
            window.location.href = `/invoice/${data.sale_id}/print/`;
        } else {
            alert("Error generating invoice: " + (data.error || "Unknown error"));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Network error. Please try again.");
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('cart-items')) {
        updateCart();
    }
});