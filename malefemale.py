import streamlit as st

# Checkbox
yes = st.checkbox("yes")

# Button
if st.button("Click"):
    st.write("Button clicked!")

# Radio buttons for gender selection
gender_radio = st.radio("Pick your gender", ["Male", "Female"])

# Dropdown for gender
gender_select = st.selectbox("Pick your gender", ["Male", "Female"])

# Dropdown for planets
planet = st.selectbox("Choose a planet", ["Choose an option", "Earth", "Mars", "Jupiter", "Saturn"])

# Slider for marks
mark = st.slider("Pick a mark", 0, 100, 50, step=10, format="%d")
st.write("Bad", "Good", "Excellent")

# Slider for number
number = st.slider("Pick a number", 0, 50, 9)