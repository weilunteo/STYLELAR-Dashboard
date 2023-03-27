import streamlit as st
import math
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
# from scipy.stats import percentileofscore
from sklearn.preprocessing import MinMaxScaler


def get_prediction(variables):
    HERE = Path(__file__).parent
    
    pickle_in = open(HERE / 'platform_model_logreg.sav', 'rb')
    model = pickle.load(pickle_in)
    # st.write(variables)
    x_test = pd.DataFrame(np.array([variables]))
    # st.write(x_test)
    
    prediction = model.predict(x_test)
    confidence = model.predict_proba(x_test)

    return int(prediction[0]), list(confidence[0])[int(prediction[0])]