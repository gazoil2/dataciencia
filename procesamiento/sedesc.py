import pandas as pd
path = "TablasLimpias/"
sedes_df = pd.read_csv(path + 'sedes_completos2.csv')

# ...existing code...

def normalize_social_media_format(url):
    """
    Normaliza el formato de URLs y handles de redes sociales
    """
    if pd.isna(url):
        return None
        
    url = url.strip().lower()
    
    # Patrones para cada red social
    patterns = {
        'twitter': ('twitter.com/', '@'),
        'facebook': ('facebook.com/', 'fb.com/'),
        'instagram': ('instagram.com/', '@'),
        'linkedin': ('linkedin.com/in/', '/company/'),
        'youtube': ('youtube.com/', 'youtu.be/'),
    }
    
    # Si es un correo, lo ignoramos
    if '@' in url and '.' in url.split('@')[1]:
        return url
        
    # Si es un handle (@usuario)
    if url.strip().startswith('@'):
        
        
        return f"https://x.com/{url[1:]}"
        
        
    # Si es una URL
    for network, (prefix, _) in patterns.items():
        if network in url:
            if not url.startswith(('http://', 'https://')):
                return f"https://{url}"
            return url
            
    return url

def analyze_social_media_format():
    total_entries = 0
    complete_urls = 0
    handle_only = 0
    url_percentage = 0
    gmail = 0
    missing = 0
    unknown = 0
    results = {}
    for _, row in sedes_df.iterrows():
        redes = row['redes_sociales']
        if pd.notna(redes):
            redes_lista = redes.split('  //  ')
            for red in redes_lista:
                if ":" in red or "twitter" in red or "facebook"  in red or "www." in red or "instagram" in red or "x.com" in red: #Algunas sedes tienen el handle de la red social sin link
                    complete_urls += 1
                elif red.strip().startswith("@"):
                    handle_only += 1
                elif "@" in red:
                    gmail += 1
                elif red.strip() == "" :
                    continue
                else: 
                    unknown += 1
                total_entries += 1
        else:
            missing += 1
    url_percentage = (complete_urls / total_entries * 100) if total_entries > 0 else 0
    results = {
        'total_entries': total_entries,
        'complete_urls': complete_urls,
        'handle_only': handle_only,
        'gmail': gmail,
        'missing': missing,
        'unknown': unknown,
        'url_percentage': round(url_percentage, 2)
    }
    
    return results

def replace_social_media_with_normalized():
    sedes_df['redes_sociales'] = sedes_df['redes_sociales'].apply(
        lambda x: '  //  '.join([normalize_social_media_format(url) for url in x.split('  //  ')]) if pd.notna(x) else x
    )
    sedes_df.to_csv("TablasLimpias/sedes_completos2.csv", index=False)

# Run analysis and display results
replace_social_media_with_normalized()
results = analyze_social_media_format()
print("\nAnálisis de Formato de URLs:")
print("==================================")
print(f"Entradas totales: {results['total_entries']}")
print(f"URLs completas: {results['complete_urls']}")
print(f"Solo handle: {results['handle_only']}")
print(f"Correos Gmail: {results['gmail']}")
print(f"Formato faltante: {results['missing']}")
print(f"Formato desconocido: {results['unknown']}")
print(f"Porcentaje de URLs completas: {results['url_percentage']}%")

print("==================================")