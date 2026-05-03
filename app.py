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
        position: sticky;
        top: 0;
    }

    nav a {
        color: white;
        margin: 5px 10px;
        text-decoration: none;
        font-size: 14px;
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
        font-size: 20px;
        margin-bottom: 10px;
        color: #2c3e50;
    }

    h3 {
        margin-top: 10px;
        font-size: 16px;
        color: #34495e;
    }

    p, li {
        font-size: 14px;
        line-height: 1.6;
    }

    ul {
        padding-left: 15px;
        margin-top: 5px;
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
    }

    iframe {
        border-radius: 10px;
    }

    @media (min-width: 768px) {
        header h1 { font-size: 36px; }
        header p { font-size: 18px; }
        nav a { font-size: 15px; }
        .card { padding: 20px; }
    }
</style>

</head>

<body>

<header id="home">
    <h1>J P Aadhitya Murugan</h1>
    <p>M.Sc, B.Ed | Real Estate | Insurance | Investment Consultant</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#services">Services</a>
    <a href="#contact">Contact</a>
</nav>

<div class="container">

    <!-- ABOUT -->
    <div class="card">
        <h2>About</h2>
        <p>
            J P Aadhitya Murugan, M.Sc, B.Ed., is a dedicated and experienced professional 
            specializing in real estate, insurance planning, and investment consulting. 
            With a strong academic background and a commitment to excellence, he provides 
            reliable and result-oriented guidance to individuals and families.
        </p>
        <p>
            He believes in building long-term relationships based on trust, transparency, 
            and professionalism. His approach focuses on understanding each client’s unique 
            needs and delivering customized solutions that ensure financial security and growth.
        </p>
        <p>
            With in-depth knowledge of market trends and financial planning, he empowers 
            clients to make confident decisions in property investments, insurance coverage, 
            and wealth management.
        </p>
    </div>

    <!-- SERVICES -->
    <div class="card" id="services">
        <h2>Services</h2>

        <h3>🏡 Real Estate Services</h3>
        <p>
            We provide complete support for buying, selling, and investing in properties. 
            From identifying the right opportunities to handling documentation, we ensure 
            a smooth and transparent process.
        </p>

        <h3>📄 Insurance Planning & Policies</h3>
        <p>
            We offer tailored insurance solutions to protect your future and secure your family. 
            Our services include policy selection, comparison, and assistance in choosing the 
            right coverage based on your needs.
        </p>

        <h3>💹 Investment & Financial Guidance</h3>
        <p>
            We help clients build and manage their wealth through strategic financial planning. 
            Our guidance includes investment strategies, risk assessment, and long-term financial 
            planning to achieve sustainable growth.
        </p>

        <h3>⭐ Why Choose Us?</h3>
        <ul>
            <li>Trusted and professional service</li>
            <li>Personalized consultation</li>
            <li>Transparent process</li>
            <li>End-to-end support</li>
            <li>Long-term client relationships</li>
        </ul>
    </div>

    <!-- CONTACT -->
    <div class="card" id="contact">
        <h2>Contact</h2>
        <p>
            We are here to assist you with all your real estate, insurance, and investment needs.
            Feel free to reach out for personalized consultation and expert guidance.
        </p>

        <p>📞 +91-8667250719</p>
        <p>📧 jprajkamal@gmail.com</p>
        <p>📍 Attur, Salem District, Tamil Nadu</p>

        <a class="whatsapp" href="https://wa.me/918667250719" target="_blank">
            💬 Chat on WhatsApp
        </a>

        <div style="margin-top:15px;">
            <iframe
                src="https://www.google.com/maps?q=11.5941,78.6014&z=14&output=embed"
                width="100%"
                height="250"
                loading="lazy">
            </iframe>
        </div>
    </div>

</div>

</body>
</html>
"""

st.components.v1.html(html_code, height=900, scrolling=True)