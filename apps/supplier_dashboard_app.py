import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import calendar
import altair as alt

def app():
    header = '''
        <h1>Market Insights (For Suppliers)</h1>
        <p style="text-align: justify">
        This dashboard provides suppliers with a visual representation of the global demand for textile materials and products
        geographically and temporally. This will help suppliers know a country's demand and 
        determine the best products and materials to export their products to, 
        as well as the best time of the year to export textiles.
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

    st.subheader("Country and Continent")
    desc1 = """
    <p style="text-align: justify;">This treemap shows the quantity of textile products exported 
    by different countries around the world, grouped by continent.</p>"""
    st.caption(desc1)

    fig = px.treemap(df, 
                     path=[px.Constant("World"), 'continent', 'countries_exported'], 
                     values='qty_exported',
                     color='continent',
                     color_continuous_scale='RdBu')
                    #  color_discrete_sequence=['purple', 'green', 'dark blue', 'salmon'])
    fig.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig)




    ## Treemap 2 - Month of exports

    st.subheader("Year and Month")

    desc2 = """
    <p style="text-align: justify;">This treemap shows the quantity of products exported 
    by different countries around the world, grouped by year and month of export.</p>"""
    st.caption(desc2)

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
                    color_continuous_scale='RdBu')
    fig2.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig2)


    ## Treemap 3 - Type of Products and materials
    st.subheader("Type of Product and Material")

    desc3 = """
    <p style="text-align: justify;">This treemap shows the quantity of textile products exported by 
    different countries around the world, grouped by type of product and textile material.</p>"""
    st.caption(desc3)


    df3 = supplier_df.groupby(['textile_type', 'type_of_product'])['qty_exported'].sum().sort_values(ascending=False)
    df3 = df3.reset_index()
    fig3 = px.treemap(df3, 
                      path=['textile_type', 'type_of_product'], 
                      values='qty_exported',
                      color='textile_type',
                      color_continuous_scale='RdBu')
    fig3.data[0].hovertemplate = '%{label}<br>Quantity Exported:%{value}'
    st.plotly_chart(fig3)


    ### 4 - Bar Chart for Month of Exports
    st.subheader("Trend for Month of Exports")

    desc4 = """
    <p style="text-align: justify;"> This is a bar chart that shows the overall distribution in the quantity of 
    textile products exported each month. </p>"""
    st.caption(desc4)

    df4 = supplier_df.groupby(['year_of_export', 'month_of_export'])['qty_exported'].sum()
    df4 = df4.reset_index()
    months = [calendar.month_name[i][:3] for i in range(1, 13)]
    # st.write(months)
    df4['month_of_export'] = pd.Categorical(df4['month_of_export'], categories=months, ordered=True)

    # sort the dataframe by month_of_export column
    df4 = df4.sort_values('month_of_export')
    # st.write(df4)

    # st.write(df)

    # Create the bar chart
    fig4 = px.bar(df4, 
                x='month_of_export', 
                y='qty_exported',
                color='qty_exported',
                color_discrete_sequence='RdBu')

    st.plotly_chart(fig4)

    ### 5 - Time Series Line Graph of Sales (per product)
    st.subheader("Demand for Textile Product Over the Years")

    desc5 = """
    <p style="text-align: justify;"> This is a time series line chart for the quantity 
    of your selected textile product exported each year, to better estimate the product's life cycle.
    </p>"""
    st.caption(desc5)

    df5 = supplier_df.groupby(['year_of_export', 'type_of_product'])['qty_exported'].sum()
    df5 = df5.reset_index()

    # filter dataframe by type_of_product
    product = st.selectbox('Select Product', df5['type_of_product'].unique())
    df_product = df5[df5['type_of_product'] == product]


    # create time series chart using Altair
    fig5 = px.line(df_product, x="year_of_export", y="qty_exported")

    # show chart in Streamlit
    st.plotly_chart(fig5)




if __name__ == '__main__':
    app()
