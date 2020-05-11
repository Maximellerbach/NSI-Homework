import random

class parametre_partie:
    """
    objet qui permet de parametrer une partie
    """
    def __init__(self, grillelen=(6,7), grillesep=" ", joueurs={1:True, 2:True}, pions={0:'.', 1:'X', 2:'O'}, debut=1, affiche=True, puissance=4):
        self.grillelen = grillelen # taille de la grille lors de sa creation
        self.grillesep = grillesep # caractère qui sépare 2 pions
        self.joueurs = joueurs # True = vrai joueur, False = joueur qui joue aleatoirement
        self.pions = pions # definie le caractère utilisé pour dessiner les pions des joueurs
        self.debut = debut # quel joueur commence
        self.affiche = affiche # True = affiche à chaque coup la grille, False = ne l'affiche qu'à la fin de la partie
        self.puissance = puissance # nombre requis d'allignement pour gagner


def grille_vide(grillelen=(6,7)): # Question 1
    """
    creer une grille de 6 par 7 remplie de 0
    """
    t = []
    for i in range(grillelen[0]):
        t.append([0]*grillelen[1])
    return t

def affiche(grille, grillesep=" ", pions={0:'.', 1:'X', 2:'O'}): # Question 2
    """
    list -> None
    affiche la grille de jeu
    """
    str_toprint = ""
    for ligne in range(len(grille)):
        for v in grille[-(ligne+1)]:
            if v == 1:
                s = pions[1]+grillesep
            elif v== 2:
                s = pions[2]+grillesep
            else:
                s = pions[0]+grillesep
            str_toprint+=s
        str_toprint += '\n'
    print(str_toprint)

def coup_possible(grille): # Question 3
    """
    (grille) -> (coups_possibles)
    (list) -> (list)
    retourne la liste des coups possibles
    """
    pl = []
    for i in range(len(grille[0])):
        if grille[-1][i] == 0:
            pl.append(i)
    return pl


def jouer(grille, n_col, joueur):  # Question 4
    """
    (grille, n_col, joueur) -> (joueur)
    (list, int, int) -> (int)
    insere un pion à la place n_col pour le joueur auquel est le tour
    si n_col>len(grille) ou <0 ou n'est pas jouable, retourne joueur actuel
    """
    if n_col in coup_possible(grille):
        max_r = check_max(grille, n_col)
        grille[max_r][n_col] = joueur
        prochain_joueur = inversement_joueur(joueur)
        return prochain_joueur
    else:
        return joueur


def diagonal(grille, joueur, lig, col, puissance=4): # Question 5
    """
    verifie si il y a un alignement diagonal de N pions du joueur
    """
    maxi = puissance-1 # valeur maximale que va prendre i

    # diagonale droite
    compt = 0
    if lig+maxi < len(grille) and col+maxi < len(grille[0]):
        for i in range(puissance):
            if grille[lig+i][col+i] == joueur:
                compt+=1
            else:
                break

    if compt == puissance:
        return True

    # diagonale gauche
    compt = 0
    if lig+maxi < len(grille) and col-maxi >= 0:
        for i in range(puissance):
            if grille[lig+i][col-i] == joueur:
                compt+=1
            else:
                break
                
    if compt == puissance:
        return True
        
    return False


def vertical(grille, joueur, lig, col, puissance=4): # Question 5
    """
    verifie si il y a un alignement vertical de N pions du joueur
    """
    maxi = puissance-1 # valeur maximale que va prendre i
    compt = 0
    if lig+maxi < len(grille):
        for i in range(puissance):
            if grille[lig+i][col] == joueur:
                compt+=1
            else:
                break

    if compt == puissance:
        return True

    return False


def horizontal(grille, joueur, lig, col, puissance=4): # Question 5
    """
    verifie si il y a un alignement horizontal de N pions du joueur
    """
    maxi = puissance-1 # valeur maximale que va prendre i
    compt = 0
    if col + maxi <len(grille[0]):
        for i in range(puissance):
            if grille[lig][col+i] == joueur:
                compt+=1
            else:
                break

    if compt == puissance:
        return True

    return False

def victoire(grille, joueur, puissance=4): # Question 6
    """
    (grille, joueur) -> (boolean)
    (list, int) -> (bool)
    verifie si le joueur a gagné
    """
    for r in range(len(grille)):
        for c in range(len(grille[r])):
            v = vertical(grille, joueur, r, c, puissance=puissance)
            h = horizontal(grille, joueur, r, c, puissance=puissance)
            d = diagonal(grille, joueur, r, c, puissance=puissance)

            if v or h or d:
                return True
    return False

