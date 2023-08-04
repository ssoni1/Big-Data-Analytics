import pandas as pd
import numpy as np
import streamlit as st
import json
import requests
import pickle
st.set_page_config(page_title='Miami Florida Housing Prediction Prices ')
model = pickle.load(open('model_3.pkl', 'rb'))


def predict_price(Land,Living,Rail_Dist,Cntr_Dist,Sub_Cntr,Hwy_Dist, Age):
    input = np.array([[Land, Living, Rail_Dist, Cntr_Dist, Sub_Cntr, Hwy_Dist, Age]]).astype(np.float64)
    prediction = model.predict(input)
    return int(prediction)


def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Miami Housing Price Prediction </h2>
    </div>
    """
    options = st.selectbox('Options', ('home','Dataset Overview','Prediction form','New Inserted Values'))

    if options == "home":
        st.title('Home')
        st.write('This is a home page.')

    elif options == "Dataset Overview":
        st.title('Dataset')

    elif options == "Prediction form":
        st.title('Miami Florida Housing Prediction Prices')
        Land = st.number_input("Land Area in square Feet")
        Living = st.number_input("Floor Area in Square Feet")
        Rail_Dist = st.number_input("Distance to the Rail Line")
        Cntr_Dist = st.number_input("Distance to the Miami Central Business Dist.")
        Sub_Cntr = st.number_input("Distance to the nearest sub center")
        Hwy_Dist = st.number_input("Distance to the nearest highway")
        Age = st.number_input("Age of the Structure")
        safe_html = """  
                <div style="background-color:#80ff80; padding:10px >
                <h2 style="color:white;text-align:center;">Prediction is accurate</h2>
                </div>
                """
        if st.button("Predict the price"):
            # output = model.predict([[float(Land), float(Living), float(Rail_Dist),
            #                                                     float(Cntr_Dist),
            #                                                     float(Sub_Cntr),
            #                                                     float(Hwy_Dist), float(Age)]])

            output = predict_price(Land, Living, Rail_Dist, Cntr_Dist, Sub_Cntr, Hwy_Dist, Age)
            st.success('The prediction price is {}'.format(output))

    elif options == "New Inserted Values":
        st.title('New Values')


main()







