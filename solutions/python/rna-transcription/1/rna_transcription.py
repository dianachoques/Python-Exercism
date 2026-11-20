"""Transcribe una cadena de ADN a su complemento de ARN."""
COMPLEMENTO_ARN = {'G':'C','C':'G','T':'A','A':'U'}
_TABLA = str.maketrans(COMPLEMENTO_ARN)
def to_rna_optimized(dna_strand):
    invalidos = set(dna_strand) - set(COMPLEMENTO_ARN)
    if invalidos:
        raise ValueError(f"nucleótidos inválidos: {sorted(invalidos)}")
    return dna_strand.translate(_TABLA)
    
def to_rna(dna_strand):
    """Transcribe una cadena ADN a ARN.
    Args :
        dna_strand (str) : Cadena ADN  en mayusculas
    Returns:
        str : Cadena de ARN transcrita
    Raises:
        ValueError: si la cadena de entrada tiene caracteres que no son nucleotidos
    """
    invalidos = set(dna_strand) - set(COMPLEMENTO_ARN)
    if invalidos:
        raise ValueError(f"nucleótidos inválidos: {sorted(invalidos)}")

    return "".join(COMPLEMENTO_ARN[nucleotido]  for nucleotido in dna_strand)
