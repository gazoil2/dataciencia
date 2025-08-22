import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
path = 'TablasOriginales/'
gdp_df = pd.read_csv(path + 'gdp.csv', skiprows=4)
sedes_df = pd.read_csv(path + 'sedes.csv')
sedes_completos = pd.read_csv(path + 'sedes-completos.csv')
secciones_df = pd.read_csv(path + 'secciones.csv')

# RELEVANCIA Y DATOS NO NULOS
gdp_2024 = gdp_df[["Country Code", "Country Name", "2024"]].dropna()
cant_secciones = secciones_df.groupby('sede_id').size().reset_index(name='counts')
cant_sedes = (
    sedes_df.groupby('pais_iso_3')['sede_id']
    .apply(list)          # junta todos los id_sede en una lista
    .reset_index(name='ids')
)

# Si también querés la cantidad:
cant_sedes['counts'] = cant_sedes['ids'].apply(len)

print(cant_sedes)