import pandas as pd
#Reportar agrupando por región geográfica: a) la cantidad de países en
#que Argentina tiene al menos una sede y b) el promedio del PBI per
#cápita 2023 de dichos países. Ordenar por el promedio del PBI per
#Cápita. 

path = "TablasLimpias/"
sc_df = pd.read_csv(path + 'sedes_completos.csv')
gdp_df = pd.read_csv(path + 'gdp_2023.csv')

paises_con_sedes = sc_df[['pais_iso_3', 'region_geografica']].drop_duplicates()
resultado = paises_con_sedes.merge(gdp_df, 
                                 left_on='pais_iso_3', 
                                 right_on='Country Code',
                                 how='left')
reporte2 = resultado.groupby('region_geografica').agg({
    'pais_iso_3': 'count', 
    '2023': 'mean'
}).reset_index()
reporte2.columns = ['Region Geografica', 'Cantidad de Paises', 'PBI per Capita Promedio']
reporte2 = reporte2.sort_values('PBI per Capita Promedio', ascending=False)
print("\nReporte por Región Geográfica:")
print("=" * 100)
print(reporte2.to_string(index=False))
print("=" * 100)

reporte2.to_csv('reportes/csv/reporte7B.csv', index=False)