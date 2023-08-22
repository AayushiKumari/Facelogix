import streamlit as st
from streamlit_option_menu import option_menu
import os 
st.set_page_config(page_title='Welcome to FaceIdTracker',layout='wide')

with st.sidebar:
    selected = option_menu(
        menu_title= "Menu",
        options = ["Home","Attendance","Registraion","Report"],
        menu_icon = "cast",
        default_index=0,
        orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": "light green"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
        }
    )

if selected == "Home":
    file_path = "module/Home.py"
    if os.path.exists(file_path):
        exec(open(file_path).read())
    else:
        st.error("File does not exist!")

if selected == "Attendance":
    file_path = "module/1_Real_Time_Prediction.py"
    if os.path.exists(file_path):
        exec(open(file_path).read())
    else:
        st.error("File does not exist!")

if selected == "Registraion":
    file_path = "module/2_Registration_form.py"
    if os.path.exists(file_path):
        exec(open(file_path).read())
    else:
        st.error("File does not exist!")

if selected == "Report":
    file_path = "module/3_Report.py"
    if os.path.exists(file_path):
        exec(open(file_path).read())
    else:
        st.error("File does not exist!")
