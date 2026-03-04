Explication de mon projet

Mon projet consiste à simuler la propagation d’une épidémie en utilisant la théorie des graphes.

Je représente un groupe de personnes sous forme de graphe :

Chaque sommet représente une personne.

Chaque arête représente un contact entre deux personnes.

J’utilise un graphe non orienté, car si une personne est en contact avec une autre, la relation fonctionne dans les deux sens.

Les arêtes sont pondérées : le poids représente la probabilité que la maladie se transmette entre deux personnes.

Au début, je choisis une personne infectée (le patient zéro).
Ensuite, à chaque étape, une personne infectée peut contaminer ses voisins selon la probabilité indiquée par le poids de l’arête.

Le programme permet de visualiser comment l’épidémie se propage dans le réseau.

Ce que j’ai utilisé du cours
 
 La définition d’un graphe:

J’utilise la définition vue en cours :
un graphe est composé de sommets et d’arêtes.

Graphe non orienté:

Dans le diapo, on a vu qu’un graphe peut être orienté ou non orienté.
J’ai choisi un graphe non orienté car les contacts sont réciproques.

 Graphe pondéré:

J’utilise un graphe pondéré.
Le poids des arêtes représente la probabilité de transmission de la maladie.
C’est une application directe de la notion de graphe pondéré vue en cours.

 Voisins d’un sommet:

En cours, on a vu que les voisins d’un sommet sont les sommets reliés par une arête.
Dans mon projet, une personne peut contaminer uniquement ses voisins.
J’utilise donc directement cette notion.

 Connexité:

On a vu qu’un graphe est connexe si on peut aller de n’importe quel sommet à n’importe quel autre.
Dans mon projet :
si le graphe est connexe, l’épidémie peut toucher tout le monde.
sinon, elle reste limitée à une partie du réseau.

Parcours de graphe:

La propagation fonctionne comme un parcours du graphe :
je pars d’un sommet infecté, puis je regarde ses voisins, puis les voisins des voisins.
C’est comme le  parcours en largeur vu en cours.
