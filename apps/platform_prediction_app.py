import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
from components import common
from datetime import datetime


def app():
    df = pd.read_csv('data/platform_dataset.csv')

    platform_prediction = """
    <h1>Platform Prediction</h1>
    <p style="text-align: justify">This is a proposed CatBoost classification model to predict if there will be 
    a successful transaction based on selected features. This will help sellers determine the ideal time during 
    the day of a month to promote their products, and possibly introduce promotion to boost textile sales.</p>
    </p>
    """

    st.title("Predicting a successful transaction")
    st.markdown(platform_prediction, unsafe_allow_html=True)

    st.header("Input Features")

    # ['Date of Purchase', 'Time of Transaction', 'Qty of Purchase', 'Cost of Purchase', 'Rating']

    date_of_purchase = st.date_input(
        label='Date',
        value=datetime.date.today(),
        min_value=datetime.date(2020, 1, 1)

    )

    time_of_transaction = st.time_input(
        label='Time',
        value=datetime.time(0, 0)
        
    )

    qty_of_purchase = st.slider(
        label='Quantity',
        min_value=int(df['Qty of Purchase'].min()),
        max_value=int(df['Qty of Purchase'].max()),
        value=1,
        step=1
    )

    cost_of_purchase = st.slider(
        label='Cost',
        min_value=int(df['Cost of Purchase'].min()),
        max_value=int(df['Cost of Purchase'].max()),
        value=1,
        step=1
    )

    rating = st.slider(
        label='Rating',
        min_value=int(df['Rating'].min()),
        max_value=int(df['Rating'].max()),
        value=1,
        step=1
    )

    user_variables = [date_of_purchase, time_of_transaction, qty_of_purchase, cost_of_purchase, rating]
    variable_names = ["Date of Purchase", "Time of Transaction", "Qty of Purchase", "Cost of Purchase", "Rating"]

    if st.button("Predict"):
        prediction = common.get_prediction(user_variables)[0]
        confidence = common.get_prediction(user_variables)[1]
        percentile_list = common.get_percentile(user_variables, df)

        st.write("The variables that you have chosen are:")
        
        for i in range(len(user_variables)):
            st.write(variable_names[i],": ", user_variables[i], ", ", str(round(percentile_list[i], 2))+" percentile")

            if prediction == 1:
                st.write("Hooray! This is a good time to list or promote your products!")
            else:
                st.write("Oh no, this is not a good time to list or promote your product.")

        st.write("Confidence level:", round(confidence, 2))


