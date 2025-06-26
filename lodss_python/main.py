import streamlit as st
import streamlit.components.v1 as components
import io
import contextlib
import random

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
selected_planet = st.selectbox("Select a planet to render:", [""] + planet_names)

if selected_planet:
    selected_index = planet_names.index(selected_planet)
    selected_planets = planet_names[:selected_index + 1]

    with open("sketch.html", "r") as f:
        html_code = f.read()
    
    html_code = html_code.replace("{{PLANET_NAME}}", ",".join(selected_planets))

    components.html(html_code, height=670, scrolling=True)

##### ENHANCED INTERACTIVE SECTION

# Planet data for enhanced features
planets_data = {
    "Mercury": {
        "emoji": "☿️",
        "color": "#8C7853",
        "fact": "A year on Mercury is only 88 Earth days - you'd have your birthday every 3 months!",
        "age_factor": 0.24,
        "weight_factor": 0.38,
        "fun_fact": "It's hot enough to melt lead during the day!"
    },
    "Venus": {
        "emoji": "♀️", 
        "color": "#FFC649",
        "fact": "Venus spins backwards! The sun would rise in the west!",
        "age_factor": 0.62,
        "weight_factor": 0.91,
        "fun_fact": "It rains acid and has clouds made of sulfur!"
    },
    "Earth": {
        "emoji": "🌍",
        "color": "#6B93D6",
        "fact": "Earth is the only planet with pizza! 🍕",
        "age_factor": 1.0,
        "weight_factor": 1.0,
        "fun_fact": "You're already living on the best planet!"
    },
    "Mars": {
        "emoji": "♂️",
        "color": "#CD5C5C", 
        "fact": "Mars has the biggest volcano in the solar system - 3 times taller than Mount Everest!",
        "age_factor": 1.88,
        "weight_factor": 0.38,
        "fun_fact": "A day on Mars is almost the same as Earth - 24 hours 37 minutes!"
    },
    "Jupiter": {
        "emoji": "♃",
        "color": "#D8CA9D",
        "fact": "Jupiter is so big that all other planets could fit inside it!",
        "age_factor": 11.86,
        "weight_factor": 2.36,
        "fun_fact": "Jupiter's Great Red Spot is a storm bigger than Earth that's been raging for 400 years!"
    },
    "Saturn": {
        "emoji": "♄",
        "color": "#FAD5A5",
        "fact": "Saturn would float in water because it's less dense than H2O!",
        "age_factor": 29.46,
        "weight_factor": 0.91,
        "fun_fact": "Saturn's rings are made of billions of ice chunks!"
    },
    "Uranus": {
        "emoji": "♅",
        "color": "#4FD0E7",
        "fact": "Uranus rolls on its side like a ball instead of spinning like a top!",
        "age_factor": 84.01,
        "weight_factor": 0.89,
        "fun_fact": "Uranus is the coldest planet even though it's not the farthest from the sun!"
    },
    "Neptune": {
        "emoji": "♆",
        "color": "#4B70DD",
        "fact": "Neptune has winds faster than the speed of sound!",
        "age_factor": 164.79,
        "weight_factor": 1.13,
        "fun_fact": "It rains diamonds on Neptune!"
    }
}

st.markdown('## 🚀  Astronaut Registration & Mission Control', unsafe_allow_html=True)

# Interactive Form Section
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👨‍🚀 What's your astronaut name?", placeholder="Captain Space Explorer")
    age = st.number_input("🎂 How old are you?", min_value=5, max_value=75, value=10)

with col2:
    favourite_planet = st.selectbox(
        "🪐 Pick your favorite planet to explore:", 
        ["Choose your destination..."] + planet_names
    )

