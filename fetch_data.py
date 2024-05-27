import requests
import geopandas as gpd
from shapely.geometry import Point

def fetch_location_data(query):
    url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    response = requests.get(url)
    data = response.json()
    return data

def create_geodataframe(data):
    latitudes = [float(item['lat']) for item in data]
    longitudes = [float(item['lon']) for item in data]
    geometries = [Point(lon, lat) for lon, lat in zip(longitudes, latitudes)]
    gdf = gpd.GeoDataFrame(geometry=geometries)
    return gdf

if __name__ == "__main__":
    query = "New York, USA"
    data = fetch_location_data(query)
    gdf = create_geodataframe(data)
    print(gdf)
    gdf.to_file("data/locations.geojson", driver="GeoJSON")

