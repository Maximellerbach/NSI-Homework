import statistics
import time

listes_data = [[(7,13), (4,12), (3,8), (3,10)], 
            [(442, 41),(525, 50),(511, 49),(593, 59),(546, 55),(564, 57),(617, 60)], 
            [(15, 2),(100, 20),(90, 20),(60, 30),(40, 40),(15, 30),(10, 60),(1, 1)], 
            [(92, 23),(57, 31),(49, 29),(68, 44),(60, 53),(43, 38),(67, 63),(84, 85),(87, 89),(72, 82)], [(214, 113),(229, 118),(192, 98),(150, 80),(173, 90),(139, 73),(240, 120),(156, 82),(135, 70),(163, 87),(221, 115),(201, 106),(149, 77),(184, 94),(210, 110)]]

poids_data = (30, 170, 102, 165, 750)

def axis_sort(L, n, reverse=False): # utilise le timsort
    assert n in range(len(L[0])) 
    return sorted(L, key= lambda x: x[n], reverse=reverse)

def evaluer_fonction(fonction, iteration=100):
    """
    calcule le temps moyen d'execution d'une fonction (exercice A, B et C)
    """
    
    elapsed_times = []

    for liste, p_max in zip(listes_data, poids_data):

        start = time.perf_counter()
        for _ in range(iteration):
            _ = fonction(liste, p_max)

        end = time.perf_counter()
        elapsed_times.append((end-start)/iteration)

    return elapsed_times

def glouton(l, maxi): # generic function for the glouton algorithm
    """ 
    l est une liste tel que: [(valeurs, poids)]
    maxi est le poids maximum que peut porter le sac
    """
    
    reponse = []
    tot_valeur = 0
    tot_poids = 0
    for valeur, poids in l:
        if poids+tot_poids<=maxi:
            tot_valeur += valeur
            tot_poids += poids
            reponse.append(1)
        else:
            reponse.append(0)
    return reponse, tot_valeur, tot_poids

def exercice_1():
    def extraire(L, n):
        return axis_sort(L, n)

    L = [[1, 5, 6], [8, 10, 2], [3, 3, 5],[4, 8, 1]]
    return extraire(L, 1)

def exercice_A(liste, poids_max):
    liste_trie_poids = axis_sort(liste, 0, reverse=True)
    return glouton(liste_trie_poids, poids_max)
    
def exercice_B(liste, poids_max):
    liste_trie_poids = axis_sort(liste, 1, reverse=True)
    return glouton(liste_trie_poids, poids_max)

def exercice_C(liste, poids_max):
    def sort_vpp(l, reverse=False):
        return sorted(l, key=lambda x: x[1]/x[0], reverse=reverse)

    liste_trie_poids = sort_vpp(liste, reverse=True)
    return glouton(liste_trie_poids, poids_max)


if __name__ == "__main__":
    sorted_list = exercice_1()
    print("liste triée pour l'exercice 1:", sorted_list)


    for liste, p_max in zip(listes_data, poids_data):
        print(exercice_A(liste, p_max), exercice_B(liste, p_max), exercice_C(liste, p_max))


    temps_A = evaluer_fonction(exercice_A)
    print("temps d'execution de la fonction GloutonP", temps_A)

    temps_B = evaluer_fonction(exercice_B)
    print("temps d'execution de la fonction GloutonV", temps_B)
    
    temps_C = evaluer_fonction(exercice_C)
    print("temps d'execution de la fonction GloutonVPP", temps_C)
    
