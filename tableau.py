def ligne(colonne, largeur):
    for i in range(colonne):
        print("+", "- "*largeur, end="")
    print("+")

def large(colonne, largeur):
    for i in range(colonne):
        print("|", "  "*largeur, end="")
    print("|")

def tableau(hauteur=0, largeur=0, colonne_hauteur=0, colonne_largeur=0):
    for i in range(colonne_hauteur):
        ligne(colonne_largeur, largeur)
        for i in range(hauteur):
            large(colonne_largeur, largeur)
    ligne(colonne_largeur, largeur)

tableau(hauteur=3, largeur=3, colonne_hauteur=3, colonne_largeur=3)