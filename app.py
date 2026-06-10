import streamlit as st

st.set_page_config(page_title="Akshaya Shopping, Thalaivasal", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Segoe UI', sans-serif;
    }

    body {
        background: linear-gradient(to right, #eef2f3, #dfe9f3);
    }

    header {
        background: linear-gradient(135deg, #ff6b35, #f7931e);
        color: white;
        padding: 20px;
        text-align: center;
    }

    nav {
        background: #2c3e50;
        padding: 10px;
        text-align: center;
    }

    nav a {
        color: white;
        margin: 0 15px;
        text-decoration: none;
        cursor: pointer;
    }

    nav a:hover {
        color: #f39c12;
    }

    .container {
        max-width: 900px;
        margin: auto;
        padding: 10px;
    }

    .card {
        background: white;
        padding: 15px;
        margin-top: 10px;
        border-radius: 12px;
        box-shadow: 0 5px 12px rgba(0,0,0,0.1);
    }

    .page {
        display: none;
    }

    .active {
        display: block;
    }

    iframe {
        border-radius: 10px;
    }

    .highlight {
        color: #e67e22;
        font-weight: bold;
    }
</style>

<script>
function showPage(id) {
    var pages = document.getElementsByClassName("page");
    for (var i = 0; i < pages.length; i++) {
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
    <a onclick="showPage('about')">Home</a>
    <a onclick="showPage('products')">Products</a>
    <a onclick="showPage('contact')">Contact</a>
</nav>

<div class="container">

    <!-- HOME -->
    <div id="about" class="page active">
        <div class="card">
            <h2>Welcome to Akshaya Shopping</h2>
            <br/>

            <p>
                <span class="highlight">Akshaya Shopping</span> is committed to providing
                high-quality products at affordable prices. We offer a wide range of
                household items, groceries, fashion accessories, electronics, and daily essentials.
            </p>

            <br/>

            <p>
                Our mission is to make shopping simple, convenient, and enjoyable for every customer.
                We focus on quality, customer satisfaction, and reliable service.
            </p>

            <br/>

            <p>
                Whether you're looking for everyday essentials or special products,
                Akshaya Shopping is here to serve your needs with trust and value.
            </p>
        </div>
    </div>

    <!-- PRODUCTS -->
    <div id="products" class="page">
        <div class="card">
            <h2>Our Product Categories</h2>

            <br/>

            <h3>🛒 Grocery & Daily Essentials</h3>
            <p>
                Fresh groceries, packaged foods, beverages, personal care products,
                and household necessities.
            </p>

            <br/>

            <h3>👕 Fashion & Accessories</h3>
            <p>
                Men's, women's, and children's clothing along with footwear,
                bags, and fashion accessories.
            </p>

            <br/>

            <h3>📱 Electronics & Gadgets</h3>
            <p>
                Mobile accessories, small electronic devices,
                and useful gadgets for everyday life.
            </p>

            <br/>

            <h3>🏠 Home & Kitchen</h3>
            <p>
                Kitchen appliances, cookware, storage solutions,
                home décor, and utility products.
            </p>
        </div>
    </div>

    <!-- CONTACT -->
    <div id="contact" class="page">
        <div class="card">
            <h2>Contact Us</h2>

            <br/>

            <p>📞 +91-9843051071</p>
            <p>📧 info@akshayashopping.com</p>
            <p>📍 Akshaya Shopping</p>
            <p>📍 Salem, Tamil Nadu</p>

            <br/>

            <a href="https://wa.me/919843051071"
               target="_blank"
               style="
               display:inline-block;
               background:#25D366;
               color:white;
               padding:10px 15px;
               border-radius:6px;
               text-decoration:none;
               font-weight:bold;">
               💬 Chat on WhatsApp
            </a>

            <br/><br/>

            <div style="margin-top:10px;">
                <iframe
                    src="https://www.google.com/maps?q=11.585151235000122,78.74966547973798&z=14&output=embed"
                    width="100%"
                    height="250">
                </iframe>
            </div>

        </div>
    </div>

</div>

</body>
</html>
"""

st.components.v1.html(html_code, height=700, scrolling=False)