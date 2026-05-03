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
        padding: 20px;
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
        cursor: pointer;
    }

    nav a:hover {
        color: #1abc9c;
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
    <h1>J P Aadhitya Murugan</h1>
    <p>Real Estate | Insurance | Investment Consultant</p>
</header>

<nav>
    <a onclick="showPage('about')">Home</a>
    <a onclick="showPage('services')">Services</a>
    <a onclick="showPage('contact')">Contact</a>
</nav>

<div class="container">

    <!-- ABOUT -->
    <div id="about" class="page active">
        <div class="card">
            <h2>About</h2>
            <br/>
            <p>
                J P Aadhitya Murugan, M.Sc, B.Ed., is a dedicated and experienced professional 
                specializing in real estate, insurance planning, and investment consulting. 
                With a strong academic background and a commitment to excellence, he provides 
                reliable and result-oriented guidance to individuals and families.
            </p>
             <br/>
            
            <p>
                He believes in building long-term relationships based on trust, transparency, 
                and professionalism. His approach focuses on understanding each client’s unique 
                needs and delivering customized solutions that ensure financial security and growth.
            </p>
              <br/>
            <p>
                With in-depth knowledge of market trends and financial planning, he empowers 
                clients to make confident decisions in property investments, insurance coverage, 
                and wealth management.
            </p>
        </div>
    </div>

    <!-- SERVICES -->
    <div id="services" class="page">
        <div class="card">
            <h2>Services</h2>
<br/>
            <h3>🏡 Real Estate Services</h3>
            <p>
                We provide complete support for buying, selling, and investing in properties.
                From identifying the right opportunities to handling documentation, we ensure
                a smooth and transparent process.
            </p>
             <br/>

            <h3>📄 Insurance Planning & Policies</h3>
            <p>
                We offer tailored insurance solutions to protect your future and secure your family.
                Our services include policy selection and choosing the right coverage.
            </p>
              <br/>
            <h3>💹 Investment & Financial Guidance</h3>
            <p>
                We help clients build and manage their wealth through strategic financial planning
                and long-term investment strategies.
            </p>
        </div>
    </div>

    <!-- CONTACT -->
    <div id="contact" class="page">
        <div class="card">
            <h2>Contact</h2>
            <br/>
            <p>📞 +91-8667250719</p>
            <p>📧 jprajkamal@gmail.com</p>
            <p>📍 Attur, Salem District, Tamil Nadu</p>

         <a href="https://wa.me/918667250719" target="_blank" style="
            display:inline-block;
            background:#25D366;
            color:white;
            padding:10px 15px;
            border-radius:6px;
            text-decoration:none;
            font-weight:bold;">
            💬 Chat on WhatsApp
        </a>
  <br/> <br/>
            <div style="margin-top:10px;">
                <iframe
                    src="https://www.google.com/maps?q=11.648245,78.510139&z=14&output=embed"
                    width="100%"
                    height="200">
                </iframe>
            </div>
        </div>
    </div>

</div>

</body>
</html>
"""

# Fixed height → NO SCROLLBAR
st.components.v1.html(html_code, height=700, scrolling=False)