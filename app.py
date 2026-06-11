import streamlit as st

st.set_page_config(
    page_title="Akshaya Shopping - Thalaivasal",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Razorpay Checkout Script Integration -->
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>

<style>
    *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body{
        background:#f5f7fa;
        color: #333;
    }

    header{
        background:linear-gradient(135deg,#27ae60,#2ecc71);
        color:white;
        text-align:center;
        padding:35px 20px 25px 20px;
    }

    .logo-container {
        max-width: 350px;
        margin: 0 auto;
    }

    nav{
        background:#2c3e50;
        padding:15px;
        text-align:center;
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    nav a{
        color:white;
        margin:0 15px;
        text-decoration:none;
        cursor:pointer;
        font-size:16px;
        transition: color 0.2s ease;
    }

    nav a:hover{
        color:#f39c12;
    }

    .container{
        max-width:1200px;
        margin:auto;
        padding:20px;
    }

    .card{
        background:white;
        padding:25px;
        margin-top:20px;
        border-radius:12px;
        box-shadow:0 4px 15px rgba(0,0,0,0.05);
    }

    .page{
        display:none;
    }

    .active{
        display:block;
    }

    .highlight{
        color:#27ae60;
        font-weight:bold;
    }

    .policy-section {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
    }

    .policy-section:last-child {
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    footer{
        background:#2c3e50;
        color:white;
        text-align:center;
        padding:25px;
        margin-top:40px;
    }

    .products-grid{
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
        gap:25px;
        margin-top:20px;
    }

    .product{
        background:white;
        border-radius:18px;
        overflow:hidden;
        box-shadow:0 10px 25px rgba(0,0,0,0.06);
        transition:all 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .product:hover{
        transform:translateY(-8px);
        box-shadow:0 20px 35px rgba(0,0,0,0.12);
    }

    .product img{
        width:100%;
        height:200px;
        object-fit:cover;
    }

    .product-content{
        padding:18px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .product-details{
        margin-bottom: 15px;
    }

    .product-title{
        font-size:1.15rem;
        font-weight:700;
        margin-bottom:8px;
    }

    .product-desc{
        font-size:0.9rem; 
        color:#666;
        line-height:1.4;
    }

    .price{
        font-size:24px;
        font-weight:bold;
        color:#ff6b35;
        margin: 10px 0;
    }

    .buy-btn{
        width:100%;
        padding:12px;
        border:none;
        border-radius:10px;
        background:linear-gradient(135deg,#27ae60,#2ecc71);
        color:white;
        font-weight:600;
        cursor:pointer;
        font-size:15px;
        transition: opacity 0.2s;
    }

    .buy-btn:hover{
        opacity:0.9;
    }

    .badge{
        position:absolute;
        top:15px;
        left:15px;
        background:#27ae60;
        color:white;
        padding:6px 12px;
        border-radius:20px;
        font-size:11px;
        font-weight:bold;
        z-index: 10;
    }

    .badge.blue { background: #2980b9; }
    .badge.red { background: #c0392b; }
    .badge.purple { background: #8e44ad; }

    .product-wrapper{
        position:relative;
    }

    .cart-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }

    .cart-table th, .cart-table td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    .cart-table th {
        background-color: #f8f9fa;
        font-weight: 600;
    }

    .cart-total-container {
        text-align: right;
        margin-top: 20px;
        font-size: 1.3rem;
        font-weight: bold;
        color: #ff6b35;
    }

    .checkout-form {
        margin-top: 30px;
        border-top: 2px dashed #ddd;
        padding-top: 20px;
    }

    .form-group {
        margin-bottom: 15px;
    }

    .form-group label {
        display: block;
        margin-bottom: 5px;
        font-weight: 600;
    }

    .form-group input, .form-group textarea, .form-group select {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 6px;
        font-size: 15px;
    }

    .remove-btn {
        background: #e74c3c;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 4px;
        cursor: pointer;
    }

    .remove-btn:hover { background: #c0392b; }

    iframe { border: none; border-radius: 10px; }
</style>

<script>
let cart = [];
let totalAmountInINR = 0;

function showPage(id) {
    var pages = document.getElementsByClassName("page");
    for(var i=0; i<pages.length; i++) {
        pages[i].classList.remove("active");
    }
    document.getElementById(id).classList.add("active");
    window.scrollTo(0, 0);
    
    if (id === 'checkout') {
        renderCart();
    }
}

function addToCart(title, price) {
    const existingItem = cart.find(item => item.title === title);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ title: title, price: price, quantity: 1 });
    }
    updateCartCount();
    alert(title + " added to your cart successfully!");
}

function updateCartCount() {
    const count = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById("cart-nav-link").innerText = "🛒 Cart (" + count + ")";
}

function removeFromCart(index) {
    cart.splice(index, 1);
    updateCartCount();
    renderCart();
}

function renderCart() {
    const cartBody = document.getElementById("cart-items-body");
    const cartContainer = document.getElementById("cart-content-wrapper");
    const emptyMsg = document.getElementById("empty-cart-msg");
    
    if (cart.length === 0) {
        cartContainer.style.display = "none";
        emptyMsg.style.display = "block";
        totalAmountInINR = 0;
        return;
    }
    
    cartContainer.style.display = "block";
    emptyMsg.style.display = "none";
    cartBody.innerHTML = "";
    
    totalAmountInINR = 0;
    
    cart.forEach((item, index) => {
        const itemTotal = item.price * item.quantity;
        totalAmountInINR += itemTotal;
        
        const row = `<tr>
            <td>${item.title}</td>
            <td>₹${item.price}</td>
            <td>${item.quantity}</td>
            <td>₹${itemTotal}</td>
            <td><button class="remove-btn" onclick="removeFromCart(${index})">Remove</button></td>
        </tr>`;
        cartBody.innerHTML += row;
    });
    
    document.getElementById("cart-grand-total").innerText = "₹" + totalAmountInINR;
}

function processCheckout(event) {
    event.preventDefault();
    if (cart.length === 0) {
        alert("Your shopping cart is completely empty!");
        return;
    }
    
    const name = document.getElementById("cust-name").value;
    const phone = document.getElementById("cust-phone").value;
    const address = document.getElementById("cust-address").value;
    const paymentMethod = document.getElementById("cust-payment").value;

    if (paymentMethod === "Cash on Delivery (COD)") {
        alert("Thank you " + name + "! Your COD order has been placed successfully.");
        completeOrderCleanup();
    } else {
        var options = {
            "key": "rzp_test_placeholderKey", 
            "amount": totalAmountInINR * 100, 
            "currency": "INR",
            "name": "Akshaya Shopping",
            "description": "Payment for Merchant Order Secure Portal",
            "image": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?auto=format&fit=crop&w=100&q=80",
            "handler": function (response){
                alert("Payment Successful!\\nRazorpay Transaction ID: " + response.razorpay_payment_id + "\\nYour order has been captured.");
                completeOrderCleanup();
            },
            "prefill": {
                "name": name,
                "contact": phone
            },
            "theme": {
                "color": "#27ae60"
            }
        };
        var rzp1 = new Razorpay(options);
        rzp1.open();
    }
}

function completeOrderCleanup() {
    cart = [];
    updateCartCount();
    document.getElementById("checkout-form-element").reset();
    showPage('home');
}
</script>
</head>

<body>

<header>
    <!-- Vector Custom Branding Logo -->
    <div class="logo-container">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 100" width="100%" height="auto">
          <defs>
            <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ffffff" />
              <stop offset="100%" stop-color="#e8f8f0" />
            </linearGradient>
            <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2ecc71" />
              <stop offset="100%" stop-color="#27ae60" />
            </linearGradient>
          </defs>
          <g transform="translate(10, 5)">
            <path d="M35,35 C35,18 55,18 55,35" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
            <rect x="20" y="35" width="50" height="50" rx="12" fill="url(#logoGrad)" />
            <path d="M45,45 C55,45 55,68 45,75 C35,68 35,45 45,45 Z" fill="url(#leafGrad)" />
            <path d="M45,50 L45,70" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
          </g>
          <text x="90" y="75" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="32" fill="#ffffff" letter-spacing="1">AKSHAYA SHOPPING</text>
       
        </svg>
    </div>
    <p style="margin-top: 8px;">Your One-Stop Destination for Quality Products</p>
</header>

<nav>
    <a onclick="showPage('home')">Home</a>
    <a onclick="showPage('products')">Products</a>
    <a onclick="showPage('contact')">Contact</a>
    <a onclick="showPage('privacy-policy')">Privacy Policy</a>
    <a onclick="showPage('checkout')" id="cart-nav-link" style="font-weight: bold; color: #f39c12;">🛒 Cart (0)</a>
</nav>

<div class="container">

    <!-- HOME PAGE -->
    <div id="home" class="page active">
        <div class="card">
            <h2>Welcome to Akshaya Shopping</h2>
            <br>
            <p><span class="highlight">Akshaya Shopping</span> is committed to providing high-quality products at affordable prices.</p>
            <br>
            <p>We offer groceries, household items, fashion accessories, electronics, home essentials and daily-use products.</p>
            <br>
            <p>Our goal is to provide customers with reliable products, excellent service and secure online payments.</p>
        </div>

        <div class="card">
            <h2>Business Information</h2>
            <br>
            <p><b>Business Name:</b> Akshaya Shopping</p>
            <p><b>Location:</b> Thalaivasal, Salem, Tamil Nadu</p>
            <p><b>Email:</b> info@akshayashopping.com</p>
            <p><b>Phone:</b> +91-9843051071</p>
            <p><b>GSTIN:</b> 33AQWPA5439K1ZH</p>
        </div>
    </div>

    <!-- PRODUCTS PAGE -->
    <div id="products" class="page">
        <div class="card">
            <h2 style="text-align:center; font-size:32px; margin-bottom:10px;">🛒 Featured Products</h2>
            <p style="text-align:center; color:#666; margin-bottom:25px;">Best Selling Products at Affordable Prices</p>

            <div class="products-grid">
                
                <!-- Product 1 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge">BEST SELLER</span>
                        <img src="https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🍚 Premium Rice - 5 KG</div>
                            <div class="product-desc">High-quality traditional premium rice ideal for everyday healthy cooking.</div>
                        </div>
                        <div>
                            <div class="price">₹450</div>
                            <button class="buy-btn" onclick="addToCart('Premium Rice - 5 KG', 450)">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge red">HOT DEAL</span>
                        <img src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🛢️ Sunflower Oil - 1L</div>
                            <div class="product-desc">Pure, multi-filtered refined sunflower oil rich in natural vitamins.</div>
                        </div>
                        <div>
                            <div class="price">₹160</div>
                            <button class="buy-btn" onclick="addToCart('Sunflower Oil - 1L', 160)">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge blue">NEW</span>
                        <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">☕ Premium Filter Coffee</div>
                            <div class="product-desc">Aromatic fine-ground South Indian blend for a robust and rich morning flavor.</div>
                        </div>
                        <div>
                            <div class="price">₹220</div>
                            <button class="buy-btn" onclick="addToCart('Premium Filter Coffee', 220)">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product 4 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge">POPULAR</span>
                        <img src="https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🌾 Whole Wheat Atta - 5 KG</div>
                            <div class="product-desc">100% pure stone-ground chakki whole wheat flour for ultra soft rotis.</div>
                        </div>
                        <div>
                            <div class="price">₹260</div>
                            <button class="buy-btn" onclick="addToCart('Whole Wheat Atta - 5 KG', 260)">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product 5 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge blue">ESSENTIAL</span>
                        <img src="https://images.unsplash.com/photo-1547058881-aa0edd92aab3?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🍛 Premium Toor Dal - 1 KG</div>
                            <div class="product-desc">Unpolished, protein-dense pulses sorted cleanly for wholesome family meals.</div>
                        </div>
                        <div>
                            <div class="price">₹175</div>
                            <button class="buy-btn" onclick="addToCart('Premium Toor Dal - 1 KG', 175)">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product 6 -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge purple">ORGANIC</span>
                        <img src="https://images.unsplash.com/photo-1605264964528-06403738d6dc?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🧼 Herbal Bath Soap (Pack of 3)</div>
                            <div class="product-desc">Enriched with natural Neem, Turmeric, and Aloe Vera extracts for healthy skin protection.</div>
                        </div>
                        <div>
                            <div class="price">₹145</div>
                            <button class="buy-btn" onclick="addToCart('Herbal Bath Soap (Pack of 3)', 145)">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- CONTACT PAGE -->
    <div id="contact" class="page">
        <div class="card">
            <h2>Contact Us</h2>
            <br>
            <p><b>Phone:</b> +91-9843051071</p>
            <p><b>Email:</b> info@akshayashopping.com</p>
            <p><b>Address:</b> Thalaivasal, Salem, Tamil Nadu, India</p>
            <br>
            <a href="https://wa.me/919843051071" target="_blank" style="display:inline-block; background:#25D366; color:white; padding:10px 20px; text-decoration:none; border-radius:8px; font-weight:600;">
                WhatsApp Us
            </a>
            <br><br>
            <iframe src="https://maps.google.com/maps?q=11.584914462911676,78.74970940723274&z=15&output=embed" width="100%" height="300"></iframe>
        </div>
    </div>

    <!-- PRIVACY POLICY PAGE -->
    <div id="privacy-policy" class="page">
        <div class="card">
            <div class="policy-section">
                <h2>Privacy Policy</h2>
                <br>
                <p>We collect customer information only for order processing, delivery and customer support purposes.</p>
                <p>Customer information will not be sold or shared with third parties except where necessary for order fulfillment or legal compliance.</p>
                <p>For privacy concerns contact: <b>info@akshayashopping.com</b></p>
            </div>

            <div class="policy-section">
                <h2>Terms & Conditions</h2>
                <br>
                <p>By using this website, customers agree to comply with our terms. Product availability and pricing may change without notice.</p>
                <p>Customers are responsible for providing accurate delivery details.</p>
                <p>Akshaya Shopping reserves the right to cancel orders due to stock unavailability or suspected fraudulent activity.</p>
            </div>

            <div class="policy-section">
                <h2>Refund & Cancellation Policy</h2>
                <br>
                <p>Orders can be cancelled before dispatch.</p>
                <p>Refunds will be processed within 7 business days after approval.</p>
                <p>Damaged or incorrect products must be reported within 48 hours of delivery.</p>
            </div>

            <div class="policy-section">
                <h2>Shipping & Delivery Policy</h2>
                <br>
                <p>Orders are processed within 1 to 3 business days.</p>
                <p>Delivery timelines depend on customer location and courier service.</p>
                <p>Customers will be informed in case of shipment delays.</p>
            </div>
        </div>
    </div>

    <!-- CART / CHECKOUT PAGE -->
    <div id="checkout" class="page">
        <div class="card">
            <h2>🛒 Shopping Cart & Checkout</h2>
            
            <div id="empty-cart-msg" style="margin-top: 20px; text-align: center; color: #777;">
                <p style="font-size: 18px;">Your cart is empty.</p>
                <br>
                <button class="buy-btn" style="max-width: 200px;" onclick="showPage('products')">Go Shopping</button>
            </div>

            <div id="cart-content-wrapper" style="display: none;">
                <table class="cart-table">
                    <thead>
                        <tr>
                            <th>Product Details</th>
                            <th>Unit Price</th>
                            <th>Qty</th>
                            <th>Total</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="cart-items-body">
                    </tbody>
                </table>

                <div class="cart-total-container">
                    Grand Total: <span id="cart-grand-total">₹0</span>
                </div>

                <!-- Checkout Shipping Section Form -->
                <div class="checkout-form">
                    <h3>📍 Delivery & Payment Gateway</h3>
                    <br>
                    <form id="checkout-form-element" onsubmit="processCheckout(event)">
                        <div class="form-group">
                            <label for="cust-name">Full Name *</label>
                            <input type="text" id="cust-name" required placeholder="Enter your full name">
                        </div>
                        <div class="form-group">
                            <label for="cust-phone">Contact Mobile Number *</label>
                            <input type="tel" id="cust-phone" required placeholder="Enter 10-digit mobile number">
                        </div>
                        <div class="form-group">
                            <label for="cust-address">Complete Shipping Address *</label>
                            <textarea id="cust-address" rows="3" required placeholder="Street name, landmark, city, pincode"></textarea>
                        </div>
                        <div class="form-group">
                            <label for="cust-payment">Select Payment Method</label>
                            <select id="cust-payment">
                                <option value="Razorpay Portal">Online Secure Payment (UPI, Cards, NetBanking)</option>
                                <option value="Cash on Delivery (COD)">Cash on Delivery (COD)</option>
                            </select>
                        </div>
                        <br>
                        <button type="submit" class="buy-btn" style="font-size: 18px; padding: 15px;">Proceed to Secure Checkout</button>
                    </form>
                </div>
            </div>

        </div>
    </div>
</div>

<footer>
    <p>© 2026 Akshaya Shopping. All Rights Reserved.</p>
</footer>

</body>
</html>
"""

st.components.v1.html(
    html_code,
    height=1450,
    scrolling=True
)