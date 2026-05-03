import streamlit as st

st.set_page_config(page_title="JP Aadhitya Consultancy", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #eef2f3, #dfe9f3);
    }

    html, body {
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    header {
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        color: white;
        padding: 40px;
        text-align: center;
    }

    nav {
        background: #34495e;
        padding: 10px;
        text-align: center;
    }

    nav a {
        color: white;
        margin: 0 15px;
        text-decoration: none;
        font-weight: bold;
    }

    .container {
        max-width: 900px;
        margin: auto;
        padding: 20px;
    }

    .card {
        background: white;
        padding: 20px;
        margin: 20px 0;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    .whatsapp {
        background: #25D366;
        color: white;
        padding: 10px 15px;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
    }
</style>
</head>

<body>

<header>
    <h1>J P Aadhitya Murugan</h1>
    <p>Real Estate | Insurance | Investment Consultant</p>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">Services</a>
    <a href="#">Contact</a>
</nav>

<div class="container">

    <div class="card">
        <h2>About</h2>
        <p>Experienced professional offering trusted services in real estate, insurance, and investment consulting.</p>
    </div>

    <div class="card">
        <h2>Services</h2>
        <ul>
            <li>🏡 Real Estate Buying & Selling</li>
            <li>📄 Insurance Planning & Policies</li>
            <li>💹 Investment & Financial Guidance</li>
        </ul>
    </div>

    <div class="card">
        <h2>Contact</h2>
        <p>📞 +91-8667250719</p>
        <p>📧 jprajkamal@gmail.com</p>
        <a class="whatsapp" href="https://wa.me/918667250719" target="_blank">
            Chat on WhatsApp
        </a>
    </div>

</div>

</body>
</html>
"""

st.components.v1.html(html_code, height=900, scrolling=False)