# Enhanced display when all fields are filled
if name and age and favourite_planet != "Choose your destination...":
    
    # Welcome message
    planet_emoji = planets_data[favourite_planet]["emoji"]
    st.markdown(f"### 🎉 Welcome aboard, {name}! {planet_emoji}")
    
    # Planet-specific info
    planet_info = planets_data[favourite_planet]
    
    # Age and weight calculations
    planet_age = int(round(age / planet_info["age_factor"], 0))
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="space-fact">
            <h4>{planet_emoji} Age on {favourite_planet}</h4>
            <h2>{planet_age} years old!</h2>
            <p>That's because {favourite_planet} takes {planet_info['age_factor']} Earth years to orbit the sun!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="space-fact">
            <h4>⚖️ Your Weight</h4>
            <h2>{int(age * planet_info['weight_factor'] * 3)} kg</h2>
            <p>On {favourite_planet} you'd weigh {planet_info['weight_factor']}x your Earth weight!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="space-fact">
            <h4>🔍 Cool Fact</h4>
            <p style="font-size: 16px;">{planet_info['fact']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Fun interactive buttons
    st.markdown("### 🎮 Mission Control:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎲 Random Space Mission!"):
            missions = [
                f"Build a secret base on {favourite_planet}!",
                f"Search for alien life forms on {favourite_planet}!",
                f"Collect space rocks from {favourite_planet}'s surface!",
                f"Race a rover around {favourite_planet}!",
                f"Plant a flag on the highest mountain of {favourite_planet}!",
                f"Send a message to aliens living on {favourite_planet}!"
            ]
            mission = random.choice(missions)
            st.balloons()
            st.markdown(f"""
            <div class="mission-box">
                🚀 MISSION ASSIGNED: {mission}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if st.button("🔮 Space Fortune"):
            fortunes = [
                "You will discover a new moon!",
                "An alien will ask for your autograph!",
                "You'll find the best space pizza in the galaxy!",
                "A comet will be named after you!",
                "You'll become friends with a robot!",
                "You'll surf on Saturn's rings!"
            ]
            fortune = random.choice(fortunes)
            st.snow()
            st.success(f"🔮 Your space fortune: {fortune}")
    
    with col3:
        if st.button("💫 Amazing Space Fact"):
            extra_facts = [
                "A spoonful of neutron star would weigh 6 billion tons!",
                "There are more trees on Earth than stars in our galaxy!",
                "One day on Venus equals 243 Earth days!",
                "Jupiter's moon Europa might have twice as much water as Earth!",
                "Sound cannot travel through space because there's no air!",
                "The sun is 400 times larger than the moon but also 400 times farther away!"
            ]
            fact = random.choice(extra_facts)
            st.info(f"🤯 Mind-blown fact: {fact}")
    
    # Planet comparison game
    st.markdown("### 🏆 Planet Comparison Challenge:")
    
    if st.button("🆚 Compare Two Planets!"):
        planet1, planet2 = random.sample(planet_names, 2)
        p1_data = planets_data[planet1]
        p2_data = planets_data[planet2]
        
        st.markdown(f"### {p1_data['emoji']} {planet1} VS {p2_data['emoji']} {planet2}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **{planet1}** {p1_data['emoji']}
            - Your age: {round(age / p1_data['age_factor'], 1)} years
            - Your weight: {int(age * p1_data['weight_factor'] * 3)} kg
            - Fun fact: {p1_data['fun_fact']}
            """)
        
        with col2:
            st.markdown(f"""
            **{planet2}** {p2_data['emoji']}
            - Your age: {round(age / p2_data['age_factor'], 1)} years  
            - Your weight: {int(age * p2_data['weight_factor'] * 3)} kg
            - Fun fact: {p2_data['fun_fact']}
            """)
    
    # Achievement system
    st.markdown("### 🏅 Your Space Achievements:")
    
    achievements = []
    if age >= 10:
        achievements.append("🎂 Double Digit Explorer!")
    if favourite_planet in ["Mars", "Jupiter"]:
        achievements.append("🔴 Red Planet Expert!" if favourite_planet == "Mars" else "🌪️ Gas Giant Fan!")
    if len(name) > 10:
        achievements.append("📝 Creative Name Captain!")
    
    achievements.append("🚀 First Mission Complete!")
    achievements.append("🌟 Solar System Explorer!")
    
    for achievement in achievements:
        st.success(achievement)

else:
    # Basic fallback (original behavior)
    st.markdown(f"Hello {name}, you are {age} years old and your favourite planet is {favourite_planet}!")
    if not name or not age or favourite_planet == "Choose your destination...":
        st.markdown("### 👆 Complete your astronaut registration above to unlock mission control!")
        st.markdown("🌌 Discover amazing facts about planets, get special missions, and become a space explorer!")

# Footer with rotating space facts
st.markdown("---")
st.markdown("### 🌟 Did you know?")
space_facts = [
    "🌌 There are more stars in the universe than grains of sand on all Earth's beaches!",
    "🚀 It would take 9 years to walk to the moon!",
    "☀️ The sun is so big that 1.3 million Earths could fit inside it!",
    "🌙 The moon is moving away from Earth by 4cm each year!",
    "⭐ Stars twinkle because we see them through Earth's moving atmosphere!"
]
random_fact = random.choice(space_facts)
st.info(random_fact)

# Preserved commented code section
# code = st.text_area("Type whatever you see in the box above",height=70)

# if st.button("Run Code"):
#     f = io.StringIO()
#     try:
#         with contextlib.redirect_stdout(f):
#             exec(code, globals())  # Run user code safely in global context
#     except Exception as e:
#         st.error(f"Error: {e}")
#     output = f.getvalue()
#     if output:
#         st.text_area("Output", value=output, height=68)
#     else:
#         st.write("No output")

# code = st.text_area("Type whatever you see in the box above",height=70)

# if st.button("Run Code"):
#     f = io.StringIO()
#     try:
#         with contextlib.redirect_stdout(f):
#             exec(code, globals())  # Run user code safely in global context
#     except Exception as e:
#         st.error(f"Error: {e}")
#     output = f.getvalue()
#     if output:
#         st.text_area("Output", value=output, height=68)
#     else:
#         st.write("No output")