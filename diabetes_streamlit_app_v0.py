#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st
import pandas as pd
#from PIL import image


# df = pd.read_csv('diabetes_data_upload.csv')

# df.head()

# df.replace({'Yes': 1, 'No': 0, 'Male': 0, 'Female': 1, 'Positive': 1, 'Negative': 0}, inplace=True)
# df.head()

# # Get unique values for each column
# unique_values = {}
# for column in df.columns:
#     unique_values[column] = df[column].unique()
# 
# # Display unique values for each column
# for column, values in unique_values.items():
#     print(f'Unique values in {column}: {values}')
# 

# df.info()

# In[23]:


st.title('Dummy Diabetes Streamit')
st.subheader('O seu resultado')

st.sidebar.title("Os seus dados")

# Create input boxes for each feature
age = st.sidebar.slider("Idade", min_value=0, max_value=120, value=30)
gender = st.sidebar.radio("Gênero de nascença", ('Masculino', 'Feminino'))
polyuria = st.sidebar.checkbox("Poliúria")
polydipsia = st.sidebar.checkbox("Polidipsia")
# Add input boxes for other features here...

# Create a button to trigger prediction
if st.sidebar.button("Predição"):
    # Now you can use the user inputs (age, gender, etc.) in your ML model
    # For example, you can create a new DataFrame with these inputs and use your model for prediction
    
    
#     user_inputs = pd.DataFrame({
#         'Age': [age],
#         'Gender': [0 if gender == 'Male' else 1],
#         'Polyuria': [1 if polyuria else 0],
#         'Polydipsia': [1 if polydipsia else 0],
#         # Add other features here...
#     })

   
    
    # Display the prediction to the user

    st.write("Um Dia teremos aqui a predição")

