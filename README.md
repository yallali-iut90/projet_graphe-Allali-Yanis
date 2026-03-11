DESCRIPTION DU PROJET

Ce projet simule la propagation d'une épidémie au sein d'une population de 16 personnes, modélisée par un graphe non orienté pondéré. L'objectif est de visualiser l'impact des interactions sociales et de la mobilité sur la diffusion d'un virus.

La simulation repose sur une population où chaque individu est un nœud et chaque connexion sociale est une arête. Le poids de chaque arête représente la probabilité de transmission (de 0.1 à 0.9).
FONCTIONNEMENT DE LA SIMULATION

La simulation se déroule sur 10 jours. À chaque étape :

    Contamination : les infectés peuvent transmettre le virus à leurs voisins selon le poids de l'arête.

    Guérison : les malades ont une chance de guérir et de devenir immunisés.

    Réinfection : une petite probabilité permet aux guéris de redevenir infectieux.

    Mouvement : les positions des nœuds sont recalculées pour simuler des déplacements

    Confinement : le sommet L est volontairement isolé (degré 0) pour tester l'efficacité d'une coupure totale de liens sociaux.

ETATS DES INDIVIDUS

SAIN (VERT) : Individu n'ayant pas encore contracté le virus.

INFECTE (ROUGE) : Individu malade, entouré d'un halo de contamination.

GUERI (BLEU) : Individu immunisé après avoir contracté la maladie.

NOTIONS DU COURS APPLIQUEES
THEORIE DES GRAPHES (NETWORKX)

    Graphe pondéré : attribution de poids sur les arêtes pour modéliser des probabilités de transmission.

    Mesures de centralité : la taille des nœuds est liée à leur degré (nombre de voisins) pour identifier les individus les plus connectés.

    Sommets isolés : suppression d'arêtes pour créer un nœud de degré 0 (cas de l'individu L).

    Layouts : utilisation du spring_layout avec une modification de la seed à chaque étape pour générer du mouvement.

ANALYSE DE DONNEES (MATPLOTLIB)

    Visualisation : affichage des probabilités sur les arêtes via draw_networkx_edge_labels.

    Bilan épidémique : génération d'un graphique final pour analyser l'évolution des trois populations au fil du temps.

PROGRAMMATION PYTHON

    Compréhensions de listes : optimisation du comptage des états et de la génération des listes de couleurs.

    F-strings : formatage dynamique des titres et des rapports de simulation.

    Dictionnaires : stockage des états de santé pour chaque sommet.
