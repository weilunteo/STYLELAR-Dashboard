import joblib

def predict(data):
    clf = joblib.load("platform_model_catboost.sav")
    return clf.predict(data)