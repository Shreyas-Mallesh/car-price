"""This module creates the web page"""

# Import necessary modules.
import streamlit as st

# Import pages.
import home
import data
import plots
import predict

# Import other necessary things.
from prepro import load_data

# Configure the web page.
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

# Create a dict for pages.
pages_dict = {
                "Home": home,
                "View Data": data, 
                "Visualise Data": plots, 
                "Predict": predict,
            }

# Load the dataset.
df = load_data()

# Create navbar in sidebar.
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to', ("Home", "View Data", "Visualise Data", "Predict"))

car_make = st.sidebar.selectbox("Car Make",
                    ("alfa-romero", "audi", "bmw", "chevrolet", "dodge", "honda", "isuzu", "jaguar",
                     "mazda", "mercedes-benz", "mercury", "mitsubishi", "nissan", "peugot", "plymouth",
                     "porsche", "renault", "saab", "subaru", "toyota", "volkswagen", "volvo"))

# Open the page selected by the user.
if (user_choice == "Home" or user_choice == "About me"):
    selected_page = pages_dict[user_choice]
    selected_page.app()
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(df, car_make)
