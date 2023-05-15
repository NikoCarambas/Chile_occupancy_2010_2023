# Docs 
# Local host https://docs.streamlit.io/library/api-reference#streamlit.selectbox
# Plot library https://plotly.com/python/choropleth-maps/
# Plot library https://plotly.com/python/map-configuration/
# Choropleth maps https://python-visualization.github.io/folium/quickstart.html#Choropleth-maps
# Side bar https://python-visualization.github.io/folium/plugins.html
# Folium options https://leafletjs.com/reference-1.6.0.html#map

import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium
from streamlit_folium import folium_static
import json

from folium.plugins import StripePattern
import geopandas as gpd
import numpy as np
from IPython.display import display

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Defined tittle and subtittle of the Board.
APP_TITLE = 'Regiones de Chile'
APP_CAPTION = 'Source: INE <https://bancodatosene.ine.cl>'

# Define the filepath for the Chile GeoJSON file.
geojson_path = 'regiones.json'
data_directory = 'Diferencia_mapa_2017.csv'


# Function to display the value for the Total of the country (contained in the Data set)
def display_total(df_year, year):
    df_year = df_year[df_year['Año'] == year]
    total = df_year.loc[df_year['Region'] == 'Total país', 'Diferencia_Hombres_Mujeres'].iloc[0]
    st.metric("Total País", '{:,.3f}'.format(total))

# Function to display the max value with the state name
def display_max(df_year, year):
    df_year = df_year[df_year['Año'] == year]
    max_row = df_year.loc[df_year['Diferencia_Hombres_Mujeres'].idxmax()]
    region_name = max_row['Region']
    max_value = max_row['Diferencia_Hombres_Mujeres']
    st.metric(region_name, '{:,.3f}'.format(max_value))

# Function to display the min value with the state name
def display_min(df_year, year):
    df_year = df_year[df_year['Año'] == year]
    min_val_int = df_year.loc[df_year['Diferencia_Hombres_Mujeres'].idxmin()]
    min_value = min_val_int.astype(str)
    st.metric(min_val_int['Region'], '{:,.3f}'.format(min_val_int['Diferencia_Hombres_Mujeres']))

# Map variables
# Define the center of the map.
center = [-38, -70]
# Define the initial zoom level of the map.
zoom = 4


def display_map(df, year):

    # df_year is df filtered by year
    df_year = df[df['Año'] == year]

    # Drop the rows where the value of "Region" column is "Total país"
    df_year = df_year[df_year['Region'] != 'Total país']
    # We grab the Region and Diferencia column
    df_year = df_year[["Region","Diferencia_Hombres_Mujeres"]]

    # Next we import the datas. 
    chile_geojson = gpd.read_file('regiones.json')

    # Next we merge our sample data (df) and the geoJSON data frame on the key id.
    final_df = pd.merge(chile_geojson, df_year, on = "Region")

    # Initialize folium map.

    m = folium.Map(location=center, zoom_start=zoom, tiles='cartodbpositron',
                   zoom_control=False,
                   scrollWheelZoom=False,
                   dragging=False,
                   labels=False,
                   )

    # Set up Choropleth map
    folium.Choropleth(
    geo_data=final_df,
    data=final_df,
    columns=['Region',"Diferencia_Hombres_Mujeres"],
    key_on="feature.properties.Region",
    fill_color='YlOrRd',
    fill_opacity=1,
    line_opacity=0.2,
    legend_name="wills",
    smooth_factor=0,
    Highlight= True,
    line_color = "#0000",
    name = "Wills",
    show=False,
    overlay=True,
    nan_fill_color = "White"
    ).add_to(m)

    # Add hover functionality.
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}
    NIL = folium.features.GeoJson(
        data=final_df,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['Region', 'Diferencia_Hombres_Mujeres'],
            aliases=['Region', 'Dif. pp'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
            localize=True,
            labels=True,
            sticky=True,
            fmt='.2f'  # only show two decimal places
        )
    )

    m.add_child(NIL)
    m.keep_in_front(NIL)

    return m

def main():
    
    st.title(APP_TITLE)
    st.caption(APP_CAPTION)
    st.markdown('Cambie el Año graficado en el Panel Lateral')
    # Load Data
    df= pd.read_csv(data_directory)

    # Display SideBar Filters
    year_list = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    

    # Add radio buttons for year selection
    st.sidebar.title('Seleccione el Año')
    year = st.sidebar.selectbox('Período 2010-2023', year_list, len(year_list)-1)
    
    # Filter the Data by year
    df_year = df[df['Año'] == year]

    # Create a Folium map object
    chile_map = display_map(df_year, year)

    # Display the map in the Streamlit app
    folium_static(chile_map, height=700, width=600)

    state_name = 'Total país'
    field_name = 'Diferencia_Hombres_Mujeres'
    metric_title = 'Promedio'

    # Display facts
    st.subheader('Datos importantes')
    col1, col2, col3 = st.columns(3)
    with col1:
        display_total(df_year, year)
        st.markdown('Valor promedio')          
    with col2:
        display_max(df_year, year)
        st.markdown('Valor máximo')      
    with col3:
        display_min(df_year, year)      
        st.markdown('Valor mínimo')   

    # Display SideBar Instructions
    st.sidebar.header('Acerca de la medición')
    st.sidebar.markdown('')
    st.sidebar.markdown('La escala de colores del mapa se relaciona a una diferencia entre la ocupación de los hombres y las mujeres.')
    st.sidebar.markdown('Donde TOH es la Tasa de ocupación para los hombres y TOM es la Tasa de ocupación para las mujeres')
    st.sidebar.latex('diferencia = TOH-TOM')
    st.sidebar.caption('El resultado se debe interpretar en puntos porcentuales')

    st.markdown("""<style>div.row-widget.stRadio > div{margin-left: 0 !important;}</style>""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()