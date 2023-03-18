import math
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import streamlit as st
from scipy.stats import percentileofscore


def get_prediction(variables):
    HERE = Path(__file__).parent
    
    pickle_in = open(HERE / 'platform_model_catboost.sav', 'rb')
    model = pickle.load(pickle_in)

    x_test = pd.DataFrame(np.array([variables]))
    prediction = model.predict(x_test)
    confidence = model.predict_proba(x_test)

    return int(prediction[0]), list(confidence[0])[int(prediction[0])]

def get_percentile(variables, df):
    variable_names = ["Date of Purchase", "Time of Transaction", "Qty of Purchase", "Cost of Purchase", "Rating"]
    percentile_list = []

    for i in range(len(variable_names)):
        if variable_names[i] == "Date of Purchase":
            timestamp = variables[i].timestamp()
            dataset = df[variable_names[i]].apply(lambda x: x.timestamp())
            percentile = percentileofscore(dataset, timestamp)
        else:
            dataset = df[variable_names[i]]
            percentile = percentileofscore(dataset, variables[i])

        percentile_list.append(percentile)

    return percentile_list