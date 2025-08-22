#Para cada país informar cantidad de sedes, cantidad de secciones en
#promedio que poseen sus sedes y el PBI per cápita del país en 2023.
#El orden del reporte debe respetar la cantidad de sedes (de manera
#descendente). En caso de empate, ordenar alfabéticamente por
#nombre de país. A modo de ejemplo, el resultado podría ser:


# RELEVANCIA Y DATOS NO NULOS

#cant_secciones = secciones_df.groupby('sede_id').size().reset_index(name='counts')
#cant_sedes = (
#    sedes_df.groupby('pais_iso_3')['sede_id']
#    .apply(list)          # junta todos los id_sede en una lista
#    .reset_index(name='ids')
#)

# Si también querés la cantidad:
#cant_sedes['counts'] = cant_sedes['ids'].apply(len)

#print(cant_sedes)