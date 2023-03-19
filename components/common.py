import math
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import streamlit as st
from scipy.stats import percentileofscore
from datetime import datetime


# def get_prediction(variables):
#     HERE = Path(__file__).parent
    
#     pickle_in = open(HERE / 'platform_model_catboost.sav', 'rb')
#     model = pickle.load(pickle_in)

#     x_test = pd.DataFrame(np.array([variables]))
#     st.write()
#     prediction = model.predict(x_test)
#     confidence = model.predict_proba(x_test)

#     return int(prediction[0]), list(confidence[0])[int(prediction[0])]


def get_prediction(user_variables):
    # Load the model
    HERE = Path(__file__).parent
    pickle_in = open(HERE / 'platform_model_catboost.sav', 'rb')
    model = pickle.load(pickle_in)

    
    # Convert date and time strings to datetime objects
    date_of_purchase = datetime.strptime(user_variables[0], '%Y-%m-%d')
    time_of_transaction = datetime.strptime(user_variables[1], '%H:%M')
    
    # Extract features from datetime objects
    day_of_week = date_of_purchase.weekday()
    hour_of_day = time_of_transaction.hour
    
    # Create a new input array with the extracted features
    x_test= [day_of_week, hour_of_day, user_variables[2], user_variables[3], user_variables[4]]
    
    # Make a prediction and return the result
    prediction = model.predict([x_test])[0]
    confidence = model.predict_proba([x_test])[0][prediction]
    
    return prediction, confidence

# def get_percentile(variables, df):
#     variable_names = ["Date of Purchase", "Time of Transaction", "Qty of Purchase", "Cost of Purchase", "Rating"]
#     percentile_list = []

#     for i in range(len(variable_names)):
#         str.write(variable_names[i])
#         if variable_names[i] == "Date of Purchase":
#             timestamp = variables[i].timestamp()
#             dataset = df[variable_names[i]].apply(lambda x: x.timestamp())
#             percentile = percentileofscore(dataset, timestamp)
#         else:
#             dataset = df[variable_names[i]]
#             percentile = percentileofscore(dataset, variables[i])

#         percentile_list.append(percentile)

#     return percentile_list