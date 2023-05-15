import pandas as pd

# Load the CSV file
df = pd.read_csv('Diferencia_mapa_2017.csv')

# Replace comma with a decimal point
df['Latitud'] = df['Latitud'].str.replace(',', '.')
df['Longitud'] = df['Longitud'].str.replace(',', '.')
df['Diferencia_Hombres_Mujeres'] = df['Diferencia_Hombres_Mujeres'].str.replace(',', '.').astype(float)

# Convert to float
df['Diferencia_Hombres_Mujeres'] = df['Diferencia_Hombres_Mujeres'].astype(float)
df['Latitud'] = df['Latitud'].astype(float)
df['Longitud'] = df['Longitud'].astype(float)

# Rename the 'Región' column to 'Region'
df = df.rename(columns={'Región': 'Region'})

# Write the updated DataFrame to a CSV file
df.to_csv('Diferencia_mapa_2017_updated.csv', index=False)

