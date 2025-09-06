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
plt.figure(figsize=(12, 6))
sedes_por_region = sedes_df['region_geografica'].value_counts()
sns.barplot(x=sedes_por_region.values, 
           y=sedes_por_region.index,
           palette='viridis')

plt.title('Cantidad de Sedes por Región Geográfica', pad=20)
plt.xlabel('Cantidad de Sedes')
plt.ylabel('Región Geográfica')
plt.tight_layout()
plt.savefig(save_path + 'sedes_por_region.png')
plt.show()

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
plt.figure(figsize=(12, 6))
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
plt.show()

# Figure c: Relación entre PBI per capita y cantidad de sedes
plt.figure(figsize=(12, 6))

# Count sedes per country
sedes_por_pais = sedes_df.groupby('pais_iso_3').size().reset_index(name='cantidad_sedes')

# Merge with GDP data
relacion_df = sedes_por_pais.merge(gdp_df, 
                                  left_on='pais_iso_3',
                                  right_on='Country Code',
                                  how='left')

# Create scatter plot
sns.scatterplot(data=relacion_df,
                x='2023',
                y='cantidad_sedes')              # Transparency

plt.title('Relación entre PBI per Cápita y Cantidad de Sedes por País', pad=20)
plt.xlabel('PBI per Cápita 2023')
plt.ylabel('Cantidad de Sedes')
plt.tight_layout()
plt.savefig(save_path+'pbi_vs_sedes.png')
plt.show()