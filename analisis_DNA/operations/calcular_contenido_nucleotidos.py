def calculate_nucleotide_content(DNA, nucleotide):
    
    if nucleotide=="A":
        print(f"El total de Adeninas es:{DNA.upper().count('A')}") 
    
    if nucleotide=="T":
        print(f"El total de Timinas es:{DNA.upper().count('T')}")

    if nucleotide=="G":
        print(f"El total de guaninas es:{DNA.upper().count('G')}")

    if nucleotide=="C":
        print(f"El total de citocinas es:{DNA.upper().count('C')}")

    if nucleotide=="ATGC":
        print(f"El total de cada base es: A:{DNA.upper().count('A')} C:{DNA.upper().count('C')} T:{DNA.upper().count('T')} G:{DNA.upper().count('G')}")

