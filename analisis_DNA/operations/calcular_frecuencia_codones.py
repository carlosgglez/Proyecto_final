def calculate_codon_frequency(sequence):

    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    if any(c not in 'ACGT' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    
    total_codons = len(codons)
    
    codon_counts = {}
    
    for codon in codons:
        codon_counts[codon] = codon_counts.get(codon, 0) + 1
    
    codon_frequencies = {codon: count / total_codons * 100 for codon, count in codon_counts.items()}
    
    return codon_frequencies