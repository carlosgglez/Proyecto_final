'''
`transcrito_dna.py`: Módulo que se encarga de transcribir una secuencia de DNA dada por el usuario.
La transcripción de secuencias de ADN a ARN es crucial en muchos aspectos de la biología molecular y la biotecnología,
ya que proporciona información valiosa sobre la expresión y función génica, también es útil para el desarrollo de terapias génicas.

Se definen dos parámetros; frame (marco de lectura) y la secuencia de DNA.

Funcionalidad:
- `transcribe_sequence(frame, secuencia)`: Se encarga de transcribir la secuencia dada de DNA a RNA.

Ejemplo de uso:
- transcribe_sequence(0, "secuencia.fasta")
'''

from Bio import SeqIO

def transcribe_sequence(frame, secuencia):
    '''
    Transcribe a RNA una secuencia de DNA.

    Args:
        frame (int): El marco de lectura FORWARD a trabajar.
        secuencia (str): La secuencia de ADN a analizar.

    Returns:
        str: La secuencia de DNA transcrita a RNA
    '''
    for record in SeqIO.parse(secuencia, "fasta"):
        # Obtener la secuencia de ADN del registro y ajustarla al marco de lectura especificado
        sequence = record.seq[frame:]
        # Transcribir la secuencia directamente a RNA
        transcrite = sequence.transcribe()
        # Imprimir el identificador del registro, el marco de lectura y la secuencia de RNA transcrita
        print(f">{record.id}_frame{frame+1}\n{transcrite}\n")



