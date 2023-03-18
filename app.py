import streamlit as st
from multiapp import MultiApp
from apps import platform_dashboard_app, supplier2_dashboard_app,platform_prediction_app

app = MultiApp()

app.add_app("Supplier Dashboard", platform_dashboard_app.app)
app.add_app("Platform Dashboard", supplier2_dashboard_app.app)
app.add_app("Platform Model", platform_prediction_app.app)

app.run()