import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
df = pd.read_excel("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/data.xlsx")

# Convert the relevant rows to numeric
df.iloc[2589] = df.iloc[2589].apply(pd.to_numeric, errors='coerce')
df.loc[2584] = pd.to_numeric(df.loc[2584], errors='coerce')

# Calculate the rate for each neighborhood
df.loc['Rate'] = df.loc[2589] / df.loc[2584]

# Replace any infinities or NaNs with 0
df.loc['Rate'] = df.loc['Rate'].replace([np.inf, -np.inf], np.nan).fillna(0)

# Keep only the rate row and transpose the dataframe so that the neighborhoods are the index
df = df.loc[['Rate']].T
df.reset_index(inplace=True)
df.columns = ['Neighbourhood Name', 'Rate']

gdf = gpd.read_file("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/neighbourhoods.geojson")
gdf.rename(columns={'AREA_NAME': 'Neighbourhood Name'}, inplace=True)

# Merge the dataframes
df_merged = gdf.merge(df, on='Neighbourhood Name')

# Ensure that the data in the column is numerical
df_merged['Rate'] = pd.to_numeric(df_merged['Rate'], errors='coerce')

# Create the choropleth map
fig, ax = plt.subplots(1, 1)
df_merged.plot(column='Rate', ax=ax, legend=True, cmap='coolwarm')

# Set the title of the plot
plt.title('Commute over 60 minutes in Toronto neighborhoods')

# Show the plot
plt.show()