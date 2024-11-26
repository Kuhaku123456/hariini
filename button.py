import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('WHY hello there')
else:
    st.write('good bye')