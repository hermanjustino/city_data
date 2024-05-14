import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/data.xlsx")

gdf = gpd.read_file("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/neighbourhoods.geojson")


data = df.iloc[94:106]


# Print rows 107 to 122
pd.set_option('display.max_rows', 500)
print(df.iloc[106:122, [0, df.columns.get_loc("West Humber-Clairville")]])