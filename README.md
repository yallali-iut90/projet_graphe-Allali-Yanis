
Description du projet

Ce projet simule la propagation d'une épidémie dans une population de 16 personnes , modélisée sous forme de graphe non orienté pondéré.
Chaque personne est un nœud, et chaque connexion entre deux personnes est une arête dont le poids représente la probabilité de transmission de la maladie entre elles.

La simulation est sur plusieurs jours. À chaque jour :
les personnes infectées peuvent contaminer leurs voisins 
les personnes infectées ont une chance de guérir
les personnes guéries ont une petite chance de retomber malades
Les nœuds bougent à chaque étape pour simuler le mouvement des personnes dans la population.

## États possibles

Vert (S) – Sain : n’a pas été infecté.

Rouge (I) – Infecté : est malade et peut transmettre la maladie.

Bleu (R) – Guéri : a été malade et est maintenant immunisé.

## Ce que j'ai utilisé du cours

### Graphes (networkx)

- **Graphe non orienté simple** (`nx.Graph()`) .
- **Voisins d'un nœud** : `G.neighbors(personne)` utilisé dans la propagation pour parcourir les contacts directs d'une personne infectée .
- **Coloration des nœuds** : `node_color` dans `nx.draw()`.
- **Layout spring** : `nx.spring_layout(G, k=1.5, seed=etape)` . Le paramètre `seed` change à chaque jour pour simuler le mouvement des personnes.
- **Paramétrage de l'affichage** : `node_size`, `edge_color`, `font_weight` .

### Python général

- **Compréhension de liste** : utilisée pour compter les sains/infectés/guéris .
- **f-strings** : pour afficher le titre du graphe et les messages dans le terminal.
- **Dictionnaire** : `etat` est un dictionnaire `{personne: état}`.
