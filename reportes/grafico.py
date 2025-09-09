import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better visualizations
sns.set_theme(style="whitegrid") 
# Read cleaned data
path = "TablasLimpias/"
save_path = "graficos/"
sedes_df = pd.read_csv(path + 'sedes_completos.csv')
gdp_df = pd.read_csv(path + 'gdp_2023.csv')

# Figure a: Sedes por región geográfica
plt.figure(figsize=(15, 8))  # Increased size for better readability
sedes_por_region = sedes_df['region_geografica'].value_counts()

# Create bar plot
ax = sns.barplot(x=sedes_por_region.values, 
                y=sedes_por_region.index,
                palette='viridis')

# Add value labels inside bars
for i, v in enumerate(sedes_por_region.values):
    ax.text(1,  # x position (middle of bar)
            i,    # y position
            f' {v} ',  # text (value)
            color='white',
            fontweight='bold',
            ha='center',
            va='center',
            fontsize=10)

plt.title('Cantidad de Sedes por Región Geográfica', pad=20, fontsize=14)
plt.xlabel('Cantidad de Sedes', fontsize=12)
plt.ylabel('Región Geográfica', fontsize=12)
plt.tight_layout()
plt.savefig(save_path + 'sedes_por_region.png', dpi=300, bbox_inches='tight')

# Figure b: Boxplot PBI per cápita por región
# Merge data
datos_unidos = sedes_df.merge(gdp_df, 
                            left_on='pais_iso_3',
                            right_on='Country Code',
                            how='left')

# Calculate medians for ordering
medianas = datos_unidos.groupby('region_geografica')['2023'].median()
orden_regiones = medianas.sort_values(ascending=False).index

# Create boxplot
plt.figure(figsize=(15, 10))
sns.boxplot(data=datos_unidos,
           x='region_geografica',
           y='2023',
           order=orden_regiones,
           palette='viridis')

plt.title('PBI per Cápita 2023 por Región Geográfica', pad=20)
plt.xticks(rotation=45)
plt.xlabel('Región Geográfica')
plt.ylabel('PBI per Cápita 2023')
plt.tight_layout()
plt.savefig(save_path + 'pbi_por_region.png')

# Figure c: Relación entre PBI per capita y cantidad de sedes
plt.figure(figsize=(15, 8))

# Create custom color palette for regions with extra spaces to match data
region_colors = {
    'AMÉRICA  DEL  SUR': '#e74c3c',
    'ASIA': '#9b59b6',
    'EUROPA  OCCIDENTAL': '#2980b9',
    'AMÉRICA  DEL  NORTE': '#2ecc71',
    'EUROPA  CENTRAL  Y  ORIENTAL': '#3498db',
    'AMÉRICA  CENTRAL  Y  CARIBE': '#1abc9c',
    'ÁFRICA  SUBSAHARIANA': '#f1c40f',
    'OCEANÍA': '#e67e22',
    'ÁFRICA  DEL  NORTE  Y  CERCANO  ORIENTE': '#d35400'
}

# Count sedes per country and include region information
sedes_por_pais = sedes_df.groupby(['pais_iso_3', 'region_geografica']).size().reset_index(name='cantidad_sedes')

# Merge with GDP data
relacion_df = sedes_por_pais.merge(gdp_df, 
                                  left_on='pais_iso_3',
                                  right_on='Country Code',
                                  how='left')

# Create scatter plot with colors by region
sns.scatterplot(data=relacion_df,
                x='2023',
                y='cantidad_sedes',
                hue='region_geografica',
                palette=region_colors,
                s=50,  # Increase point size
                alpha=0.6)  # Add some transparency

plt.title('Relación entre PBI per Cápita y Cantidad de Sedes por País', pad=20, fontsize=14)
plt.xlabel('PBI per Cápita 2023 (USD)', fontsize=12)
plt.ylabel('Cantidad de Sedes', fontsize=12)

# Rotate legend labels if needed
plt.legend(title='Región Geográfica', bbox_to_anchor=(1.05, 1), loc='upper left')

# Format x-axis with thousand separators
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.tight_layout()
plt.savefig(save_path+'pbi_vs_sedes.png', dpi=300, bbox_inches='tight')