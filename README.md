 SIMULATION DE PROPAGATION D'UNE ÉPIDÉMIE
DESCRIPTION DU PROJET

Ce projet simule la propagation d'une épidémie au sein d'une population de 16 personnes, modélisée à l'aide d'un graphe non orienté pondéré.

L'objectif est de visualiser l'impact des interactions sociales et de la mobilité sur la diffusion d'un virus.

Dans cette simulation :

Chaque individu est représenté par un nœud.

Chaque interaction sociale est représentée par une arête.

Le poids de l'arête correspond à la probabilité de transmission du virus, comprise entre 0.1 et 0.9.

 FONCTIONNEMENT DE LA SIMULATION

La simulation se déroule sur 10 jours.
À chaque étape, plusieurs mécanismes sont appliqués :

 Contamination

Les individus infectés peuvent transmettre le virus à leurs voisins selon le poids de l'arête qui les relie.

 Guérison

Les individus malades ont une probabilité de guérir et deviennent alors immunisés.

 Réinfection

Les individus guéris peuvent redevenir infectés, mais avec une faible probabilité.

 Mouvement

Les positions des nœuds sont recalculées afin de simuler des déplacements dans le réseau social.

Confinement

Le sommet L est volontairement isolé (degré 0) afin de tester l'efficacité d'une coupure totale des liens sociaux.

 ÉTATS DES INDIVIDUS

Les individus peuvent être dans trois états différents :

 SAIN (VERT)
Individu n'ayant pas encore contracté le virus.

 INFECTÉ (ROUGE)
Individu malade, entouré d'un halo de contamination.

GUÉRI (BLEU)
Individu ayant contracté la maladie et devenu immunisé.

 NOTIONS DU COURS APPLIQUÉES
 THÉORIE DES GRAPHES (NETWORKX)

Plusieurs concepts de théorie des graphes sont utilisés :

Graphe pondéré
Les arêtes possèdent des poids représentant les probabilités de transmission.

Mesures de centralité
La taille des nœuds dépend de leur degré (nombre de voisins), ce qui permet d'identifier les individus les plus connectés.

Sommets isolés
Certaines arêtes sont supprimées afin de créer un nœud de degré 0 (cas de l'individu L).

Layouts dynamiques
Utilisation de spring_layout avec une seed différente à chaque étape pour créer un effet de mouvement dans le réseau.

ANALYSE DE DONNÉES (MATPLOTLIB)

La bibliothèque Matplotlib est utilisée pour l'analyse et la visualisation :

Visualisation du graphe
Les probabilités de transmission sont affichées sur les arêtes grâce à
draw_networkx_edge_labels.

Bilan épidémique final
Un graphique final montre l'évolution du nombre d'individus :

sains

infectés

guéris

au cours des 10 jours de simulation.

 PROGRAMMATION PYTHON

Plusieurs concepts de programmation Python sont utilisés :

Compréhensions de listes
Pour optimiser le comptage des états et la génération des listes de couleurs.

F-strings
Pour créer des titres et rapports dynamiques durant la simulation.

Dictionnaires
Pour stocker l'état de santé de chaque individu dans le graphe.
