# <https://towardsdatascience.com/how-to-step-up-your-folium-choropleth-map-skills-17cf6de7c6fe>
# Choropleth paramethers: <https://python-visualization.github.io/folium/modules.html>

# We first import the libraries. 
import pandas as pd
import folium 
from folium.plugins import StripePattern
import geopandas as gpd
import numpy as np
from IPython.display import display

# Next we import the data. 
df = pd.read_csv("Diferencia_mapa_2017.csv")

# Next we import the datas. 
chile_geojson = gpd.read_file('regiones.json')
df= pd.read_csv('Diferencia_mapa_2017.csv')

print(type(df)) 

# df_year is df filtered by year
df_year = df[df['Año'] == 2019]

print(type(df_year)) 

# Drop the rows where the value of "Region" column is "Total país"
df_year = df_year[df_year['Region'] != 'Total país']
# We grab the Region and Diferencia column
df_year = df_year[["Region","Diferencia_Hombres_Mujeres"]]

# Checking the df_year metadata
df_year.head()
df_year.info()

# Checking the chile_geojson metadata
chile_geojson.head()
chile_geojson.info()

# Next we merge our sample data (df) and the geoJSON data frame on the key id.
final_df = pd.merge(chile_geojson, df_year, on = "Region")
final_df.head()

# Initialize folium map.

sample_map = folium.Map(location=[-40, -70], 
                        zoom_start=4, 
                        tiles='cartodbpositron',
                        zoom_control=False,
                        scrollWheelZoom=False,
                        dragging=False)

sample_map.save("map.html")

# The next step is to set up the Choropleth map.

# Set up Choropleth map
folium.Choropleth(
geo_data=final_df,
data=final_df,
columns=['Region',"Diferencia_Hombres_Mujeres"],
key_on="feature.properties.Region",
fill_color='YlGnBu',
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
).add_to(sample_map)

sample_map.save("map.html")
sample_map


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

sample_map.save("map.html")
sample_map

sample_map.add_child(NIL)
sample_map.keep_in_front(NIL)

sample_map.save("map.html")
sample_map
