import networkx as nx
import matplotlib.pyplot as plt
import random

# =========================
# 1️⃣ Création du graphe
# =========================

G = nx.Graph()  # graphe non orienté

# =========================
# 2️⃣ Ajout des sommets
# =========================

personnes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(personnes)

# =========================
# 3️⃣ Ajout des arêtes (contacts) avec poids
# poids = probabilité de transmission
# =========================

G.add_edge("A", "B", weight=0.6)
G.add_edge("A", "C", weight=0.4)
G.add_edge("B", "D", weight=0.5)
G.add_edge("C", "D", weight=0.3)
G.add_edge("D", "E", weight=0.7)

# =========================
# 4️⃣ État des personnes
# S = sain, I = infecté
# =========================

etat = {p: "S" for p in G.nodes()}
etat["A"] = "I"  # patient zéro

# =========================
# 5️⃣ Fonction de propagation
# =========================

def propagation(G, etat):
    nouvel_etat = etat.copy()

    for personne in G.nodes():
        if etat[personne] == "I":
            for voisin in G.neighbors(personne):
                if etat[voisin] == "S":
                    proba = G[personne][voisin]["weight"]
                    if random.random() < proba:
                        nouvel_etat[voisin] = "I"

    return nouvel_etat

# =========================
# 6️⃣ Affichage du graphe
# =========================

def afficher_graphe(G, etat, etape):
    couleurs = []
    for p in G.nodes():
        if etat[p] == "I":
            couleurs.append("red")
        else:
            couleurs.append("green")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=couleurs, node_size=1200)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f"Étape {etape}")
    plt.show()

# =========================
# 7️⃣ Simulation
# =========================

nb_etapes = 5

for t in range(nb_etapes):
    print(f"jour {t} :", etat)
    afficher_graphe(G, etat, t)
    etat = propagation(G, etat)
