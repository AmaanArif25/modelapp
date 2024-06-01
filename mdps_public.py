# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: Amaan Arif
"""

import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# loading the saved models
crop_model = pickle.load(open('crop_model.sav', 'rb'))

fertilizer_model = pickle.load(open('fertilizer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('AI in Agriculture',
                          
                          ['Crop Recommendation Prediction',
                           'Fertilizer Recommendation Prediction'],
                          icons=['Agronomy','Agriculture'],
                          default_index=0)
    st.image(
    "https://em-content.zobj.net/source/apple/391/farmer_1f9d1-200d-1f33e.png",
    width=100,
    )


st.image(
    "https://em-content.zobj.net/source/apple/391/sheaf-of-rice_1f33e.png",
    width=100,
)

# Diabetes Prediction Page
if (selected == 'Crop Recommendation Prediction'):
    
    # page title
    st.title('Crop Recommendation System using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        N = st.number_input('Nitrogen (N) value')
    
    with col2:
        P = st.number_input('Phosphorus (P) value')
        
    with col3:
        K = st.number_input('Potassium (K) value')

    with col1:
        temperature = st.number_input('Temperature value')
    
    with col2:
        humidity = st.number_input('Humidity value')

    with col3:
        pH = st.number_input('pH value')

    with col1:
        rainfall = st.number_input('Rainfall value')

    
    
    # code for Prediction
    crop_pred = ''
    
    # creating a button for Prediction
    if st.button('Crop Recommendation Test Result'):
        crop_prediction = crop_model.predict([[N, P, K, temperature, humidity, pH, rainfall]])
        # Assuming `crop_prediction` returns the recommended crop as a string
        st.success(f'The recommended crop is: {crop_prediction[0]}')


# Fertilizer Recommendation Prediction Page
if (selected == 'Fertilizer Recommendation Prediction'):
    
    # Page title
    st.title('Fertilizer Recommendation System using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Nitrogen = st.number_input('Nitrogen (N) value')
        
    with col2:
        Potassium = st.number_input('Potassium (K) value')
        
    with col3:
        Phosphorous = st.number_input('Phosphorous (P) value')
    # Ensure the input values are converted to float
    try:
        nitrogen = float(Nitrogen)
        potassium = float(Potassium)
        phosphorous = float(Phosphorous)
    except ValueError:
        st.error("Please enter valid numeric values for Nitrogen, Potassium, and Phosphorous.")

    # Code for Prediction
    fertilizer_pred = ''
    
    # Creating a button for Prediction
    if st.button('Fertilizer Recommendation Test Result'):
        fertilizer_prediction = fertilizer_model.predict([[Nitrogen, Potassium, Phosphorous]])
        # Assuming `crop_prediction` returns the recommended crop as a string
        st.success(f'The recommended fertilizer is: {fertilizer_prediction[0]}')
        

    
# Define the message
message = "Created by Amaan Arif"

# Display the message in the sidebar
st.sidebar.markdown(message)
