import streamlit as st
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from streamlit_autorefresh import st_autorefresh

# Page Configuration
st.set_page_config(page_title="Ahmad Anim | Portfolio", layout="wide")

# Load profile picture
image_filenames = [
    "img7.jpg", "img6.jpg", "img05.jpg", "img04.jpg",
    "img03.jpg", "img02.jpg"
]

# Titles for images 1 to 4 (assuming these correspond to img1 to img4)
image_titles = {
    "img6.jpg": "The Convocation Day ",
    "img7.jpg": "I am in full formal dress",
    "img05.jpg": "Casual but Not Boring",
    "img04.jpg": "A little glimpse of my place: Lounge",
    "img03.jpg": "A little glimpse of my place: Family Drawing Room",
    "img02.jpg": "A little glimpse of my place: Dining Space"
}

# Autorefresh every 2 seconds (2000 milliseconds)
count = st.session_state.get('count', 0)
refresh = st_autorefresh(interval=3000, limit=None, key="refresh")

# Update count every rerun
count = (count + 1) % len(image_filenames)
st.session_state['count'] = count


# CSS for hover magnification effect on segments and social links
st.markdown("""
    <style>
    .hover-segment {
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out, background-color 0.3s ease-in-out, color 0.3s ease-in-out;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        background-color:#EA8282;
    }
    .hover-segment:hover {
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
        background-color: #FF4B4B;
        color: white;
    }
    .hover-segment:hover h3,
    .hover-segment:hover li,
    .hover-segment:hover p {
        color: white;
    }
    a {
        text-decoration: none;
    }

    .connect-with-me a {
        color: #EA8282;
        text-decoration: none;
        margin-right: 15px;
        font-size: 18px;
    }
    .connect-with-me a:hover {
        color: #FF4B4B;
    }
    .social-icons i {
        font-size: 24px;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Left Column (Profile) ---
col1, col2 = st.columns([1, 3])

with col1:
    current_image = image_filenames[count]
    image = Image.open(current_image)
    st.image(image, use_container_width=True)

    # Show title for images 1 to 4 only
    if current_image in image_titles:
        st.markdown(
            f"<h4 style='text-align:center; color:gray'>{image_titles[current_image]}</h4>",
            unsafe_allow_html=True,
        )

    # Profile info
    st.markdown("<h1 style='text-align:center;'>Ahmad Anim</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align:center; color:gray'>CEO, Founder | Markelyst</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; color:#666;'>📧 ahmad@markelyst.com</p>",
        unsafe_allow_html=True,
    )
with col2:
    # --- About Me Section ---
    st.markdown("""
    <div class='hover-segment'>
    <h3>About Me</h3>
    <ul>
        <li><strong>Date of Birth:</strong> 28 March 1999</li>
        <li><strong>Height:</strong> 5 feet 7 inches</li>
        <li><strong>Aqida:</strong> Salafi</li>
    </ul>
    <strong>Some of my key qualities:</strong>
    <ul>
        <li><strong>Problem Solver</strong></li>
        <li><strong>Advanced English Speaker</strong></li>
        <li><strong>Public Speaker</strong></li>
    </ul>
    <strong>Hobbies:</strong>
                    <ul>
        <li><strong>Body Building</strong></li>
        <li><strong>Reading Books</strong></li>

    </ul>
                
    </div>
    """, unsafe_allow_html=True)

    # --- Education Section ---
    st.markdown("""
    <div class='hover-segment'>
    <h3>Education</h3>
    <ul>
        <li><strong>BRAC University</strong> – BSc in CSE (2019–2024)</li>
        <li><strong>Notre Dame College</strong></li>
        <li><strong>Ideal School and College, Motijheel</strong></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- Family Section ---
    st.markdown("""
    <div class='hover-segment'>
    <h3>Family</h3>
    <ul>
        <li><strong>Father:</strong> Alauddin Ahmed (Businessman)</li>
        <li><strong>Mother:</strong> Maksuda Begam (Housewife)</li>
       <li><strong>2 brothers, 1 sister</strong> (I'm the youngest)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- What I Do Section ---
    st.markdown("""
    <div class='hover-segment'>
    <h3>What I Do</h3>
    <ul>
        <li><strong>Full-stack Digital Marketing Solutions</strong></li>
        <li><strong>Branding, Identity & Strategic Positioning</strong></li>
        <li><strong>SEO & Content Optimization</strong></li>
        <li><strong>Social Media Automation</strong></li>
        <li><strong>AI-powered Campaigns</strong></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- Whereabouts Section ---
    st.markdown("""
    <div class='hover-segment'>
    <h3>Whereabouts</h3>
    <p><strong>Permanent Address:</strong> Shahi Moholla, Fatullah, Narayanganj(Adjacent to Dhaka North City Corporation)</p>
    </div>
    """, unsafe_allow_html=True)


# --- Social Links (Horizontal, Text Only, Hover Animation) ---
st.markdown("""
    <style>
    .connect-with-me {
        text-align: center;
        margin: 20px 0;
    }
    .connect-with-me a {
        color: #fff;
        text-decoration: none;
        margin: 0 15px;
        font-size: 18px;
        transition: transform 0.3s ease-in-out, color 0.3s ease-in-out;
    }
    .connect-with-me a:hover {
        color: #FF4B4B;
        transform: scale(1.2);  /* Magnification effect */
    }
    .social-icons i {
        font-size: 24px;
        margin-right: 10px;
    }
    .socials-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    </style>
""", unsafe_allow_html=True)


# --- Connect with Me Section ---
st.markdown("<h3 style='text-align:center;'>Connect with Me</h3>",
            unsafe_allow_html=True)
st.markdown("""
<div class="connect-with-me">
    <a href="https://instagram.com/animmetrics" target="_blank">Instagram</a>
    <a href="https://linkedin.com/in/ahmadmarkelyst" target="_blank">LinkedIn</a>
    <a href="https://threads.net/@animmetrics" target="_blank">Threads</a>
    <a href="https://youtube.com/@ahmaadanim" target="_blank">YouTube</a>
    <a href="https://github.com/ahmaad99" target="_blank">GitHub</a>
    <a href="https://twitter.com/ahmaadxhandle" target="_blank">X (Twitter)</a>
    <a href="https://www.facebook.com/ahmad.anim.2024" target="_blank">Facebook</a>
    <a href="https://wa.link/1m9cod" target="_blank">Whatsapp</a>
</div>
""", unsafe_allow_html=True)
# Button for taking the full-page screenshot
