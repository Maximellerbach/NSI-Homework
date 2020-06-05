import random
import time

class Partie():
    def __init__(self, minmax=(0, 100000), flottant=False, manuel=True, au_hasard=False, log=True):
        '''
        minmax: tuple (int, int); définie les limites de la partie
        flottant: boolean; détermine si le nombre cherché doit être un flottant (True) ou un entier (False)
        manuel: boolean; détermine si la partie s'effectura de manière automatique (False) ou de manière manuelle (True)
        au_hasard: boolean; détermine si le nombre sera choisis au hasard (True) ou bien si l'utilisateur doit le préciser (False)
        log: boolean; influ sur l'utilisation de print() à chaque itération
        '''
        self.limites = minmax
        self.flottant = flottant
        self.manuel = manuel  
        self.au_hasard = au_hasard
        self.log = log

        if self.flottant == False:
            self.limites = (int(self.limites[0]), int(self.limites[1])) # force l'usage d'entiers (au cas où l'utilisateur soit malintentionné et qu'il donne des Floats !!!!)

        # creations d'un adversaire et d'un chercheur
        self.adversaire = CeluiQuiFaitDeviner(self)
        self.chercheur = Chercheur(self)

    def lancer_la_partie(self):
        '''
        fonction pour iterer entre le Chercheur et CeluiQuiFaitDeviner
        '''
        trouve = False
        while(trouve==False):
            trouve, valeur = self.chercheur.essayer_de_trouver()
        return self.chercheur.it, valeur

    def calculer_temps_execution(self, n=1):
        '''
        n: int; nombre de parties simulé, plus n est grand, plus le temps d'execution sera précis
        fonction qui mesure le temps d'execution de la partie
        '''
        start_time = time.time()
        for _ in range(n):
            self.lancer_la_partie()

            end_time = time.time()
            dt = end_time-start_time
        return dt/n # très souvent zéro (temps d'execution trop rapide) 


class Chercheur():
    '''
    objet contenant ce qui est nécéssaire pour trouver le nombre cherché et demander à CeluiQuiFaitDeviner s'il s'agit de ce nombre
    '''
    def __init__(self, partie):
        self.partie = partie
        self.min, self.max = self.partie.limites
        self.it = 0

    def demande_utilisateur(self, nombre):
        return self.partie.adversaire.repondre(nombre)

    def essayer_de_trouver(self):
        self.it += 1

        if self.partie.flottant:
            millieu = (self.max+self.min)/2
        else:
            millieu = (self.max+self.min)//2

        indication = self.demande_utilisateur(millieu)
        
        if indication == 0:
            self.max = millieu
        elif indication == 2:
            self.min = millieu
        elif indication == 1:
            return True, millieu
        return False, None


class CeluiQuiFaitDeviner(): # de beaux noms de variables
    '''
    objet contenant ce qui est nécéssaire pour choisir un nombre et repondre au Chercheur
    '''
    def __init__(self, partie):
        self.partie = partie
        self.choisir()

    def choisir(self):
        '''
        fonction pour choisir un nombre soit de manière aléatoire soit de manière manuelle en demandant à l'utilisateur
        '''
        if self.partie.au_hasard:
            if self.partie.flottant:
                self.nombre_a_trouver = random.uniform(self.partie.limites[0], self.partie.limites[1])
            else:
                self.nombre_a_trouver = random.randint(self.partie.limites[0], self.partie.limites[1])

        else:
            if self.partie.flottant:
                self.nombre_a_trouver = float(input('entrez un nombre entre '+str(self.partie.limites)+' :'))
            else:
                self.nombre_a_trouver = int(input('entrez un nombre entre '+str(self.partie.limites)+' :'))

        print("nombre à trouver:", self.nombre_a_trouver)


    def repondre(self, nombre):
        '''
        fonction pour répondre au Chercheur
        '''
        if self.partie.manuel:
            return int(input(str(nombre)+'; entrez 0 si votre nombre est plus petit, 1 si le compte est bon, 2 si il est plus grand '))
        else:
            if self.partie.log:
                print(nombre)
            return self.reponse_automatique(nombre)      

    def reponse_automatique(self, nombre):
        '''
        fonction pour répondre automatiquement au Chercheur
        '''
        if self.nombre_a_trouver == nombre:
            return 1
        elif self.nombre_a_trouver < nombre:
            return 0
        elif self.nombre_a_trouver > nombre:
            return 2


if __name__ == "__main__":
    
    # Exemple avec des entiers, nombre à chercher choisis aléatoirement, execution automatique:
    partie = Partie(minmax=(-50012, 420732), flottant=False, manuel=False, au_hasard=True, log=False) # initialisation de la partie
    nombre_iterations, nombre_trouve = partie.lancer_la_partie() # lance la partie
    
    print("le nombre était:", nombre_trouve, "| l'algorithme l'a trouvé après:", nombre_iterations, "itérations")
    
    
    '''
    # Exemple avec des flottants et en choisissant le nombre à chercher, execution automatique:
    partie = Partie(minmax=(-600012.49, 987143.7), flottant=True, manuel=False, au_hasard=False, log=False) # initialisation de la partie
    nombre_iterations, nombre_trouve = partie.lancer_la_partie() # lance la partie
    
    print("le nombre était:", nombre_trouve, "| l'algorithme l'a trouvé après:", nombre_iterations, "itérations")
    '''

    # Exemple de calcul du temps d'exectution:
    temps = partie.calculer_temps_execution(n=100)
    print("temps d'execution:", temps)