import pandas as pd

# Read the Excel file
df = pd.read_excel("/Users/hermanjustino/Desktop/projects/youth_Summit/city_data/data/data.xlsx")


# Print rows 107 to 122
pd.set_option('display.max_rows', 500)
print(df.iloc[106:122, [0, df.columns.get_loc("West Humber-Clairville")]])