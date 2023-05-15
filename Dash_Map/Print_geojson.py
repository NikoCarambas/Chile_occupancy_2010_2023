import json

with open('regiones.json') as f:
    chile_geojson = json.load(f)

for feature in chile_geojson['features']:
    print(feature['properties']['Region'])
