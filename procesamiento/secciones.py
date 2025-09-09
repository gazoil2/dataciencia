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

print("\n" + "=" * 50)
print(f"{Fore.CYAN}LIMPIEZA Y COMPARACIÓN DE DATASETS{Style.RESET_ALL}")
print("=" * 50)

# Store original metrics
original_metrics = {
    'columns': total_columns,
    'missing_percentage': missing_dataset_percentage/total_columns,
    'completeness': overall_completeness
}

# Modified column dropping section
print(f"\n{Fore.CYAN}Proceso de limpieza de columnas:{Style.RESET_ALL}")
print("=" * 50)

# More explicit column dropping with verification
columns_to_drop = []
for column, percentage in missing_percentages.items():
    if percentage > 90:
        columns_to_drop.append(column)
        print(f"Marcando para eliminar: {column} ({percentage:.2f}% valores faltantes)")

# Verify columns exist before dropping
secciones_cleaned = secciones.copy()
actually_dropped = []
for col in columns_to_drop:
    if col in secciones_cleaned.columns:
        secciones_cleaned.drop(columns=col, inplace=True)
        actually_dropped.append(col)

print(f"\n{Fore.GREEN}Columnas efectivamente eliminadas:{Style.RESET_ALL}")
for col in actually_dropped:
    print(f"- {col}: {missing_percentages[col]:.2f}% faltante")

print(f"\n{Fore.YELLOW}Verificación:{Style.RESET_ALL}")
print(f"Columnas originales: {len(secciones.columns)}")
print(f"Columnas eliminadas: {len(actually_dropped)}")
print(f"Columnas restantes: {len(secciones_cleaned.columns)}")

# Recalculate metrics for cleaned dataset
cleaned_total_columns = len(secciones_cleaned.columns)
cleaned_missing = secciones_cleaned.isnull().sum()
cleaned_missing_pct = (cleaned_missing / len(secciones_cleaned)) * 100
cleaned_missing_total = sum(cleaned_missing_pct)

# Recalculate completeness for critical fields
cleaned_completeness = 0
cleaned_fields = 0
for category, fields in critical_fields.items():
    for field in fields:
        if field in secciones_cleaned.columns:
            field_completeness = (1 - secciones_cleaned[field].isnull().sum() / len(secciones_cleaned)) * 100
            cleaned_completeness += field_completeness
            cleaned_fields += 1

cleaned_overall_completeness = cleaned_completeness / cleaned_fields if cleaned_fields > 0 else 0

# Compare metrics
print(f"\n{Fore.CYAN}Comparación de Métricas:{Style.RESET_ALL}")
print("=" * 50)
print(f"\n{Fore.YELLOW}Dataset Original:{Style.RESET_ALL}")
print(f"- Total columnas: {original_metrics['columns']}")
print(f"- Porcentaje promedio de valores faltantes: {original_metrics['missing_percentage']:.2f}%")

print(f"\n{Fore.GREEN}Dataset Limpio:{Style.RESET_ALL}")
print(f"- Total columnas: {cleaned_total_columns}")
print(f"- Porcentaje promedio de valores faltantes: {cleaned_missing_total/cleaned_total_columns:.2f}%")

secciones_cleaned.dropna(subset="sede_id", inplace=True)
# Save cleaned dataset
secciones_cleaned.to_csv('TablasLimpias/secciones.csv', index=False)
print(f"\n{Fore.GREEN}Dataset limpio guardado como 'secciones.csv'{Style.RESET_ALL}")
print("=" * 50)