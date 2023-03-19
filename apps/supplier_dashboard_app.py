import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    header = '''
        <h1>Treemap Dashboard (For Suppliers)</h1>
        <p style="text-align: justify">
        This dashboard helps suppliers to visualise the demand/distribution of the textile materials 
        and products exported by country, month and type of productS.
        </p>
    '''
    st.markdown(header, unsafe_allow_html = True)

    # Load the data
    supplier_df = pd.read_csv("data/supplier_dataset.csv")

    ## Treemap 1 - Country demand

    supplier_agg = supplier_df.groupby('countries_exported')['qty_exported'].sum().sort_values(ascending=False)
    df = pd.DataFrame(supplier_agg).reset_index()

    # st.write(df)
    continent = ['Asia', 'Asia', 'Asia', 'Asia', 'North America', 'Asia', 'Asia', 'Europe', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe']

    df['continent'] = continent

    st.header("Continent and Country")
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

    df2 = supplier_df.groupby(['month_of_export', 'year_of_export'])['qty_exported'].sum()
    df2 = pd.DataFrame(df2).reset_index()
  
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
    df2['month_of_export'] = df2['month_of_export'].replace(month_names)

    # Sort the DataFrame by the "month_of_export" column
    df2 = df2.sort_values(by=['year_of_export', 'month_of_export'], ascending=[True, True])

    # st.write(df2)

    fig2 = px.treemap(df2, 
                    path=[px.Constant("Year"), 'year_of_export', 'month_of_export'], 
                    values='qty_exported',
                    color='year_of_export',
                    color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig2.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig2)


    ## Treemap 3 - Type of Products and materials
    st.header("Type of Products and Materials")

    df3 = supplier_df.groupby(['textile_type', 'type_of_product'])['qty_exported'].sum().sort_values(ascending=False)
    df3 = df3.reset_index()
    fig3 = px.treemap(df3, 
                      path=['textile_type', 'type_of_product'], 
                      values='qty_exported',
                      color='textile_type',
                      color_discrete_sequence=['#00a0e3', '#0072c6', '#004b87'])
    fig3.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig3)


    ### 4 - Time Series Line Graph of Sales (per product)

    # st.header("Time Series Line Graph of Sales (per product)")

    # df4 = supplier_df.groupby(['year_of_export', 'month_of_export', 'type_of_product'])['qty_exported'].sum()
    # df4 = df4.reset_index()
    # fig4 = 



if __name__ == '__main__':
    app()
