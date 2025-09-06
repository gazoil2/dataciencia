import pandas as pd
from colorama import init, Fore, Style

# Initialize colorama
init()
path = "TablasOriginales/"
secciones = pd.read_csv(path + 'secciones.csv')

# Analyze missing values
total_columns = len(secciones.columns)
missing_analysis = secciones.isnull().sum()
missing_percentages = (missing_analysis / len(secciones)) * 100
missing_dataset_percentage = 0

# Define critical fields and categories
critical_fields = {
    'Identificación básica': ['sede_id', 'sede_desc_castellano', 'tipo_seccion'],
    'Contacto principal': ['correo_electronico', 'telefono_principal']
}

# Initialize tracking variables
total_completeness = 0
total_fields = 0

print(f"\n{Fore.CYAN}Análisis de Campos Críticos:{Style.RESET_ALL}")
print("=" * 50)

# Analyze each category and its fields
for category, fields in critical_fields.items():
    for field in fields:
        if field in secciones.columns:
            completeness = (1 - secciones[field].isnull().sum() / len(secciones)) * 100
            total_completeness += completeness
            total_fields += 1
            
            # Color based on completeness percentage
            color = Fore.GREEN if completeness > 90 else (Fore.YELLOW if completeness > 50 else Fore.RED)
            print(f"{field}: {color}{completeness:.2f}% completo{Style.RESET_ALL}")
        else:
            print(f"{field}: {Fore.RED}Campo no encontrado{Style.RESET_ALL}")

overall_completeness = total_completeness / total_fields

print(f"\n{Fore.CYAN}Análisis de Valores Faltantes:{Style.RESET_ALL}")
print("=" * 50)
print(f"Total de columnas: {Fore.BLUE}{total_columns}{Style.RESET_ALL}")
print(f"\n{Fore.CYAN}Detalle por columna:{Style.RESET_ALL}")
print("-" * 50)

for column in secciones.columns:
    missing_count = missing_analysis[column]
    missing_percent = missing_percentages[column]
    missing_dataset_percentage += missing_percent
    
    print(f"{Fore.BLUE}Columna: {column}{Style.RESET_ALL}")
    print(f"  - Valores faltantes: {missing_count}")
    
    # Color for missing percentage
    color = Fore.GREEN if missing_percent < 10 else (Fore.YELLOW if missing_percent < 50 else Fore.RED)
    print(f"  - Porcentaje faltante: {color}{missing_percent:.2f}%{Style.RESET_ALL}")
    
    if missing_percent > 90:
        print(f"  - {Fore.RED}Advertencia: Más del 90% de los datos faltantes.{Style.RESET_ALL}") 
    elif missing_percent > 50:
        print(f"  - {Fore.YELLOW}Nota: Más del 50% de los datos faltantes.{Style.RESET_ALL}")
    
    if column in critical_fields['Identificación básica'] + critical_fields['Contacto principal']:
        print(f"  - {Fore.MAGENTA}Campo crítico{Style.RESET_ALL}")
    print("-" * 50)

print(f"Porcentaje total de datos faltantes en el dataset: {Fore.YELLOW}{missing_dataset_percentage/total_columns:.2f}%{Style.RESET_ALL}")

print("\n" + "=" * 50)
color = Fore.GREEN if overall_completeness > 90 else (Fore.YELLOW if overall_completeness > 50 else Fore.RED)
print(f"Completitud general en campos críticos: {color}{overall_completeness:.2f}%{Style.RESET_ALL}")