import json
import pandas as pd

# Load the json file
with open('regiones.json', encoding='utf-8') as f:
    data = json.load(f)

# Extract the "features" list from the json data
features = data['features']

# Define an empty list to store the region data
regions = []

# Loop through each feature and extract the region data
for feature in features:
    properties = feature['properties']
    region = {
        'id': properties['codregion'],
        'name': properties['Region'],
        'geometry': json.dumps(feature['geometry'])
    }
    regions.append(region)

# Create a dataframe from the regions list
df = pd.DataFrame(regions)
df = df.rename(columns={'name': 'Region'})

# Write the dataframe to a csv file
df.to_csv('regiones.csv', index=False)
