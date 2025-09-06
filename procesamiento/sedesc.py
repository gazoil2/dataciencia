import pandas as pd
path = "TablasOriginales/"
sedes_df = pd.read_csv(path + 'sedes-completos.csv')

# ...existing code...

def analyze_social_media_format():
    # Columns to analyze
    social_columns = ['facebook', 'twitter', 'instagram', "linkedin", "youtube", "flickr"]
    total_handles = 0
    total_urls = 0
    results = {}
    total_handles = sedes_df["redes_sociales"].str.contains("@", na=False, case=False).sum()
    for network in social_columns:
        url_por_red = sedes_df["redes_sociales"].str.contains(network, 
                                                  case=False, 
                                                  na=False).sum()
        total_urls += url_por_red
    total_entries = total_urls + total_handles
    handle_count = total_entries - total_urls
    url_percentage = (total_urls / total_entries * 100) if total_entries > 0 else 0
            
    results = {
            'total_entries': total_entries,
            'complete_urls': total_urls,
            'handle_only': handle_count,
            'url_percentage': round(url_percentage, 2)
    }
    
    return results

# Run analysis and display results
results = analyze_social_media_format()
print("\nAnalisis de Formato de URLs:")
print("==================================")
print(f"Entradas totales: {results['total_entries']}")
print(f"URLs completas: {results['complete_urls']}")
print(f"Handle only: {results['handle_only']}")
print(f"URL format percentage: {results['url_percentage']}%")