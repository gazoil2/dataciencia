import pandas as pd
#Para saber cuál es la vía de comunicación de las sedes en cada país,
#nos hacemos la siguiente pregunta: ¿Cuán variado es, en cada el país,
#el tipo de redes sociales que utilizan las sedes? Se espera como
#respuesta que para cada país se informe la cantidad de tipos de redes
#distintas utilizadas. Por ejemplo, si en Chile utilizan 4 redes de
#facebook, 5 de instagram y 4 de twitter, el valor para Chile debería ser
#3 (facebook, instagram y twitter).
# Leer el archivo de sedes completos que contiene la información de redes sociales
path = "TablasLimpias/"
sedes_df = pd.read_csv(path + 'sedes_completos.csv')

# Crear un diccionario para almacenar las redes por país
paises_redes = {}

# Recolectar todas las redes por país
for _, row in sedes_df.iterrows():
    pais = row['pais_iso_3']
    redes = row['redes_sociales']

    if pais not in paises_redes:
        paises_redes[pais] = set()  # Usamos set para mantener redes únicas

    if pd.notna(redes):  # Verificar que no sea NaN
        redes_lista = redes.split('  //  ')
        for red in redes_lista:
            if ":" in red: #Algunas sedes tienen el handle de la red social sin link
                red_completa = red.split('/')[2] # El tercer lugar despues de la barra es el link, el primero es el http, y el segundo es en blanco, posterior es el link de la red social
                paises_redes[pais].add(red_completa)

print("Redes sin procesar:", paises_redes)
# Normalizar nombres de redes sociales
for key in paises_redes.keys():
    redes_actualizadas = set()
    for red in paises_redes[key]:
        if 'facebook.com' in red.lower():
            redes_actualizadas.add('Facebook')
        elif 'twitter.com' in red.lower() or 'x.com' in red.lower():
            redes_actualizadas.add('Twitter')
        else:
            redes_actualizadas.add(red)
    paises_redes[key] = redes_actualizadas

print("\nRedes después de normalizar:", paises_redes)
# Convertir el diccionario a DataFrame
variedades_redes = pd.DataFrame([
    {'País': pais, 'Cantidad de Redes Sociales Diferentes': len(redes)}
    for pais, redes in paises_redes.items()
])

# Ordenar por cantidad de redes sociales (descendente) y país (ascendente)
variedades_redes = variedades_redes.sort_values(
    ['Cantidad de Redes Sociales Diferentes', 'País'], 
    ascending=[False, True]
)

# Mostrar el reporte
print("\nVariedad de Redes Sociales por País:")
print("=" * 50)
print(variedades_redes.to_string(index=False))
print("=" * 50)

# Mostrar el detalle de tipos de redes por país
print("\nDetalle de tipos de redes por país:")
print("=" * 50)
for pais, redes in paises_redes.items():
    if len(redes) > 0:  # Solo mostrar países que tienen redes
        print(f"{pais}: {', '.join(sorted(redes))}")
print("=" * 50)



