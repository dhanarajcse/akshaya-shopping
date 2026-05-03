import streamlit as st

st.set_page_config(page_title="JP Aadhitya Consultancy", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
    html {
        scroll-behavior: smooth;
    }

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
        padding: 25px 10px;
        text-align: center;
    }

    header h1 {
        font-size: 24px;
    }

    header p {
        font-size: 14px;
        margin-top: 5px;
    }

    nav {
        background: #34495e;
        padding: 10px;
        text-align: center;
        position: sticky;
        top: 0;
    }

    nav a {
        color: white;
        margin: 5px 10px;
        text-decoration: none;
        font-size: 14px;
        display: inline-block;
    }

    nav a:hover {
        color: #1abc9c;
    }

    .container {
        width: 100%;
        max-width: 900px;
        margin: auto;
        padding: 10px;
    }

    .card {
        background: white;
        padding: 15px;
        margin: 12px 0;
        border-radius: 12px;
        box-shadow: 0 5px 12px rgba(0,0,0,0.1);
    }

    h2 {
        font-size: 18px;
        margin-bottom: 8px;
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
        margin-top: 12px;
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
            font-size: 34px;
        }

        header p {
            font-size: 18px;
        }

        nav a {
            font-size: 15px;
        }

        .card {
            padding: 20px;
        }
    }
</style>

</head>

<body>

<header id="home">
    <h1>J P Aadhitya Murugan</h1>
    <p>Real Estate | Insurance | Investment Consultant</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
</nav>

<div class="container">

    <div class="card">
        <h2>About</h2>
        <p>
            Experienced professional offering trusted services in real estate,
            insurance, and investment consulting.
        </p>
    </div>

    <div class="card" id="services">
        <h2>Services</h2>
        <ul>
            <li>🏡 Real Estate Buying & Selling</li>
            <li>📄 Insurance Planning & Policies</li>
            <li>💹 Investment & Financial Guidance</li>
        </ul>
    </div>

    <div class="card" id="contact">
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

st.components.v1.html(html_code, height=750, scrolling=True)