'''
`transcrito_dna.py`: Módulo que se encarga de transcribir una secuencia de DNA dada por el usuario.
La trancrio de secuencias de ADN a proteínas es crucial en muchos aspectos de la biología molecular y la biotecnología,
ya que proporciona información valiosa sobre la expresión y función génica, también es útil para el desarrollo de terapias génicas  
Se definen dos parámetros; frame(marco de lectura) y la secuencia de DNA 

Funcionalidad:
- `trancribe_sequence(frame, secuencia)`: Se encarga de trancribir la secuencia dada de DNA a RNA
 

Ejemplo de uso:
- trancribe_sequence(0, "secuencia.fasta")

'''

from Bio import SeqIO

def transcribe_sequence(frame, secuencia):
    for record in SeqIO.parse(secuencia, "fasta"):
        # Obtener la secuencia de ADN del registro y ajustarla al marco de lectura especificado
        sequence = record.seq[frame:]
        # Trancribir la secuencia directamente a RNA
        transcrite = sequence.transcribe()
        # Imprimir el identificador del registro, el marco de lectura y la secuencia de RNA transcrita
        print(f">{record.id}_frame{frame+1}\n{transcrite}\n")

secuencia = "/Users/frida_galan/Desktop/PythonSEM2/Notes/seq.nt.fa"
transcribe_sequence(0, secuencia) 


