from turtle import color, fillcolor
import folium
import pandas as pd

map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)
fgv = folium.FeatureGroup(name="Volcanoes")
fgl = folium.FeatureGroup(name="Lakes")
fgw = folium.FeatureGroup(name="person")

# Leer datos de volcanes
volcanoes_data = pd.read_csv("data/Volcanoes.txt")
volcano_lat = list(volcanoes_data["LAT"])
volcano_lon = list(volcanoes_data["LON"])
volcano_elev = list(volcanoes_data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'

# Leer datos de lagos
lakes_data = pd.read_csv("data/lakes.txt")
lake_lat = list(lakes_data["Latitude"])
lake_lon = list(lakes_data["Longitude"])
lake_name = list(lakes_data["Lake"])

# Agregar marcadores de volcanes
for lt, ln, el in zip(volcano_lat, volcano_lon, volcano_elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                            radius=6,
                            popup=str(el) + " m",
                            fill_color=color_producer(el),
                            color="grey",  # Borde de color negro
                            fill_opacity=0.7))

# Agregar marcadores de lagos
for lt, ln, name in zip(lake_lat, lake_lon, lake_name):
    fgl.add_child(folium.CircleMarker(location=[lt, ln],
                               popup=name,
                               fill_color='blue',
                               fill_opacity=1))

def style_function(feature):
    population = feature['properties']['POP2005']
    if population < 10000000:
        return {'fillColor': 'green'}
    elif 10000000 <= population <= 20000000:
        return {'fillColor': 'orange'}
    else:
        return {'fillColor': 'red'}

fgw.add_child(folium.GeoJson(data=open('data/world.json','r',encoding='utf-8-sig').read(),
                             style_function=style_function))

map.add_child(fgw)
map.add_child(fgv)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Map1.html")
