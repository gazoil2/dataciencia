#Para cada país informar cantidad de sedes, cantidad de secciones en
#promedio que poseen sus sedes y el PBI per cápita del país en 2023.
#El orden del reporte debe respetar la cantidad de sedes (de manera
#descendente). En caso de empate, ordenar alfabéticamente por
#nombre de país. A modo de ejemplo, el resultado podría ser:


# RELEVANCIA Y DATOS NO NULOS

#cant_secciones = secciones_df.groupby('sede_id').size().reset_index(name='counts')
#cant_sedes = (
#    sedes_df.groupby('pais_iso_3')['sede_id']
#    .apply(list)          # junta todos los id_sede en una lista
#    .reset_index(name='ids')
#)

# Si también querés la cantidad:
#cant_sedes['counts'] = cant_sedes['ids'].apply(len)

#print(cant_sedes)

import pandas as pd
pd.set_option('display.max_columns', None)

path = "TablasLimpias/"

sedes_df = pd.read_csv(path + 'sedes_completos.csv')
secciones_df = pd.read_csv(path + 'secciones.csv')
gdp_df = pd.read_csv(path + 'gdp_2023.csv')

sedes_por_pais = sedes_df.groupby('pais_iso_3').size().reset_index(name='cant_sedes')

secciones_por_sede = secciones_df.merge(sedes_df, on='sede_id')
secciones_stats = secciones_por_sede.groupby('pais_iso_3').agg({
    'sede_id': 'count'
}).reset_index()


secciones_stats = secciones_stats.merge(sedes_por_pais, on='pais_iso_3')
secciones_stats['promedio_secciones'] = secciones_stats['sede_id'] / secciones_stats['cant_sedes']


gdp_df = gdp_df.rename(columns={'Country Code': 'pais_iso_3', '2023': 'gdp_per_capita_2023'})

reporte1 = sedes_por_pais.merge(secciones_stats[['pais_iso_3', 'promedio_secciones']], on='pais_iso_3')
reporte1 = reporte1.merge(gdp_df[['pais_iso_3', 'gdp_per_capita_2023']], on='pais_iso_3', how='left')

reporte1 = reporte1.sort_values(['cant_sedes', 'pais_iso_3'], ascending=[False, True])

reporte1['promedio_secciones'] = reporte1['promedio_secciones'].round(2)
reporte1['gdp_per_capita_2023'] = reporte1['gdp_per_capita_2023'].round(2)

print("\nReporte de Sedes, Secciones y PBI per cápita por País:")
print("=" * 70)
print(reporte1.to_string(index=False))
print("=" * 70)

reporte1.to_csv('reportes/csv/reporte7A.csv', index=False)
