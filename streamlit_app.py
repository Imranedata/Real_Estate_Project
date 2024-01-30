#!/usr/bin/env python
# coding: utf-8

# In[9]:


import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names, but RandomForestRegressor was fitted with feature names")


# In[8]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import ipywidgets as widgets
from IPython.display import display

# Load the dataset
df = pd.read_csv('cleaned_data.csv')

# Select features and target variable
X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'yr_built', 'yr_renovated', 'zipcode']]
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Function to predict house price based on features
def predict_price(bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                  waterfront, view, condition, grade, yr_built, yr_renovated, zipcode):
    features = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                 waterfront, view, condition, grade, yr_built, yr_renovated, zipcode]]
    predicted_price = model.predict(features)[0]
    return f'Predicted Price: ${predicted_price:,.0f}'

# Create widgets for each feature
bedrooms_widget = widgets.IntSlider(min=1, max=10, step=1, description='Bedrooms:', value=3)
bathrooms_widget = widgets.IntSlider(min=0.5, max=8, step=0.5, description='Bathrooms:', value=2.5)
sqft_living_widget = widgets.IntSlider(min=500, max=10000, step=100, description='Sqft Living:', value=1500)
sqft_lot_widget = widgets.IntSlider(min=1000, max=50000, step=1000, description='Sqft Lot:', value=5000)
floors_widget = widgets.IntSlider(min=1, max=3, step=0.5, description='Floors:', value=1)
waterfront_widget = widgets.Checkbox(value=False, description='Waterfront')
view_widget = widgets.IntSlider(min=0, max=4, step=1, description='View:', value=0)
condition_widget = widgets.IntSlider(min=1, max=5, step=1, description='Condition:', value=3)
grade_widget = widgets.IntSlider(min=1, max=13, step=1, description='Grade:', value=7)
yr_built_widget = widgets.IntSlider(min=1900, max=2022, step=1, description='Year Built:', value=2000)
yr_renovated_widget = widgets.IntSlider(min=1900, max=2022, step=1, description='Year Renovated:', value=2000)
zipcode_widget = widgets.IntSlider(min=98000, max=98200, step=1, description='Zipcode:', value=98000)

# Create button widget
button = widgets.Button(description='Predict Price')

# Function to handle button click event
def on_button_click(event):
    predicted_price.value = predict_price(bedrooms_widget.value, bathrooms_widget.value,
                                          sqft_living_widget.value, sqft_lot_widget.value,
                                          floors_widget.value, waterfront_widget.value,
                                          view_widget.value, condition_widget.value,
                                          grade_widget.value, yr_built_widget.value,
                                          yr_renovated_widget.value, zipcode_widget.value)

# Attach button click event to function
button.on_click(on_button_click)

# Create output widget to display predicted price
predicted_price = widgets.Label(value='')

# Display widgets
widgets.VBox([bedrooms_widget, bathrooms_widget, sqft_living_widget, sqft_lot_widget,
              floors_widget, waterfront_widget, view_widget, condition_widget,
              grade_widget, yr_built_widget, yr_renovated_widget, zipcode_widget,
              button, predicted_price])


# In[ ]:




