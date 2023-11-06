import os

def read_file(filename):
    """
    Lire un fichier et retourner les lignes sous forme de listes.
    """
    if os.path.exists(filename) :
        print(f"{filename} a ete trouve")
        # Lecture du fichier
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    else:
        print("Le fichier nest pas trouve")
        lines = []
    return lines
    
def is_identifiant(line) :
    """
    Test si une ligne de fasta est un identifant ou une séquence.
    """
    if ">" in line :
        return True
    else:
        return False