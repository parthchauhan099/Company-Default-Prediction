import streamlit as st
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

with open('company_default.pkl','rb') as file:
    model = pickle.load(file)
    
st.title('Company Default Prediction')
st.text('Aim is to forecast potential company defaults using Random Forest Model')
st.subheader('Enter Company Information')

col1, col2, col3 = st.columns(3)
with col1:
    pbdita = st.number_input('PBDITA as % of Total Income')
with col2:
    pbt = st.number_input('PBT as % of Total Income')
with col3:
    pat = st.number_input('PAT as % of Total Income')
    
col4, col5, col6 = st.columns(3)
with col4:
    cash_profit = st.number_input('Cash Profit % of Total Income')
with col5:
    pat_net = st.number_input('PAT as % of Net Worth')
with col6:
    tol_tnw = st.number_input('TOL_to_TNW')

col7, col8, col9 = st.columns(3)
with col7:
    ttl_tnw = st.number_input('TTL_to_TNW')
with col8:
    conti_lia = st.number_input('Contigent Liablity to Net Worth %')
with col9:
    debt_equ = st.number_input('Debt to Equity Ratio Times')
    
col10, col11, col12 = st.columns(3)
with col10:
    cash_sales = st.number_input('Cash to Avg Cost of Sales per Day')
with col11:
    share_out = st.number_input('Shares Outstanding')
with col12:
    facevalue = st.number_input('Equity FaceValue')
    
col13, col14 = st.columns(2)
with col13:
    eps = st.number_input('EPS')
with col14:
    adj_eps = st.number_input('Adjusted EPS')

input_data = pd.DataFrame({
    'PBDITA_as_perc_of_total_income':[pbdita],
    'PBT_as_perc_of_total_income':[pbt],
    'PAT_as_perc_of_total_income':[pat], 
    'Cash_profit_as_perc_of_total_income':[cash_profit],
    'PAT_as_perc_of_net_worth':[pat_net],
    'TOL_to_TNW':[tol_tnw],
    'Total_term_liabilities_to_tangible_net_worth':[ttl_tnw],
    'Contingent_liabilities_to_Net_worth_perc':[conti_lia],
    'Debt_to_equity_ratio_times':[debt_equ],
    'Cash_to_average_cost_of_sales_per_day':[cash_sales],
    'Shares_outstanding':[share_out], 
    'Equity_face_value':[facevalue],
    'EPS':[eps], 
    'Adjusted_EPS':[adj_eps]
    })

if st.button('Predict'):
    prediction = model.predict(input_data)
    result_map = {0:'Not Default', 1:'Default'}
    result = result_map[prediction[0]]
    st.write(f'The Prediction of the Company is: **{result}**')
