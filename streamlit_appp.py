#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Custom hash function for load_data function
def hash_load_data(func):
    return None

def load_data():
    return pd.read_csv('cleaned_data.csv')
# Load the dataset
@st.cache(hash_funcs={type(load_data): hash_load_data})
def load_data():
    return pd.read_csv('cleaned_data.csv')

# Selecting features
selected_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                     'waterfront', 'view', 'condition', 'grade', 'yr_built', 'yr_renovated', 'zipcode']

# Train the model
@st.cache
def train_model():
    data = load_data()
    X = data[selected_features]
    y = data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

# Predict function
def predict_price(features, model):
    return model.predict([features])[0]

# Streamlit app
st.title('House Price Prediction App')

# Add widgets
bedrooms = st.sidebar.slider('Bedrooms', min_value=1, max_value=10, value=3)
bathrooms = st.sidebar.slider('Bathrooms', min_value=1, max_value=8, value=2)
sqft_living = st.sidebar.slider('Sqft Living', min_value=100, max_value=10000, value=1500)
sqft_lot = st.sidebar.slider('Sqft Lot', min_value=100, max_value=10000, value=5000)
floors = st.sidebar.slider('Floors', min_value=1, max_value=3, value=1)
waterfront = st.sidebar.selectbox('Waterfront', [0, 1], index=0)
view = st.sidebar.slider('View', min_value=0, max_value=4, value=0)
condition = st.sidebar.slider('Condition', min_value=1, max_value=5, value=3)
grade = st.sidebar.slider('Grade', min_value=1, max_value=13, value=7)
yr_built = st.sidebar.slider('Year Built', min_value=1900, max_value=2022, value=2000)
yr_renovated = st.sidebar.slider('Year Renovated', min_value=1900, max_value=2022, value=2000)
zipcode = st.sidebar.text_input('Zipcode', value='98000')

# Create a button to predict the price
if st.sidebar.button('Predict Price'):
    model = train_model()
    features = [bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                waterfront, view, condition, grade, yr_built, yr_renovated, zipcode]
    prediction = predict_price(features, model)
    st.sidebar.success(f'Predicted Price: ${prediction:,.2f}')


# In[ ]:




