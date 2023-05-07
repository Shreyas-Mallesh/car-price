"""This module create the home page."""

# Import necessary modules.
import streamlit as st


def app():
    st.title("Car Pridiction App")
    st.image("./car_image.jpg")
    st.text(
        """
        This web app allows a user to predict the prices of a car based on their 
        engine size, horse power, dimensions and the drive wheel type parameters.
        """
    )
