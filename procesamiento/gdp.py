"""
    Utilizado para el analisis de datos sobre el PBI, verificar si hay datos faltantes
    sobre el PBI de 2023 en países, utilizando los datos originales.
"""
import pandas as pd

# Read the GDP data
gdp_df = pd.read_csv('TablasOriginales/gdp.csv', skiprows=4)
gdp_2023_corrected_df = pd.read_csv('TablasLimpias/gdp_2023.csv')
YEAR = '2023'

def analyze_gdp_data(given_df):
    """
        Analizar los datos de pbi por paises, toma toda la lista
    """

    # Agarrar el total de paises
    total_countries = len(given_df)

    # Contar cuantos tienen valores nulos o no asignados y cuantos si tienen valor asignado
    countries_with_gdp = given_df[YEAR].notna().sum()
    countries_without_gdp = given_df[YEAR].isna().sum()

    # Calcular el porcentaje en base a las dos sumas anteriores
    missing_percentage = (countries_without_gdp / total_countries) * 100

    country_results = {
        'total_countries': total_countries,
        'with_gdp': countries_with_gdp,
        'without_gdp': countries_without_gdp,
        'missing_percentage': round(missing_percentage, 2)
    }

    return country_results

def show_data_analysis(results, name):
    """
        Muestra y formatea los datos a consola para mostrar lo obtenido de resultados del dataframe
    """

    print(f"\n{name}")
    print("==================================")
    print(f"Total de Países/Territorios: {results['total_countries']}")
    print(f"Países/Territorios con datos PBI {YEAR}: {results['with_gdp']}")
    print(f"Países/Territorios sin datos PBI {YEAR}: {results['without_gdp']}")
    print(f"Porcentaje de países/territorios sin datos PBI: {results['missing_percentage']}%")
    print("==================================")

# Mostrar resultados y correr el analisis de ambos dataframe
show_data_analysis(analyze_gdp_data(gdp_df), f"Análisis de Datos PBI {YEAR}:")
show_data_analysis(analyze_gdp_data(gdp_2023_corrected_df), f"Valores corregidos del PBI {YEAR}:")
