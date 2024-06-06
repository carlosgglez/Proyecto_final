'''
codon-frequency.py: Modulo para calcular el contenido de cada codon en secuencias de DNA.

Este módulo proporciona funciones para determinar el porcentaje de aparicipon de cada codon 
en una secuencia de ADN dada. Esto es util para estudios de ingeneria genetica ya que optimizar
la expresión de genes en sistemas heterólogos. Al seleccionar codones preferidos por el organismo 
huésped, se puede aumentar la eficiencia de la traducción y la producción de proteínas recombinantes.

Funciones:
- calculate_codon_frequency(sequence): Devuelve el porcentaje de apariciones de cada codon en la secuencia.

'''

def calculate_codon_frequency(sequence):
    '''
    Calcula el contenido porcentual de cada codon en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.

    Returns:
        float: El porcentaje de contenido de cada codon en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos.
    '''
    #Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    
    total_codons = len(codons)
    
    codon_counts = {}
    
    for codon in codons:
        codon_counts[codon] = codon_counts.get(codon, 0) + 1
    
    codon_frequencies = {codon: round(count / total_codons * 100, 3) for codon, count in codon_counts.items()}
    
    return codon_frequencies