def match_nul(grille): # Question 7
    for i in range(len(grille[0])):
        if grille[-1][i] == 0:
            return False
    return True

def coup_aleatoire(grille, joueur): # Question 8
    """
    (grille, joueur) -> (prochain_joueur)
    (list, int) -> (int)
    effectue un coup aléatoire pour le joueur
    """
    cp = coup_possible(grille)
    col = random.choice(cp)
    next_j = jouer(grille, col, joueur)
    return next_j


def check_max(grille, n_col):
    """
    (grille, id_colonne) -> (nombre_de_pion)
    (list, int) -> (int)

    verifie le nombre de pion dans la colonne
    si la colonne est pleine, retourne -1
    """
    for i in range(len(grille)):
        if grille[i][n_col] == 0:
            return i
    return -1
    
def inversement_joueur(joueur):
    """
    inverse le role selon celui qui a jouer
    """
    if joueur == 1:
        return 2
    else:
        return 1


def random_vs_random(affiche_partie=True):
    """
    (affiche_partie) -> (joueur_gagnant)
    (bool) -> (int)
    
    joue une partie en considerant les deux joueurs comme jouant aléatoirement
    """
    grille = grille_vide()
    j = 1

    while(True):
        next_j = coup_aleatoire(grille, j)

        if affiche_partie == True:
            affiche(grille)
            
        if match_nul(grille) == True:
            affiche(grille)
            print("Match nul !", end="\n\n")
            return 0

        elif victoire(grille, j) == True:
            if affiche_partie == False:
                affiche(grille)
            print("le joueur "+str(j)+" a gagné", end="\n\n")
            return j
            
        j = next_j

def joueur_vs_random(affiche_partie=True):
    """
    (affiche_partie) -> (joueur_gagnant)
    (bool) -> (int)

    joue une partie en considerant que le joueur 1 est un vrai joueur
    et le joueur 2 jouant aléatoirement
    """

    grille = grille_vide()
    j = 1

    while(True):
        if j == 1:
            col = int(input("jouez en saississant un nombre entre 0 et 6 inclu : "))
            next_j = jouer(grille, col, j)
        else: 
            next_j = coup_aleatoire(grille, j)

        if affiche_partie == True:
            affiche(grille)
            
        if match_nul(grille) == True:
            affiche(grille)
            print("Match nul !", end="\n\n")
            return 0

        elif victoire(grille, j) == True:
            if affiche_partie == False:
                affiche(grille)
            print("le joueur "+str(j)+" a gagné", end="\n\n")
            return j
            
        j = next_j

def joueur_vs_joueur(affiche_partie=True):
    """
    (affiche_partie) -> (joueur_gagnant)
    (bool) -> (int)

    joue une partie en considerant que les deux joueurs sont des vrais joueurs
    """
     
    grille = grille_vide()
    j = 1

    while(True):
        col = int(input("jouez en saississant un nombre entre 0 et 6 inclu : "))
        next_j = jouer(grille, col, j)

        if affiche_partie == True:
            affiche(grille)
        
        if match_nul(grille) == True:
            affiche(grille)
            print("Match nul !", end="\n\n")
            return 0

        elif victoire(grille, j) == True:
            if affiche_partie == False:
                affiche(grille)
            print("le joueur "+str(j)+" a gagné", end="\n\n")
            return j
            
        j = next_j

def partie(param):
    """
    (parametre_partie) -> (joueur_gagnant)
    (class) -> (int)

    joue une partie suivant les parametres rentrés au préalable
    """
    grille = grille_vide(param.grillelen)
    j = param.debut

    while(True):
        if param.joueurs[j] == True:
            col = int(input(str(j)+", jouez en saississant un nombre entre 0 et 6 inclu : "))
            next_j = jouer(grille, col, j)
        else:
            next_j = coup_aleatoire(grille, j)

        if param.affiche == True:
            affiche(grille, grillesep=params.grillesep, pions=params.pions)

        if match_nul(grille) == True:
            if param.affiche == False:
                affiche(grille, grillesep=params.grillesep, pions=params.pions)
            print("Match nul !", end="\n\n")
            return 0

        elif victoire(grille, j, puissance = param.puissance) == True:
            if param.affiche == False:
                affiche(grille, grillesep=params.grillesep, pions=params.pions)
            print("le joueur "+str(j)+" a gagné", end="\n\n")
            return j

        j = next_j
            
            
        
if __name__ == "__main__":
    
    params = parametre_partie(grillelen=(12,14), joueurs={1:False, 2:False}, pions={0:'.', 1:'X', 2:'O'}, debut=1, affiche=False, puissance=7)
    partie(params)

