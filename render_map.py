# map
import folium
from branca.element import Figure
# [50.7087332,7.1296882]
def render_map(location, prefix, markertext):
    m1=folium.Map(location,zoom_start=11)
    folium.Marker(location ,popup=markertext).add_to(m1)
    m1.save("./assets/{}.html".format(prefix.lower()))

if __name__=='__main__':
    import json
    with open("./assets/locations.json", encoding="UTF8") as file:
        locations = json.load(file)
    for city in locations.keys():
        render_map(locations.get(city).get("geo"), city, locations.get(city).get("Marker"))
