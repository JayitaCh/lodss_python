import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        background-image: url("https://img.freepik.com/premium-photo/cosmic-theme-3d-render-with-glowing-stars-planet_599037-248.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100%;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.write("")

st.title("✨ Welcome to the LODSS!")
st.text("Add some text")
st.video("https://www.youtube.com/watch?v=sD1-rS_TM2o")

with open("sketch.html", "r") as f:
    html_code = f.read()

# Planet options (same as in CSV)
planet_names = ["Mercury","Venus","Earth", "Mars","Jupiter","Saturn","Uranus","Neptune" ]

st.title("🪐 Choose a Planet")
selected_planet = st.selectbox("Select a planet to render:", [""] + planet_names)

if selected_planet:
    with open("sketch.html", "r") as f:
        html_code = f.read()
    
    html_code = html_code.replace("{{PLANET_NAME}}", selected_planet)

    st.components.v1.html(html_code, height=670, scrolling=True)