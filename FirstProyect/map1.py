import folium
import pandas as pd

map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)
fgv = folium.FeatureGroup(name="Volcanoes")
fgl = folium.FeatureGroup(name="Lakes")


# Leer datos de volcanes
volcanoes_data = pd.read_csv("data/Volcanoes.txt")
volcano_lat = list(volcanoes_data["LAT"])
volcano_lon = list(volcanoes_data["LON"])
volcano_elev = list(volcanoes_data["ELEV"])

# Leer datos de lagos
lakes_data = pd.read_csv("data/lakes.txt")
lake_lat = list(lakes_data["Latitude"])
lake_lon = list(lakes_data["Longitude"])
lake_name = list(lakes_data["Lake"])

# Agregar marcadores de volcanes
for lt, ln, el in zip(volcano_lat, volcano_lon, volcano_elev):
    fgv.add_child(folium.Marker(location=[lt, ln],
                               popup=str(el) + " m",
                               icon=folium.Icon(color='red')))

# Agregar marcadores de lagos
for lt, ln, name in zip(lake_lat, lake_lon, lake_name):
    fgl.add_child(folium.Marker(location=[lt, ln],
                               popup=name,
                               icon=folium.Icon(color='green')))

map.add_child(fgv)
map.add_child(fgl)
map.add_child(folium.LayerControl())
map.save("Map1.html")
