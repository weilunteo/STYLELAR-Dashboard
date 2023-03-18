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
    supplier_df = pd.read_csv("data/textile_export_data.csv")
    # st.write(supplier_df.head())

    ## Treemap 1 - Country demand
    df = pd.DataFrame({
    'countries_exported': ['Vietnam', 'Malaysia', 'Indonesia', 'United States', 'China', 'Japan', 'Hong Kong', 'United Kingdom', 'Pakistan', 'Bangladesh', 'India', 'Turkey', 'Korea', 'Austria', 'Cambodia', 'Ukraine', 'Germany', 'Netherlands', 'France', 'Italy'],
    'qty_exported': [183658, 145270, 142822, 117830, 113158, 109436, 85612, 71378, 54813, 51622, 38243, 31082, 28595, 21918, 12694, 12607, 12482, 11196, 10707, 10361],
    'continent': ['Asia', 'Asia', 'Asia', 'North America', 'Asia', 'Asia', 'Asia', 'Europe', 'Asia', 'Asia', 'Asia','Asia','Asia', 'Europe', 'Asia','Europe', 'Europe', 'Europe','Europe', 'Europe' ]
    })
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

    df = supplier_df.groupby(['month_of_export', 'year_of_export'])['qty_exported'].sum()
    df = df.reset_index()
  
    # Define a dictionary to map month numbers to their names
    month_names = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }

    # Replace month numbers with their names
    df['month_of_export'] = df['month_of_export'].replace(month_names)

    # Sort the DataFrame by the "month_of_export" column
    df = df.sort_values(by=['year_of_export', 'month_of_export'], ascending=[True, True])

    fig2 = px.treemap(df, 
                    path=[px.Constant("Year"), 'year_of_export', 'month_of_export'], 
                    values='qty_exported',
                    color='year_of_export',
                    color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig2.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig2)





    ## Treemap 3 - Type of Products and materials
    st.header("Type of Products and Materials")

    df3 = supplier_df.groupby(['type_of_textile', 'type_of_product'])['qty_exported'].sum().sort_values(ascending=False)
    df3 = df3.reset_index()
    fig3 = px.treemap(df3, 
                      path=['type_of_textile', 'type_of_product'], 
                      values='qty_exported',
                      color='type_of_textile',
                      color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig3.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig3)

if __name__ == '__main__':
    app()
