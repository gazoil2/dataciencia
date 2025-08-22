import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
path = 'TablasOriginales/'
gdp_df = pd.read_csv(path + 'gdp.csv', skiprows=4)
sedes_df = pd.read_csv(path + 'sedes.csv')
sedes_completos = pd.read_csv(path + 'sedes-completos.csv')
secciones_df = pd.read_csv(path + 'secciones.csv')

# RELEVANCIA
gdp_2023 = gdp_df[["Country Code", "Country Name", "2023"]].dropna()
gdp_2023.to_csv('TablasLimpias/gdp_2023.csv', index=False)

sedes_df = sedes_df[["sede_id", "pais_iso_3"]]
sedes_df.to_csv('TablasLimpias/sedes.csv', index=False)

sedes_completos = sedes_completos[["sede_id", "pais_iso_3","region_geografica", "redes_sociales"]]
sedes_completos.to_csv('TablasLimpias/sedes_completos.csv', index=False)

secciones_df = secciones_df[["sede_id"]]
secciones_df.to_csv('TablasLimpias/secciones.csv', index=False)