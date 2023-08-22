import streamlit as st
from streamlit_option_menu import option_menu




st.header('Attendance System using Face Recognition')

with st.spinner("Loading Models and Conneting to Redis db ..."):
    import face_rec
    
st.success('Model loaded sucesfully')
st.success('Redis db sucessfully connected')


    