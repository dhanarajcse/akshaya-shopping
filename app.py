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
        background:linear-gradient(135deg,#ff6b35,#f7931e);
        color:white;
        text-align:center;
        padding:30px 20px;
    }

    header h1{
        margin-bottom:8px;
        font-size: 2.5rem;
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
        color:#e67e22;
        font-weight:bold;
    }

    .policy-section {
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid #eee;
    }

    .policy-section:last-child {
        border-bottom: none;
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
        background:linear-gradient(135deg,#ff6b35,#f7931e);
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

    iframe { border: none; border-radius: 10px; }
</style>

<script>
function showPage(id) {
    var pages = document.getElementsByClassName("page");
    for(var i=0; i<pages.length; i++) {
        pages[i].classList.remove("active");
    }
    document.getElementById(id).classList.add("active");
    window.scrollTo(0, 0);
}
</script>
</head>

<body>

<header>
    <h1>🛍️ Akshaya Shopping</h1>
    <p>Your One-Stop Destination for Quality Products</p>
</header>

<nav>
    <a onclick="showPage('home')">Home</a>
    <a onclick="showPage('products')">Products</a>
    <a onclick="showPage('contact')">Contact</a>
    <a onclick="showPage('policies')">Policies</a>
    <a onclick="showPage('shipping')">Shipping</a>
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

    <!-- PRODUCTS PAGE (10 PRODUCTS) -->
    <div id="products" class="page">
        <div class="card">
            <h2 style="text-align:center; font-size:32px; margin-bottom:10px;">🛒 Featured Products</h2>
            <p style="text-align:center; color:#666; margin-bottom:25px;">Best Selling Products at Affordable Prices</p>

            <div class="products-grid">
                
                <!-- Product 1: Rice -->
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
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 2: Sunflower Oil -->
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
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 3: Coffee Powder -->
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
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 4: Whole Wheat Atta -->
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
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 5: Toor Dal -->
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
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 6: Herbal Soap -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge purple">ORGANIC</span>
                        <img src="https://images.unsplash.com/photo-1607006342411-9a3363e63945?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🧼 Herbal Bath Soap (Pack of 3)</div>
                            <div class="product-desc">Enriched with natural Neem, Turmeric, and Aloe Vera extracts for healthy skin protection.</div>
                        </div>
                        <div>
                            <div class="price">₹145</div>
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 7: Bamboo Toothbrushes -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge blue">ECO-FRIENDLY</span>
                        <img src="https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🪥 Bamboo Toothbrush (Pack of 4)</div>
                            <div class="product-desc">100% biodegradable organic handles coupled with charcoal infused soft bristles.</div>
                        </div>
                        <div>
                            <div class="price">₹199</div>
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 8: Smart LED Bulb -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge purple">TOP RATED</span>
                        <img src="https://images.unsplash.com/photo-1550537687-c91072c4792d?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🔌 Smart LED Bulb 9W</div>
                            <div class="product-desc">Energy-saving bright white light built to optimize dynamic household consumption.</div>
                        </div>
                        <div>
                            <div class="price">₹249</div>
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 9: Coconut Hair Oil -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge">100% PURE</span>
                        <img src="https://images.unsplash.com/photo-1621263764928-df1444c5e859?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🧴 Pure Coconut Hair Oil - 500ml</div>
                            <div class="product-desc">Naturally processed, cold-pressed premium hair oil for deeper nourishment.</div>
                        </div>
                        <div>
                            <div class="price">₹210</div>
                            <button class="buy-btn">View Product</button>
                        </div>
                    </div>
                </div>

                <!-- Product 10: Assam Tea Powder -->
                <div class="product">
                    <div class="product-wrapper">
                        <span class="badge red">LIMITED STOCK</span>
                        <img src="https://images.unsplash.com/photo-1597481499750-3e6b22637e12?auto=format&fit=crop&w=600&q=80">
                    </div>
                    <div class="product-content">
                        <div class="product-details">
                            <div class="product-title">🍵 Assam CTC Tea Powder - 500g</div>
                            <div class="product-desc">Rich, strong aroma directly sourced from premium handpicked Assam tea estates.</div>
                        </div>
                        <div>
                            <div class="price">₹165</div>
                            <button class="buy-btn">View Product</button>
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

    <!-- POLICIES PAGE -->
    <div id="policies" class="page">
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
        </div>
    </div>

    <!-- SHIPPING PAGE -->
    <div id="shipping" class="page">
        <div class="card">
            <h2>Shipping & Delivery Policy</h2>
            <br>
            <p>Orders are processed within 1 to 3 business days.</p>
            <p>Delivery timelines depend on customer location and courier service.</p>
            <p>Customers will be informed in case of shipment delays.</p>
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
    height=1350,
    scrolling=True
)