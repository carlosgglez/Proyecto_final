from Bio import SeqIO
from Bio.Seq import Seq
import sys 
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/Proyecto_final/analisis_DNA/operations")
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/Proyecto_final/analisis_DNA/utils")
from file_io import read_dna_sequence
from validators import validate_dna_sequence
from validators import validate_fasta_format
from calcular_contenido_nucleotidos import calculate_nucleotide_content
from calcular_frecuencia_codones import calculate_codon_frequency
from enz_restriccion import find_restriction_sites
from traduccion_dna import translate_sequence
import argparse

parser=argparse.ArgumentParser(description="El siguiente script sirve para analizar una secuencia de DNA, incluye distintas funcionalidades.")

parser.add_argument("Input_file",
                    help = "El nombre o la ruta al archivo FASTA que se quiera procesar",
                    type = str)

parser.add_argument("-n", "--Nucleotidos",
                    help = "El nucleotido para calcular cuantas veces aparece, por default son los 4 (A T G C)",
                    type = str,
                    default = "ATCG",
                    choices = ["A", "T", "G", "C"],
                    required = False)

parser.add_argument("-m", "--Marco_lectura",
                    help = "El marco de lectura a elegir, solo se puede FORWARD, inserte 0 para el mc 1, 1 para mc 2 o 2 para mc 3",
                    type = int,
                    default = 0,
                    choices = [0, 1, 2],
                    required = False)

parser.add_argument("-e", "--Enzima_restriccion",
                    help = "Nombre de la enzima de restricción a usar para encontrar los sitios de restricción",
                    type = str,
                    required = True)

args = parser.parse_args()

if __name__ == "__main__":
    print("Te amo Jenni.")

    #Abrimos archivo y realizamos validaciones de formato
    secuencia = read_dna_sequence(args.Input_file)
    val_fasta = validate_fasta_format(args.Input_file)
    validacion_secuencia = validate_dna_sequence(secuencia)
    if (validacion_secuencia):

        #Calculamos la frecuencia de nucleótidos 
        calculate_nucleotide_content(secuencia, args.Nucleotidos)

        #Calculamos la frecuencia de codones 
        frec_codons = calculate_codon_frequency(secuencia)
        print(f"La frecuencia de cada codón es: {frec_codons}")

        #Encontrar sitios de restricción para una enzima dada
        sitios = find_restriction_sites(secuencia, args.Enzima_restriccion)
        print(f"Los sitios de restricción encontrados para la enzima {args.Enzima_restriccion} son:\n {sitios}")

        #Traducción de la secuencia de DNA dada por el usuario 
        translate_sequence(args.Marco_lectura, secuencia)







