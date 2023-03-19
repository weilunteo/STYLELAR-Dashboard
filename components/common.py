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

# def get_percentile(variables, df):
#     variable_names = ["Time of Transaction", "Qty of Purchase", "Cost of Purchase", "Rating"]
#     percentile_list = []

#     for i in range(len(variable_names)):
#         st.write(variable_names[i])
#         if variable_names[i] == "Time of Transaction":
#             timestamp = variables[i].timestamp()
#             dataset = df[variable_names[i]].apply(lambda x: x.timestamp())
#             percentile = percentileofscore(dataset, timestamp)
#         else:
#             dataset = df[variable_names[i]]
#             percentile = percentileofscore(dataset, variables[i])

#         percentile_list.append(percentile)

#     return percentile_list



# def preprocess_data(X):
#     # for numerical columns
#     # ---------------------
#     # we normalize using MinMaxScaler to constrain values between 0 and 1

#     scaler = MinMaxScaler(feature_range = (0,1))
#     df_numeric = X.select_dtypes(include=[np.number])
#     numeric_cols = df_numeric.columns.values

#     for col in numeric_cols:
#         # fit_transform() of scaler can be applied to each column individually
#         X[col] = scaler.fit_transform(X[[col]])
        
#     print("---Successfully processed numeric column(s)")
#     st.write(X.head(5))
    
#     # for categorical columns
#     # -----------------------
#     # we convert the column into one-hot encoding
#     df_categorical = X.select_dtypes(exclude=[np.number])
#     categorical_cols = df_categorical.columns.values
    
#     # the function get_dummies() (from pandas) creates one-hot encoding
#     X = pd.get_dummies(X,columns=categorical_cols)
           
#     print("---Successfully processed categorical column(s)")
#     st.write(X.head(5))
        
#     return X