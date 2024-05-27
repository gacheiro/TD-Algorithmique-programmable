import random

# Classe Ville
class Ville:
    def __init__(self, identifiant, nom):
        self.identifiant = identifiant
        self.nom = nom

    def get_identifiant(self):
        return self.identifiant

    def get_nom(self):
        return self.nom

# Classe Instance
class Instance:
    def __init__(self, villes, matrice_des_distances):
        self.villes = villes
        self.matrice_des_distances = matrice_des_distances

    def get_nom_ville(self, identifiant):
        for ville in self.villes:
            if ville.get_identifiant() == identifiant:
                return ville.get_nom()
        return None

    def get_distance(self, ville_a, ville_b):
        return self.matrice_des_distances[ville_a][ville_b]

    def imprimer_instance(self):
        print("Instance du problème :")
        for ville in self.villes:
            print(f"Ville {ville.get_identifiant()}: {ville.get_nom()}")

# Classe Trajet
class Trajet:
    def __init__(self, instance, ordre_visite):
        self.instance = instance
        self.ordre_visite = ordre_visite

    def imprimer_trajet(self):
        trajet_str = " -> ".join([self.instance.get_nom_ville(ville) for ville in self.ordre_visite])
        print(f"Trajet : {trajet_str}")

    def calculer_distance_totale(self):
        distance_totale = 0
        for i in range(len(self.ordre_visite) - 1):
            distance_totale += self.instance.get_distance(self.ordre_visite[i], self.ordre_visite[i + 1])
        distance_totale += self.instance.get_distance(self.ordre_visite[-1], self.ordre_visite[0])
        return distance_totale

# Classe Algorithme
class Algorithme:
    def __init__(self, instance):
        self.instance = instance

    def heuristique_sequence_aleatoire(self):
        sequence_aleatoire = random.sample(range(len(self.instance.villes)), len(self.instance.villes))
        return Trajet(self.instance, sequence_aleatoire)

    def heuristique_plus_proche_voisin(self):
        non_visites = list(range(len(self.instance.villes)))
        ordre_visite = [non_visites.pop(0)]
        while non_visites:
            derniere_ville = ordre_visite[-1]
            plus_proche = min(non_visites, key=lambda ville: self.instance.get_distance(derniere_ville, ville))
            ordre_visite.append(plus_proche)
            non_visites.remove(plus_proche)
        return Trajet(self.instance, ordre_visite)

    def enumeration(self):
        from itertools import permutations
        villes = range(len(self.instance.villes))
        min_distance = float('inf')
        meilleur_trajet = None
        for perm in permutations(villes):
            trajet = Trajet(self.instance, list(perm))
            distance = trajet.calculer_distance_totale()
            if distance < min_distance:
                min_distance = distance
                meilleur_trajet = trajet
        return meilleur_trajet

# Test des heuristiques
def tester_heuristiques():
    # Création des objets Ville
    villes = [Ville(i, nom) for i, nom in enumerate(["Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille"])]

    # Matrice des distances (exemple)
    matrice_des_distances = [
        [0, 465, 775, 680, 930, 385, 490, 750, 585, 230],
        [465, 0, 315, 370, 475, 560, 385, 305, 500, 645],
        [775, 315, 0, 400, 205, 705, 745, 125, 605, 910],
        [680, 370, 400, 0, 470, 465, 920, 240, 245, 830],
        [930, 475, 205, 470, 0, 820, 665, 325, 780, 1150],
        [385, 560, 705, 465, 820, 0, 765, 545, 340, 610],
        [490, 385, 745, 920, 665, 765, 0, 800, 935, 485],
        [750, 305, 125, 240, 325, 545, 800, 0, 485, 885],
        [585, 500, 605, 245, 780, 340, 935, 485, 0, 800],
        [230, 645, 910, 830, 1150, 610, 485, 885, 800, 0]
    ]

    # Création de l'instance du problème
    instance = Instance(villes, matrice_des_distances)
    instance.imprimer_instance()

    # Création de l'objet Algorithme
    algorithme = Algorithme(instance)

    # Heuristique de séquence aléatoire
    trajet_aleatoire = algorithme.heuristique_sequence_aleatoire()
    trajet_aleatoire.imprimer_trajet()
    print(f"Distance totale (séquence aléatoire) : {trajet_aleatoire.calculer_distance_totale()} km")

    # Heuristique du plus proche voisin
    trajet_ppv = algorithme.heuristique_plus_proche_voisin()
    trajet_ppv.imprimer_trajet()
    print(f"Distance totale (plus proche voisin) : {trajet_ppv.calculer_distance_totale()} km")

    # Méthode d'énumération (Note: cela peut être très long pour un grand nombre de villes)
    trajet_enumeration = algorithme.enumeration()
    trajet_enumeration.imprimer_trajet()
    print(f"Distance totale (énumération) : {trajet_enumeration.calculer_distance_totale()} km")

# Appel de la fonction de test
tester_heuristiques()
