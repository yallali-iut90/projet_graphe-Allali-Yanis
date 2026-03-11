 Simulation d'Épidémie sur Graphe Dynamique

Ce projet simule la propagation d'une maladie au sein d'une population modélisée par un graphe non orienté pondéré. L'objectif est de visualiser comment les interactions sociales et la mobilité influencent la diffusion d'un virus.
Description du projet

La simulation repose sur une population de 16 personnes. Chaque individu est un nœud, et chaque connexion sociale est une arête dont le poids représente la probabilité de transmission (de 0.1 à 0.9).
Fonctionnement de la simulation

La simulation se déroule sur 10 jours. À chaque étape :

    Contamination : Les infectés peuvent transmettre le virus à leurs voisins selon le poids de l'arête.

    Guérison : Les malades ont une chance de guérir (état immunisé).

    Réinfection : Une petite probabilité permet aux guéris de retomber malades.

    Mouvement : Les positions des nœuds sont recalculées à chaque pas de temps pour simuler les déplacements réels.

    Confinement : Le sommet "L" est volontairement isolé (degré 0) pour tester l'efficacité d'une coupure totale de liens sociaux.

Code couleur des états
État	Couleur	Description
Sain	🟢 Vert	Individu n'ayant pas encore contracté le virus.
Infecté	🔴 Rouge	Individu malade, entouré d'un halo de contamination.
Guéri	🔵 Bleu	Individu immunisé (temporairement ou non).
 Notions du cours appliquées

Ce projet met en pratique les concepts du cours de C. Guyeux sur les graphes en Python :
1. Théorie des Graphes (networkx)

    Graphe Pondéré : Attribution de poids aléatoires sur les arêtes pour modéliser des probabilités de transmission.

    Mesures de centralité : La taille des nœuds est liée à leur degré (nombre de voisins) pour identifier les individus les plus connectés.

    Sommets isolés : Suppression d'arêtes pour créer un nœud de degré 0 (Cas de l'individu "L").

    Layouts : Utilisation du spring_layout avec une modification de la seed à chaque étape pour générer du mouvement dynamique.

2. Analyse de données (matplotlib)

    Visualisation interactive : Affichage des probabilités sur les arêtes via draw_networkx_edge_labels.

    Bilan Épidémique : Génération d'un graphique final (courbes de survie) pour analyser l'évolution des trois populations (S, I, R) au fil du temps.

3. Programmation Python

    Compréhensions de listes : Optimisation du comptage des états et de la génération des listes de couleurs.

    F-strings : Formatage dynamique des titres et des rapports de simulation dans la console.

    Dictionnaires : Stockage efficace des états de santé pour chaque sommet.
