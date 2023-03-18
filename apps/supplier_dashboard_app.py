import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    header = '''
        <h1>Treemap Dashboard (For Suppliers)</h1>
        <p style="text-align: justify">
        This is a dashboard to help suppliers visually understand the distribution of their textile materials 
        and products in the market, by country and also month.
        </p>
    '''
    st.markdown(header, unsafe_allow_html = True)

    # Load the data
    df = pd.read_csv("data/textile_export_data.csv")

    ## Treemap 1 - Country demand
    st.header("Country Demand")
    fig = px.treemap(df, 
                     path=[px.Constant("World"), 'continent', 'countries_exported'], 
                     values='qty_exported',
                     color='continent',
                     color_continuous_scale='RdBu',
                     color_discrete_sequence=['purple', 'green', 'dark blue', 'salmon'])
    fig.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig)

    ## Treemap 2 - Month of exports
    st.header("Month of Exports")
    data = df.groupby(['month_of_export', 'year_of_export'])['qty_exported'].sum()
    df2 = data.reset_index()
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    cat_dtype = pd.CategoricalDtype(categories=month_order, ordered=True)
    df2['month_of_export'] = df2['month_of_export'].astype(cat_dtype)
    sorted_df = df2.sort_values(by=['year_of_export', 'month_of_export'], ascending=[True, True])
    fig2 = px.treemap(df2, 
                      path=[px.Constant("Year"), 'year_of_export', 'month_of_export'], 
                      values='qty_exported',
                      color='year_of_export',
                      color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig2.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig2)

    ## Treemap 3 - Type of Products and materials
    st.header("Type of Products and Materials")
    df3 = df.groupby(['textile_type', 'type_of_product'])['qty_exported'].sum().sort_values(ascending=False)
    df3 = df3.reset_index()
    fig3 = px.treemap(df3, 
                      path=['textile_type', 'type_of_product'], 
                      values='qty_exported',
                      color='textile_type',
                      color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig3.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig3)

if __name__ == '__main__':
    app()
