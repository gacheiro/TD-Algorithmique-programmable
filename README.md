# TD 6 (première partie - ISEL 3 - Algorithmique programmable)

- Objectifs : Modéliser et résoudre un problème de Recherche Opérationnelle, implémenter des heuristiques et vérifier expérimentalement la complexité algorithmique.
- Règles de base : Sauvegardez votre fichier régulièrement ; soyez rigoureux sur le nommage des classes, des variables et méthodes, etc. ; visez la simplicité ; testez le code, décomposez-le en fonctions / méthodes et ajoutez des commentaires.
- Activités demandées : Implémentez des classes et des heuristiques pour la résolution du **Problème de Voyageur de Commerce**.
- Remise de ce TD : Le TD sera évalué en contrôle continu à la fin de la séance de TD. Le travail réalisé devra également être **déposé sur Eurêka**. N'oubliez pas d'indiquer votre nom en commentaire au début du code source.

# Vacances en France

Paul et Laura sont un couple heureux qui vient en France pour leurs vacances. Leur plan est de louer une voiture et de passer leurs vacances à parcourir la France en visitant une liste de villes touristiques. Comme certaines des villes sont éloignées les unes des autres, ils souhaitent trouver le meilleur itinéraire (l'itinéraire avec la distance minimale) pour visiter toutes les villes de leur liste.

Étant donné que vous êtes un(e) programmeur(rice) compétent(e), Paul et Laura vous ont demandé de calculer le meilleur itinéraire pour leurs vacances. À partir d'une liste de villes et des distances entre chaque paire de villes, ils souhaitent que vous trouviez un itinéraire qui commence dans une ville, visite toutes les autres villes, et se termine dans la même ville de départ, en minimisant la distance parcourue.

Ils vous ont fourni les identifiants et les noms des villes qu'ils souhaitent visiter :

0. Paris
1. Nice
2. Lyon
3. Marseille
4. Bordeaux
5. Toulouse
6. Strasbourg
7. Lille
8. Nantes
9. Le Havre

Et les distances (en km) entre chaque paire de villes, représentées par leur identifiant. Par exemple, la distance de Paris (identifiant 0) au Havre (identifiant 9) est d'environ 200 km.

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 930 | 465 | 775 | 590 | 680 | 490 | 225 | 380 | 200 |
| 1 | 930 | 0 | 470 | 200 | 800 | 560 | 810 | 1120 | 1080 | 1280 |
| 2 | 465 | 470 | 0 | 315 | 540 | 535 | 490 | 700 | 600 | 670 |
| 3 | 775 | 200 | 315 | 0 | 640 | 400 | 730 | 975 | 910 | 1040 |
| 4 | 590 | 800 | 540 | 640 | 0 | 245 | 1000 | 800 | 350 | 660 |
| 5 | 680 | 560 | 535 | 400 | 245 | 0 | 910 | 880 | 560 | 870 |
| 6 | 490 | 810 | 490 | 730 | 1000 | 910 | 0 | 520 | 870 | 730 |
| 7 | 225 | 1120 | 700 | 975 | 800 | 880 | 520 | 0 | 590 | 290 |
| 8 | 380 | 1080 | 600 | 910 | 350 | 560 | 870 | 590 | 0 | 470 |
| 9 | 200 | 1280 | 670 | 1040 | 660 | 870 | 730 | 290 | 470 | 0 |

**Table 1:**  distances, en kilomètres, pour chaque paire de villes.

Votre mission est d'utiliser toutes les connaissances que vous avez acquises dans ce cours pour aider Paul et Laura dans leurs vacances en France !

## Implémentez une structure de données (tableau à deux dimensions) pour représenter les distances entre chaque paire de villes telles que présentées dans la Table 1.
   
💡 En Python, un tableau à deux dimensions peut être représenté comme suit (remplissez les "..." par les valeurs correspondantes), dont l'identifiant de la ville correspond à ses coordonées dans la matrice des distances. 

```python
matrices_des_distances = [
  [0, 930, ..., 380, 200],
  [930, 0, ..., 1080, 1280],
  ...
  [380, 1080, ..., 0, 470],
  [200, 1280, ..., 470, 0],
]
```

Ensuite, pour récupérer la distance entre deux villes comme 0 (Paris) et 9 (Le Havre), par exemple, il suffit d'utiliser leurs identifiants comme indices de la matrice :

```python
dist = matrices_des_distances[0][9]
```

## Modéliser les données du problème

1. Définissez une classe **Ville** contenant un identifiant et un nom de ville :
    1. Implémentez le constructeur prenant l'identifiant et le nom de la ville en paramètres.
    2. Implémentez les méthodes get pour récupérer l'identifiant et le nom de la ville.
2. Définissez une classe **Instance** contenant la liste des villes à visiter et la matrice des distances entre chaque paire de villes :
    1. Implémentez le constructeur avec les attributs passés en paramètres.
    2. Implémentez une méthode pour récupérer le nom de la ville à partir de son identifiant.
    3. Implémentez une méthode pour récupérer la distance entre une ville a et une ville b.
    4. Implémentez une méthode pour imprimer l'instance. C'est à dire, imprimer les villes à visiter.
3. Définissez une classe **Itinéraire** pour représenter une séquence de visite des villes :
    1. Implémentez le constructeur prenant l'instance du problème et un ordre de visite des villes.
    2. Implémentez une méthode pour imprimer l'itinéraire en commençant par la première ville à visiter et en terminant par la dernière ville à visiter.
    3. Implémentez une méthode pour calculer la distance totale de l'itinéraire basée sur la séquence de visite des villes.
  
## Modéliser les algorithmes pour résoudre le problème

1. Définissez une classe **Algorithme** qui va contenir les méthodes pour construire une solution (une solution est un objet de la classe Itinéraire).
2. Implémentez le constructeur prenant l’instance du problème en paramètre.
3. Implémentez une méthode pour l'heuristique de séquence aléatoire.

💡 En Python, pour mélanger une liste, utilisez la fonction `random.sample`. Par exemple :
```python
import random
...
séquence_aléatoire = random.sample(liste_des_villes, len(liste_des_villes))
```

4. Implémentez une méthode d’énumération - on énumère tous les itinéraires possible et on renvoie le plus court.

💡 En Python, l’ensemble des permutations d’une liste peut être obtenu avec la fonction `itertools.permutations`. Par example :
```python
import itertools
...
for perm in itertools.permutations(liste_des_villes):
    nouveau_itn = Itinéraire(instance, list(perm))
    ...
```

5. **[BONUS]** Implémentez une méthode pour l’heuristique du plus proche voisin - en partant d’une ville, on se déplace toujours vers la ville la plus proche qui n’a pas déjà été visitée.

## Testez les heuristiques pour trouver l'itinéraire le plus court pour visiter toutes les villes

1. Créez un objet de la classe **Ville** pour chacune des villes à visiter. Placez ces objets dans une liste des villes.
2. Créez l'instance du problème en utilisant la liste des villes ainsi que la matrice des distances.
3. Appelez la méthode pour imprimer l'instance du problème.
4. Créez un objet de la classe **Algorithme** pour calculer l'itinéraire le plus court pour visiter toutes les villes.
5. Appelez les différentes heuristiques implémentées dans la classe **Algorithme**. Pour chaque heuristique, faites une comparaison avec les autres en imprimant l'itinéraire et la distance totale parcourue, en km, de la solution trouvée par l'heuristique.

# TD 6 (seconde partie)

On poursuit le travail fait dans le TD précédent. Un code python reprenant les fonctionnalités
développées est disponible sur Eurêka.

1. Implémentez une méthode d’affichage graphique dans les classes Data et Cycle. Elles
utiliseront les fonctionnalités de pyplot, cf. les commentaires plus bas.

2. Implémentation d’une recherche locale : les mouvements de type 2-Opt permettent
de générer une solution voisine de la solution courante en remplaçant 2 arêtes par 2
autres. L’exploration du voisinage 2-Opt de la solution courante teste toutes les
possibilités de 2-Opt et applique le premier mouvement qui améliore la solution. Il
modifie la solution courante et retourne un booléen indiquant si la solution courante
a été améliorée. La recherche locale appelle l’exploration du voisinage tant qu’elle
améliore la solution courante.
    1. Implémenter la méthode `mvt2opt(s)` dans Algorithme.
    2. Implémenter la méthode `rechercheLocale(s)` dans Algorithme.

3. La recherche locale s’arrête dès que la solution courante est un optimum local. Une
manière simple de pallier ce défaut est d’utiliser une stratégie de type mutistart : à
chaque itération, on génère une solution aléatoire que l’on optimise avec la recherche
locale. On garde la meilleure solution obtenue. Implémenter la méthode
multistart(nb_iter) dans Algorithme.

4. Tracer un diagramme d’évolution de la qualité de la solution en fonction du temps de
calcul pour les deux approches suivantes :
    1. Multistart : à chaque fois que le record est amélioré, on note le temps de calcul
associé
    2. Idem, sans la recherche locale
    3. Que note-t-on ?

L’affichage de l’instance et de la solution utiliseront les fonctionnalités du package
`matplotlib.pyplot` :

```Python
import matplotlib.pyplot as plt
fig = plt.figure() # cree une figure
plt.title(‘titre de la figure’) # ajoute un titre
plt.xlabel(‘abscisses’) # ajoute le label des abscisses
plt.ylabel(’ordonnees’) # ajoute le label des ordonnees
plt.scatter(x,y) # affiche les points avec x et y, vecteurs des abscisses et des ordonnees
plt.plot(x,y) #trace une ligne brisée reposant sur la séquence de points dans les vecteurs x et y
fig.show() # affiche la figure -> dans l’onglet plot sous spyder
```

Le temps de calcul d’une fonction peut être obtenu en utilisant la fonction `time()` du
package time. Elle retourne le temps courant en secondes. Il faut donc faire la
différence entre le temps après la fonction et le temps avant la fonction :

```Python
import time
debut = time.time()
heuristique_1(instance)
duree = time.time() - debut
```
