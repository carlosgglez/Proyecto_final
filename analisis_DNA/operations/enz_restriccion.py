'''
`enz_restriccion.py`: Modulo que se encarga de buscar todas las ocurrencias de las secuencias de reconocimiento de 
las enzimas de restricción dentro de una secuencia de ADN dada.

Se definen dos parámetros; `dna`(para la secuencia de DNA) y `enzymes` para definir la enzima de restricción 
para la cual buscar su secuencia de reconocimiento

Funcionalidad:
- `find_restriction_sites`: Funcion encargada de encontrar las ocurrencias de las secuencias de reconocimiento de las enzimas 
'''

def find_restriction_sites(dna, enzymes):
    ''' 
    Se crea un diccionario vacío llamado 'sites' donde las claves son los nombres de las enzimas
    y los valores son listas vacías.
    '''
    sites = {enzyme: [] for enzyme in enzymes}
    
    #Se itera sobre el diccionario 'enzymes'
    for enzyme, recognition_seq in enzymes.items():
        # Se busca la primera ocurrencia de la secuencia de reconocimiento de la enzima actual dentro de la secuencia de ADN.
        pos = dna.find(recognition_seq)
        
        # Se inicia un bucle while para buscar todas las ocurrencias de la secuencia de reconocimiento dentro de la secuencia de ADN.
        while pos != -1:
            # Se añade la posición de la ocurrencia encontrada al valor correspondiente en el diccionario 'sites'.
            sites[enzyme].append(pos)
            
            '''
            Se realiza una optimización para avanzar la posición de búsqueda más allá de la última ocurrencia encontrada.
            Esto ayuda a evitar encontrar la misma ocurrencia repetidamente.
            '''
            pos = dna.find(recognition_seq, pos + len(recognition_seq))
    
    #Se devuelve el diccionario 'sites', que contiene las posiciones de todas las ocurrencias de las enzimas 
    return sites

# Diccionario que contiene las secuencias de reconocimiento para algunas enzimas de restricción.
ENZIMAS_RESTRICCION = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT"
}

