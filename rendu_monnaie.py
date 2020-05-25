def exercice_1():
    def rendmonnaie(s, c):
        somme_centime = s*100 # transforme la somme en centimes
        pieces_rendu = []
        for piece in c:
            nombre_piece_max = int(somme_centime//piece)
            somme_centime -= nombre_piece_max*piece
            pieces_rendu.append(nombre_piece_max)

        return pieces_rendu

    caisse = [200, 100, 50, 20, 10, 5, 2, 1] # liste de toutes les pièces de monnaie en centime
    rendu = rendmonnaie(2.34, caisse)
    print("rendu:", rendu)

def exercice_2():
    def rendmonnaie2(s, c):
        somme_centime = s*100 # transforme la somme en centimes
        pieces_rendu = []
        for piece in c:
            nombre_piece_max = int(somme_centime//piece)
            somme_centime -= nombre_piece_max*piece
            pieces_rendu.append([piece, nombre_piece_max])

        return pieces_rendu

    caisse = [200, 100, 50, 20, 10, 5, 2, 1] # liste de toutes les pièces de monnaie en centime
    rendu = rendmonnaie2(2.34, caisse)
    print("rendu:", rendu)

def exercice_3():
    import random
    def rendmonnaie3(s, c):
        somme_centime = s*100 # transforme la somme en centimes
        pieces_rendu = {}
        for piece in c:
            nombre_piece_max = int(somme_centime//piece)
            if nombre_piece_max>c[piece]:
                nombre_piece_max = c[piece]
            somme_centime -= nombre_piece_max*piece
            pieces_rendu[piece] = nombre_piece_max

        if somme_centime != 0:
            print("il n'y a plus de monnaie disponible, il manquait:", int(somme_centime), "centimes")

        return pieces_rendu

    keys = [200, 100, 50, 20, 10, 5, 2, 1]
    caisse2 = {}
    for k in keys:
        caisse2[k] = random.randint(0, 5)

    print("caisse:", caisse2)
    rendu = rendmonnaie3(2.34, caisse2)
    print("rendu:", rendu)

if __name__ == "__main__":
    print("Exercice 1")
    exercice_1()
    print("Exercice 2")
    exercice_2()
    print("Exercice 3")
    exercice_3()