import geopandas as gpd

# Read the GeoJSON file
gdf = gpd.read_file("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/neighbourhoods.geojson")

# Access the AREA_NAME column
area_names = gdf['AREA_NAME']

# Print the area names
print(area_names)