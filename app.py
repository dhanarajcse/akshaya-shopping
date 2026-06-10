import streamlit as st

st.set_page_config(
    page_title="Akshaya Shopping - Thalaivasal",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html>
<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    background:#f5f7fa;
}

header{
    background:linear-gradient(135deg,#ff6b35,#f7931e);
    color:white;
    text-align:center;
    padding:25px;
}

header h1{
    margin-bottom:10px;
}

nav{
    background:#2c3e50;
    padding:15px;
    text-align:center;
}

nav a{
    color:white;
    margin:0 12px;
    text-decoration:none;
    cursor:pointer;
    font-size:15px;
}

nav a:hover{
    color:#f39c12;
}

.container{
    max-width:1000px;
    margin:auto;
    padding:15px;
}

.card{
    background:white;
    padding:20px;
    margin-top:15px;
    border-radius:12px;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

.page{
    display:none;
}

.active{
    display:block;
}

.product{
    border:1px solid #ddd;
    border-radius:10px;
    padding:15px;
    margin-top:15px;
}

.highlight{
    color:#e67e22;
    font-weight:bold;
}

footer{
    background:#2c3e50;
    color:white;
    text-align:center;
    padding:20px;
    margin-top:30px;
}

iframe{
    border-radius:10px;
}

</style>

<script>

function showPage(id)
{
    var pages=document.getElementsByClassName("page");

    for(var i=0;i<pages.length;i++)
    {
        pages[i].classList.remove("active");
    }

    document.getElementById(id).classList.add("active");
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
    <a onclick="showPage('privacy')">Privacy Policy</a>
    <a onclick="showPage('terms')">Terms</a>
    <a onclick="showPage('refund')">Refund Policy</a>
    <a onclick="showPage('shipping')">Shipping</a>
</nav>

<div class="container">

<!-- HOME -->

<div id="home" class="page active">

    <div class="card">

        <h2>Welcome to Akshaya Shopping</h2>

        <br>

        <p>
            <span class="highlight">Akshaya Shopping</span> is committed to
            providing high-quality products at affordable prices.
        </p>

        <br>

        <p>
            We offer groceries, household items, fashion accessories,
            electronics, home essentials and daily-use products.
        </p>

        <br>

        <p>
            Our goal is to provide customers with reliable products,
            excellent service and secure online payments.
        </p>

    </div>

    <div class="card">

        <h2>Business Information</h2>

        <br>

        <p><b>Business Name:</b> Akshaya Shopping</p>
        <p><b>Location:</b> Thalaivasal, Salem, Tamil Nadu</p>
        <p><b>Email:</b> info@akshayashopping.com</p>
        <p><b>Phone:</b> +91-9843051071</p>
        <p><b>GSTIN:</b>33AQWPA5439K1ZH</p>
    </div>

</div>

<!-- PRODUCTS -->

<div id="products" class="page">

    <div class="card">

        <h2>Our Products</h2>

        <div class="product">
            <h3>🍚 Premium Rice - 5 KG</h3>
            <p>High quality rice suitable for daily cooking.</p>
            <p><b>Price:</b> ₹450</p>
        </div>

        <div class="product">
            <h3>🛢️ Sunflower Oil - 1 Litre</h3>
            <p>Refined sunflower cooking oil.</p>
            <p><b>Price:</b> ₹160</p>
        </div>

        <div class="product">
            <h3>☕ Premium Coffee Powder</h3>
            <p>Fresh and aromatic coffee powder.</p>
            <p><b>Price:</b> ₹220</p>
        </div>

        <div class="product">
            <h3>📱 Mobile Accessories</h3>
            <p>Chargers, cables and mobile accessories.</p>
            <p><b>Starting From:</b> ₹99</p>
        </div>

    </div>

</div>

<!-- CONTACT -->

<div id="contact" class="page">

    <div class="card">

        <h2>Contact Us</h2>

        <br>

        <p><b>Business Name:</b> Akshaya Shopping</p>
        <p><b>Phone:</b> +91-9843051071</p>
        <p><b>Email:</b> info@akshayashopping.com</p>
        <p><b>Address:</b> Thalaivasal, Salem, Tamil Nadu, India</p>

        <br>

        <a href="https://wa.me/919843051071"
        target="_blank"
        style="
        display:inline-block;
        background:#25D366;
        color:white;
        padding:10px 15px;
        text-decoration:none;
        border-radius:8px;">
        WhatsApp Us
        </a>

        <br><br>

        <iframe
        src="https://www.google.com/maps?q=11.585151235000122,78.74966547973798&z=14&output=embed"
        width="100%"
        height="250">
        </iframe>

    </div>

</div>

<!-- PRIVACY POLICY -->

<div id="privacy" class="page">

    <div class="card">

        <h2>Privacy Policy</h2>

        <br>

        <p>
        We collect customer information only for order processing,
        delivery and customer support purposes.
        </p>

        <br>

        <p>
        Customer information will not be sold or shared with third parties
        except where necessary for order fulfillment or legal compliance.
        </p>

        <br>

        <p>
        For privacy concerns contact:
        info@akshayashopping.com
        </p>

    </div>

</div>

<!-- TERMS -->

<div id="terms" class="page">

    <div class="card">

        <h2>Terms & Conditions</h2>

        <br>

        <p>
        By using this website, customers agree to comply with our terms.
        Product availability and pricing may change without notice.
        </p>

        <br>

        <p>
        Customers are responsible for providing accurate delivery details.
        </p>

        <br>

        <p>
        Akshaya Shopping reserves the right to cancel orders due to stock
        unavailability or suspected fraudulent activity.
        </p>

    </div>

</div>

<!-- REFUND -->

<div id="refund" class="page">

    <div class="card">

        <h2>Refund & Cancellation Policy</h2>

        <br>

        <p>
        Orders can be cancelled before dispatch.
        </p>

        <br>

        <p>
        Refunds will be processed within 7 business days after approval.
        </p>

        <br>

        <p>
        Damaged or incorrect products must be reported within 48 hours
        of delivery.
        </p>

    </div>

</div>

<!-- SHIPPING -->

<div id="shipping" class="page">

    <div class="card">

        <h2>Shipping & Delivery Policy</h2>

        <br>

        <p>
        Orders are processed within 1 to 3 business days.
        </p>

        <br>

        <p>
        Delivery timelines depend on customer location and courier service.
        </p>

        <br>

        <p>
        Customers will be informed in case of shipment delays.
        </p>

    </div>

</div>

</div>

<footer>

    <p>© 2026 Akshaya Shopping. All Rights Reserved.</p>

    <br>

    <p>
        Privacy Policy |
        Terms & Conditions |
        Refund Policy |
        Shipping Policy
    </p>

</footer>

</body>
</html>
"""

st.components.v1.html(
    html_code,
    height=1200,
    scrolling=True
)