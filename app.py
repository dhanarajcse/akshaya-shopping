import streamlit as st

st.set_page_config(page_title="JP Aadhitya Consultancy", layout="wide")

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
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        color: white;
        padding: 30px 15px;
        text-align: center;
    }

    header h1 {
        font-size: 26px;
    }

    header p {
        font-size: 14px;
        margin-top: 5px;
    }

    nav {
        background: #34495e;
        padding: 10px;
        text-align: center;
    }

    nav a {
        color: white;
        margin: 5px 10px;
        text-decoration: none;
        font-size: 14px;
        display: inline-block;
    }

    .container {
        width: 100%;
        max-width: 900px;
        margin: auto;
        padding: 15px;
    }

    .card {
        background: white;
        padding: 15px;
        margin: 15px 0;
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }

    h2 {
        font-size: 18px;
        margin-bottom: 10px;
        color: #2c3e50;
    }

    p, li {
        font-size: 14px;
        line-height: 1.5;
    }

    ul {
        padding-left: 15px;
    }

    .whatsapp {
        display: block;
        text-align: center;
        margin-top: 15px;
        padding: 10px;
        background: #25D366;
        color: white;
        border-radius: 6px;
        text-decoration: none;
        font-size: 14px;
    }

    /* Desktop view */
    @media (min-width: 768px) {
        header h1 {
            font-size: 36px;
        }

        header p {
            font-size: 18px;
        }

        nav a {
            font-size: 16px;
        }

        .card {
            padding: 20px;
        }
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

# Increased height and enabled scrolling
st.components.v1.html(html_code, height=1200, scrolling=True)