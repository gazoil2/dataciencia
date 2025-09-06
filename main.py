import pandas as pd 
pbi_2023_df = pd.DataFrame(columns=[
    "pais_iso_3",       # PK
    "pais_nombre",
    "pbi_2023"
])

# Tabla Sedes
sedes_df = pd.DataFrame(columns=[
    "sede_id",          # PK
    "pais_iso_3",       # FK -> PBI_2023
    "region_geografica",
    "redes_sociales",
    "pais_nombre_ingles"
])

# Tabla Secciones
secciones_df = pd.DataFrame(columns=[
    "seccion_id",       # PK
    "sede_id"           # FK -> Sedes
])