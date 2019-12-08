from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import folium

def index(requests):
    csv_df = pd.read_csv('file.csv')
    lat_long = list(zip(csv_df.y, csv_df.x))
    maps = folium.Map(location = (40.7829,-73.9654), tiles = 'OpenStreetMap', max_zoom = 18, zoom_control=True, zoom_start=15)

    for cor in lat_long:
    
        folium.Marker(location = [cor[0],cor[1]], fill_color='#43d9de', radius=8 ).add_to( maps ) 
    maps.save('map.html')
    
    return HttpResponse(maps.get_root().render())

# Create your views here.
