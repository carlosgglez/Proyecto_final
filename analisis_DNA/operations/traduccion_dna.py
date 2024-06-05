'''
`traduccion_dna.py`: Módulo que se encarga de traducir una secuencia de DNA dada por el usuario.
La traducción de secuencias de ADN a proteínas es crucial en muchos aspectos de la biología molecular y la biotecnología,
ya que proporciona información valiosa sobre la función y estructura de las proteínas en los organismos vivos. 

Se definen dos parámetros; frame(marco de lectura) y la secuencia de DNA 

Funcionalidad:
- `translate_sequence(frame, secuencia)`: Se encarga de traducir la secuencia dada de DNA a aminoácidos
Codones de parada los marca con un  `*` 

Ejemplo de uso:
- translate_sequence(0, "secuencia.fasta")

'''

def translate_sequence(frame, secuencia):
    '''
    Traduce a aminocidos una secuencia de ADN.

    Args:
        frame (int): El marco de lectura FORWARD a trabajar.
        secuencia (str): La secuencia de ADN a analizar.

    Returns:
        str: La secuencia de DNA traducida a aminoacidos
    '''
    for record in SeqIO.parse(secuencia, "fasta"):
        # Obtener la secuencia de ADN del registro y ajustarla al marco de lectura especificado
        sequence = record.seq[frame:]
        # Traducir la secuencia directamente a aminoácidos
        translated_sequence = sequence.translate()
        # Imprimir el identificador del registro, el marco de lectura y la secuencia de aminoácidos traducida
        print(f">{record.id}_frame{frame+1}\n{translated_sequence}\n")


