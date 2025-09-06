#Confeccionar un reporte con la información de redes sociales, donde
#se indique para cada caso: el país, la sede, el tipo de red social y url
#utilizada. Ordenar de manera ascendente por nombre de país, sede,
#tipo de red y finalmente por url.

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
path = "TablasLimpias/"
# Leer el archivo de sedes completos
sedes_df = pd.read_csv(path + 'sedes_completos.csv')

# Función para separar las redes sociales y clasificarlas
def procesar_redes_sociales(redes):
    if pd.isna(redes):
        return []

    urls = [url.strip() for url in redes.split(' // ') if url.strip()]
    resultado = []

    for url in urls:
        red_social = ''
        if 'facebook' in url.lower():
            red_social = 'Facebook'
        elif 'instagram' in url.lower():
            red_social = 'Instagram'
        elif 'twitter' in url.lower() or 'x.com' in url.lower():
            red_social = 'Twitter/X'
        elif 'linkedin' in url.lower():
            red_social = 'LinkedIn'
        elif 'youtube' in url.lower():
            red_social = 'YouTube'
        elif 'flickr' in url.lower():
            red_social = 'Flickr'
        else:
            red_social = 'Otra'

        resultado.append({'tipo_red': red_social, 'url': url})

    return resultado

filas = []
for _, sede in sedes_df.iterrows():
    redes = procesar_redes_sociales(sede['redes_sociales'])
    for red in redes:
        filas.append({
            'pais': sede['pais_ingles'],
            'sede_id': sede['sede_id'],
            'tipo_red': red['tipo_red'],
            'url': red['url']
        })

# Crear DataFrame con todas las redes sociales
reporte = pd.DataFrame(filas)

# Ordenar según los criterios especificados
reporte = reporte.sort_values(['pais', 'sede_id', 'tipo_red', 'url'])

# Imprimir el reporte
print("\nReporte de Redes Sociales por País y Sede:")
print("=" * 120)
if len(reporte) > 0:
    print(reporte.to_string(index=False))
else:
    print("No se encontraron redes sociales registradas.")
print("=" * 120)

reporte.to_csv('reportes/csv/reporte4.csv', index=False)