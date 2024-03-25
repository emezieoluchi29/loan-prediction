import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import joblib

data = pd.read_csv('loan_approval_dataset.csv')
model = joblib.load('loan_predictor_models.pkl')

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-family: helvetica'>HORIZON LOAN STATUS  PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By Emezie Oluchi</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com (2).png', width= 500)

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Project Overview</h4>", unsafe_allow_html = True)

st.write("The goal of this project is to develop a self-help predictive model that assesses different phone features and group the prices based on these features. By leveraging machine learning techniques, we aim to provide insights into the factors influencing price range based on features, empowering stakeholders to make informed decisions")

st.markdown("<br>", unsafe_allow_html= True)
st.dataframe(data, use_container_width= True)

st.sidebar.image('pngwing.com (3).png', caption = 'Welcome Dear User')

loan_amount = st.sidebar.number_input(' loan_amount')
income_annum = st.sidebar.number_input(' income_annum',)
cibil_score = st.sidebar.number_input(' cibil_score')
residential_assets_value = st.sidebar.number_input(' residential_assets_value')
commercial_assets_value = st.sidebar.number_input(' commercial_assets_value')
luxury_assets_value = st.sidebar.number_input(' luxury_assets_value')
no_of_dependents = st.sidebar.number_input(' no_of_dependents')

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Input Variable</h4>", unsafe_allow_html = True)

inputs = pd.DataFrame()
#inputs[' loan_amount'] = [loan_amount]
#inputs[' income_annum'] = [income_annum]
#inputs[' cibil_score'] = [cibil_score]
#inputs[' residential_assets_value'] = [residential_assets_value]
#inputs[' commercial_assets_value'] = [commercial_assets_value]
#inputs[' luxury_assets_value'] = [luxury_assets_value]
#inputs[' no_of_dependents'] = [no_of_dependents]

#st.dataframe(inputs, use_container_width= True)

prediction_button = st.button('Predict loan status')
if prediction_button:
    predicted = model.predict(inputs)

    if predicted[0]==0:
        st.success(f'Your loan request is Approved')
    elif predicted[0]==1:
        st.success(f'Your loan request is Denied')