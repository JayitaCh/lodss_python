import streamlit as st
import streamlit.components.v1 as components
import io
import contextlib

# Setting the layout
st.set_page_config(layout="wide")

# Inserting custom image in the sidebar to enhance the visual appearance
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

# Applying it to the sidebar
st.sidebar.write("")

# Intro - title and video embedding
st.title("✨ Welcome to the LODSS!")
st.text("Add some text")
st.video("https://www.youtube.com/watch?v=sD1-rS_TM2o")

##### Playing around with the solar system 

# Planet options (same as in CSV)
planet_names = ["Mercury","Venus","Earth", "Mars","Jupiter","Saturn","Uranus","Neptune" ]

st.title("🪐 Choose a Planet")
selected_planet = st.selectbox("Select a planet to render:", ["None"] + planet_names)

if selected_planet:
    selected_index = planet_names.index(selected_planet)
    selected_planets = planet_names[:selected_index + 1]

    with open("sketch.html", "r") as f:
        html_code = f.read()
    
    html_code = html_code.replace("{{PLANET_NAME}}", ",".join(selected_planets))

    components.html(html_code, height=670, scrolling=True)

##### Running code
st.markdown("""
```python
print("Your Name")            
""")

st.markdown("""### Enter Python code here:""")
code = st.text_area("Type whatever you see in the box above",height=70)

if st.button("Run Code"):
    f = io.StringIO()
    try:
        with contextlib.redirect_stdout(f):
            exec(code, globals())  # Run user code safely in global context
    except Exception as e:
        st.error(f"Error: {e}")
    output = f.getvalue()
    if output:
        st.text_area("Output", value=output, height=68)
    else:
        st.write("No output")