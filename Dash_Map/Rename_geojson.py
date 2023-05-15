import json
# Open the file
with open('regiones.json', 'r') as f:
    chile_geojson = json.load(f)

    # Rename regions
    for feature in chile_geojson['features']:
        current_region = feature['properties']['Region']

        if current_region == "RegiÃ³n de Arica y Parinacota":
            feature['properties']['Region'] = "Región de Arica y Parinacota"

        elif current_region == "RegiÃ³n de TarapacÃ¡":
            feature['properties']['Region'] = "Región de Tarapacá"

        elif current_region == "RegiÃ³n de Antofagasta":
            feature['properties']['Region'] = "Región de Antofagasta"
            
        elif current_region == "RegiÃ³n de Magallanes y AntÃ¡rtica Chilena":
            feature['properties']['Region'] = "Región de Magallanes y La Antártica Chilena"

        elif current_region == "RegiÃ³n de AysÃ©n del Gral.IbaÃ±ez del Campo":
            feature['properties']['Region'] = "Región de Aysén del Gral. Carlos Ibáñez del Campo"

        elif current_region == "RegiÃ³n de Atacama":
            feature['properties']['Region'] = "Región de Atacama"

        elif current_region == "RegiÃ³n de Coquimbo":
            feature['properties']['Region'] = "Región de Coquimbo"

        elif current_region == "RegiÃ³n de ValparaÃ\xadso":
            feature['properties']['Region'] = "Región de Valparaíso"

        elif current_region == "RegiÃ³n Metropolitana de Santiago":
            feature['properties']['Region'] = "Región Metropolitana de Santiago"

        elif current_region == "RegiÃ³n de Los Lagos":
            feature['properties']['Region'] = "Región de Los Lagos"

        elif current_region == "RegiÃ³n de Los RÃ\xados":
            feature['properties']['Region'] = "Región de Los Ríos"

        elif current_region == "RegiÃ³n de La AraucanÃ\xada":
            feature['properties']['Region'] = "Región de La Araucanía"

        elif current_region == "RegiÃ³n del BÃ\xado-BÃ\xado":
            feature['properties']['Region'] = "Región del Biobío"

        elif current_region == "RegiÃ³n de Ã‘uble":
            feature['properties']['Region'] = "Región de Ñuble"

        elif current_region == "RegiÃ³n del Maule":
            feature['properties']['Region'] = "Región del Maule"

        elif current_region == "RegiÃ³n del Libertador Bernardo O'Higgins":
            feature['properties']['Region'] = "Región del Libertador Gral. Bernardo O'Higgins"


# Save the modified data back to the file
with open('regiones.json', 'w') as f:
    json.dump(chile_geojson, f)

