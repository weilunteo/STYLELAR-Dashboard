
### Textile Dashboard 

This is a proof of concept for our 'IS215: Digital Business Transformation and Technologies' project. This interactive dashboard allows both textile suppliers and textile sellers to tap on data to drive their business decisions. It consists of a visualisation charts for suppliers and a prediction model for sellers.

Access the deployed dasboard here: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://weilunteo-textile-dashboard-app-e4tbrh.streamlit.app/)

Alternatively, to run the app locally: 

1. Install respective dependencies (either manually from the requirements.txt file or by running the following command)
```
pip install -r requirements.txt
```

2. Run the app.
```
streamlit run app.py
```

# Development
The folders are organised in the following manner:

1. [Apps](./apps) - supplier visualisation plots and seller prediction model for the streamlit web dashboard
2. [Components](./components) - code for seller prediction model and saved models
3. [Assets](./data) - supplier and seller datasets
4. [notebooks](./notebooks) - initial workings and code to generate bias for target variable 'return' in seller dataset 
