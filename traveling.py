import streamlit as st
from datetime import time, date

st.title("Form Example")

# Input angka dengan stepper
number = st.number_input("Pick a number", min_value=0, step=1)

# Input email
email = st.text_input("Email address")

# Input tanggal
travel_date = st.date_input("Travelling date", value=date(2022, 6, 17))

# Input waktu
school_time = st.time_input("School time", value=time(8, 0))

# Input teks deskripsi
description = st.text_area("Description")

# Upload foto
uploaded_file = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"], help="Limit 200MB per file")

# Pilih warna favorit
favorite_color = st.color_picker("Choose your favourite color", "#800080")

# Tombol Submit
if st.button("Submit"):
    st.success("Form submitted successfully!")
    st.write("Here is the data you submitted:")
    st.write(f"Number: {number}")
    st.write(f"Email: {email}")
    st.write(f"Travel Date: {travel_date}")
    st.write(f"School Time: {school_time}")
    st.write(f"Description: {description}")
    st.write(f"Favorite Color: {favorite_color}")
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded photo", use_column_width=True)
