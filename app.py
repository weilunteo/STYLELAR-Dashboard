import streamlit as st
from multiapp import MultiApp
from apps import supplier_dashboard_app, platform_prediction_app

app = MultiApp()

# app.add_app("Supplier Dashboard", platform_dashboard_app.app)
app.add_app("Suppliers - Dashboard", supplier_dashboard_app.app)
app.add_app("Sellers - Prediction", platform_prediction_app.app)

app.run()