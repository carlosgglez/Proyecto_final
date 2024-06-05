from Bio import SeqIO
from Bio.Seq import Seq
import sys 
sys.path.append("")
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
    print("Te amo Jenni")