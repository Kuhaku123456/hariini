import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame dengan data acak
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

# Judul aplikasi
st.title("Visualisasi Data dengan Streamlit")

# Menampilkan Line Chart
st.subheader("Line Chart")
st.line_chart(df)

# Menampilkan Bar Chart
st.subheader("Bar Chart")
st.bar_chart(df)

# Menampilkan Area Chart
st.subheader("Area Chart")
st.area_chart(df)
