# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:01:38 2021

@author: PRANAV
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

df1 = pd.read_excel(r"C:\Users\PRANAV\Desktop\Project\no of customer per month.xlsx")
salepermonth = pd.read_csv(r"C:\Users\PRANAV\Desktop\Project\salepermonth.csv")
df = pd.read_csv(r"C:\Users\PRANAV\Desktop\Project\df_rfm.csv")
retail = pd.read_excel(r"C:\Users\PRANAV\Desktop\Project\sample_data.xlsx")

st.title('Retail Sector domain Analysis')
st.write('@Pranav')
nav = st.sidebar.radio('options',['Home','Prediction'])
if nav == 'Home':
    st.header("Business Objective:")
    st.markdown(''' ##### Predict who is likely to shop next month. Highlight factors that impact likelihood of customer shopping next month. For each customer shopped during 12/1/2009 till 11/9/2011, you must predict the likelihood of customer shopping next month.''')
    st.header("Data Set Details:")
    st.markdown(''' ##### The dataset contains ~2 years of transaction data for e-commerce retailer to be used for building a model. -Data set details sent in excel file. Your task is to predict for all customers who shopped at-least once during 12/1/2009 till 11/9/2011, who will come back to buy any product next month (11/9/2011 – 12/9/2011).''')
    st.subheader('Dataset')
    st.markdown(''' ##### sample dataset''')
    st.dataframe(retail)
    st.markdown(''' ### Number of customer per month ''')
    st.bar_chart(df1)
    st.write("Thank You")

if nav == 'Prediction':
    st.header('Prediction')
    
    x = st.number_input("CustomerID: ",min_value=salepermonth['CustomerID'].min(),max_value=salepermonth['CustomerID'].max())
    z = pd.DataFrame(df.loc[df['CustomerID'] == x])
    
    if st.button("Predict"):
        if z.iloc[0,11] == 2:
            st.success('yes')
        else:
            st.info('NO')
    st.subheader("RFM Score")
    y = salepermonth.loc[salepermonth['CustomerID'] == x]
    y = y.drop(y.iloc[:,0:1],axis = 1)
   
    st.dataframe(z)
    
    # Plotting Graph
    st.markdown("Number of month per customer")
    fig = plt.figure(figsize = (20, 12))
    month = ['Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011',
         'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011']
    # creating the bar plot
    plt.bar(month,y.iloc[0] ,color ='orange',width = 0.5)
    plt.xlabel("CustomerID: {}".format(x))
    plt.ylabel("Money Spent")
    st.pyplot()
    st.write("Thank You")