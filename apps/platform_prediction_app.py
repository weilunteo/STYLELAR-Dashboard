import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
from components import common
from datetime import datetime, date, time


def app():
    df = pd.read_csv('data/platform_dataset.csv')

    st.write(df.head())

    platform_prediction = """
    <p style="text-align: justify">A Logistic Regression model is used to predict if there will be 
    a successful transaction based on selected features. This will help sellers determine the ideal time during 
    the day to promote their products, and possibly introduce promotions to boost textile sales.</p>
    </p>
    """

    st.title("Transaction Prediction (For Sellers)")
    st.markdown(platform_prediction, unsafe_allow_html=True)

    st.header("Input Features")

    # ['Date of Purchase', 'Time of Transaction', 'Qty of Purchase', 'Cost of Purchase', 'Rating']

    # date_of_purchase = st.date_input(
    #     label='Date',
    #     value=date(2020,1,1)

    # )

    time_of_transaction = st.time_input(
        label='Time of Transaction',
        value=time(0, 0)
        
    )

    qty_of_purchase = st.slider(
        label='Quantity of Product',
        min_value=int(df['Qty of Purchase'].min()),
        max_value=int(df['Qty of Purchase'].max()),
        value=1,
        step=1
    )

    cost_of_purchase = st.slider(
        label='Cost of Product',
        min_value=int(df['Cost of Purchase'].min()),
        max_value=int(df['Cost of Purchase'].max()),
        value=1,
        step=1
    )

    rating = st.slider(
        label='Rating of Purchase',
        min_value=int(df['Rating'].min()),
        max_value=int(df['Rating'].max()),
        value=1,
        step=1
    )

    
    # date_of_purchase = date_of_purchase.strftime('%Y-%m-%d')
    time_of_transaction = time_of_transaction.strftime('%H:%M')     # format the time as a string without the seconds

    # Extract the hour and minute components from the 'Time of Transaction' column
    # Convert the time of transaction string to hour and minute components
    hour = int(time_of_transaction.split(':')[0])
    minute = int(time_of_transaction.split(':')[1])

    # Convert the hour and minute components to a fraction of the total number of minutes in a day
    time_of_transaction = (hour * 60 + minute) / 1440.0

    # st.write(date_of_purchase, type(date_of_purchase))
    # st.write(time_of_transaction, type(time_of_transaction))


    user_variables = [time_of_transaction, qty_of_purchase, cost_of_purchase, rating]
    variable_names = ["Time of Transaction", "Qty of Purchase", "Cost of Purchase", "Rating"]

    if st.button("Predict"):
        prediction = common.get_prediction(user_variables)[0]
        # st.write(prediction)
        confidence = common.get_prediction(user_variables)[1]
        # percentile_list = common.get_percentile(user_variables, df)

        # st.write("The variables that you have chosen are:")
        
        # for i in range(len(user_variables)):
            # st.write(variable_names[i],": ", user_variables[i], ", ", str(round(percentile_list[i], 2))+" percentile")
            # st.write(variable_names[i],": ", user_variables[i])

        if prediction == 1:
            st.write("Hooray! This is a good time to list or promote your product. ")
        else:
            st.write("Oh no, this is not a good time to list or promote your product. ")

        st.write("Confidence level:", round(confidence, 2))



