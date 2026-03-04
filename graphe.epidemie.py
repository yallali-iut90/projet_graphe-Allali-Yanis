import networkx as nx
import matplotlib.pyplot as plt
import random


NB_PERSONNES = 16
NB_ETAPES = 10
PROBA_CONNEXION = 0.2      
PROBA_GUERISON = 0.25       
PROBA_REINFECTION = 0.05   

#  graphe
G = nx.Graph()
personnes = [chr(i) for i in range(65, 65 + NB_PERSONNES)]
G.add_nodes_from(personnes)

for i in range(len(personnes)):
    for j in range(i + 1, len(personnes)):
        if random.random() < PROBA_CONNEXION:
            G.add_edge(personnes[i], personnes[j], weight=round(random.uniform(0.1, 0.8), 2))

# etats de basse 
etat = {p: "S" for p in G.nodes()}
etat[random.choice(personnes)] = "I"

# propa
def propagation(G, etat):
    nouvel_etat = etat.copy()
    for personne in G.nodes():
        if etat[personne] == "I":
            for voisin in G.neighbors(personne):
                if etat[voisin] == "S":
                    if random.random() < G[personne][voisin]["weight"]:
                        nouvel_etat[voisin] = "I"
            if random.random() < PROBA_GUERISON:
                nouvel_etat[personne] = "R"
        elif etat[personne] == "R":
 
            if random.random() < PROBA_REINFECTION:
                nouvel_etat[personne] = "I"
    return nouvel_etat

# Affichage 
def afficher_graphe(G, etat, etape):
    couleurs = []
    tailles = []
    for p in G.nodes():
        if etat[p] == "I":
            couleurs.append("red")
            tailles.append(1000)   
        elif etat[p] == "R":
            couleurs.append("steelblue")
            tailles.append(700)
        else:
            couleurs.append("limegreen")
            tailles.append(700)

    nb_sains    = sum(1 for e in etat.values() if e == "S")
    nb_infectes = sum(1 for e in etat.values() if e == "I")
    nb_gueris   = sum(1 for e in etat.values() if e == "R")

    pos = nx.spring_layout(G, k=1.5, seed=etape)
    plt.figure(figsize=(10, 7))
    plt.title(
        f"Jour {etape + 1}  —  Sains: {nb_sains}   Infectés: {nb_infectes}   Guéris: {nb_gueris}",
        fontsize=13, fontweight='bold'
    )

    nx.draw(G, pos, with_labels=True, node_color=couleurs, node_size=tailles,
            font_size=10, font_weight='bold', edge_color='gray', width=1.2)

    plt.tight_layout()
    plt.show()

# simu 
for t in range(NB_ETAPES):
    nb_i = sum(1 for e in etat.values() if e == "I")
    print(f"Jour {t+1} : {nb_i} infecté")
    afficher_graphe(G, etat, t)
    etat = propagation(G, etat)

    # si plus de infecte 
    if nb_i == 0:
        print("L'épidémie est terminée !")
        break