"""
    Genomic.py

    Debut
"""
import os
import sys
import argparse
from .tools import tool

def parse_fasta(lines) :
    """
    Parcourir les lignes du fasta pour créer un dictionnaire {identifiant : séquence} 
    """
    i = 0
    dict_seq_dna = {}
    identifiant = ""
    # Parcours des lignes
    while i < len(lines) :
        line = lines[i].strip()
        # Recupere l'identfiant de séquence
        if tool.is_identifiant(line) :
            identifiant = line
        else :
            # Si la sequence est sur plusieurs lignes, ajoute la nouvelle ligne de sequence à la sequence existante
            if identifiant in dict_seq_dna :
                dict_seq_dna[identifiant] = dict_seq_dna[identifiant] + line
            # Crée une nouvelle entrée dans le dictionnaire
            else :
                identifiant = identifiant.replace('>','')
                dict_seq_dna[identifiant] = line
        i = i+1
    return dict_seq_dna


def parse(filename):
    lines = tool.read_file(filename)
    dict_seq_dna = parse_fasta(lines)
    print(f'la sequence dict_seq_dna{dict_seq_dna}')
    
def convert_RNA(dict_seq_dna):
    """
    Convertir les séquences d'ADN en séquence d'ARN
    
    :param dict_seq_dna: Le dictiionnaire de séquence à convertir.
    
    :return: Un dictionnaire de séquence converties
    """
    seq_adn = {}
    for key, dna in dict_seq_dna.items():
        seq_rna = dna.replace('T', 'U')
        seq_adn[key] = seq_rna
    return(seq_adn)



#Point d'entrée principal du Script
def run():

    # Vérification du nombre d'arguments (si le nombre est different de 2)
    # if len(sys.argv) != 2:
    #     print("Utilisation: python genomic.py <nom_du_fichier>")
    #     sys.exit(1)

    # # Récupération du nom du fichier à partir des arguments de la ligne de commande (<nom_du_fichier>)
    # filename = sys.argv[1]
    
    
    parser = argparse.ArgumentParser(
        prog="transcription",
        usage="transcription filename --RNA",
        description="cette fonction fait la transcription de l'ADN",
    )
    
    parser.add_argument(
        "filename",
        type=str,
        help="Required argument: le chemin du fichier fasta",
    )
    
    parser.add_argument(
        "--RNA",
        action = 'store_true',
        help="Veuiller entrez un nombre",
        default= False
    )
        
    # Parse tous les arguments
    args = parser.parse_args()
    filename = args.filename
    
    lines = tool.read_file(filename)
    dict_seq_dna = parse_fasta(lines)
    if args.RNA :
        dict_seq_dna = convert_RNA(dict_seq_dna)
    print(dict_seq_dna)
    


if __name__=="__main__":
    run()
