import json
import streamlit as st
import requests
streamlit_options = json.load(open('streamlit_options.json'))
user_options = {}
st.title('Breast Cancer Diagnosis')
for col, range in streamlit_options.items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options[col] = st.sidebar.slider(col, min_val, float(max_val), value=float(current_value))
user_options

if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    response = requests.post('http://127.0.0.1:8000/predict',data=data)
    st.write(response.json())