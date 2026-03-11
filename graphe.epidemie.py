import networkx as nx
import matplotlib.pyplot as plt
import random


NB_PERSONNES = 16
NB_ETAPES = 10  
PROBA_CONNEXION = 0.25      
PROBA_GUERISON = 0.20       
PROBA_REINFECTION = 0.05   

stats_s, stats_i, stats_r = [], [], []


G = nx.Graph()
sommets = [chr(i) for i in range(65, 65 + NB_PERSONNES)]
G.add_nodes_from(sommets)

for i in range(len(sommets)):
    for j in range(i + 1, len(sommets)):
        if random.random() < PROBA_CONNEXION:
            poids = round(random.uniform(0.1, 0.9), 2)
            G.add_edge(sommets[i], sommets[j], weight=poids)


if 'L' in G:
    aretes_a_retirer = list(G.edges('L'))
    G.remove_edges_from(aretes_a_retirer)
    print(" Le sommet L a été isolé (confinement total !)")


etat = {p: "S" for p in G.nodes()}

possible_zeros = [s for s in sommets if s != 'L']
etat[random.choice(possible_zeros)] = "I"


def propagation(G, etat_actuel):
    nouvel_etat = etat_actuel.copy()
    rapports = []
    for personne in G.nodes():
        if etat_actuel[personne] == "I":
            for voisin in G.neighbors(personne):
                if etat_actuel[voisin] == "S":
                    if random.random() < G[personne][voisin]["weight"]:
                        nouvel_etat[voisin] = "I"
                        rapports.append(f" {personne} a contaminé {voisin}")
            if random.random() < PROBA_GUERISON:
                nouvel_etat[personne] = "R"
        elif etat_actuel[personne] == "R" and random.random() < PROBA_REINFECTION:
            nouvel_etat[personne] = "I"
    return nouvel_etat, rapports


def afficher_graphe(G, etat, etape):
    plt.figure(figsize=(12, 7))
    pos = nx.spring_layout(G, k=1.2, seed=etape)
    
    nb_s, nb_i, nb_r = list(etat.values()).count("S"), list(etat.values()).count("I"), list(etat.values()).count("R")
    stats_s.append(nb_s); stats_i.append(nb_i); stats_r.append(nb_r)
    
    couleurs = ["red" if etat[p] == "I" else "steelblue" if etat[p] == "R" else "limegreen" for p in G.nodes()]
    tailles = [400 + (G.degree(p) * 200) for p in G.nodes()]
    largeurs = [G[u][v]['weight'] * 4 for u, v in G.edges()]

    
    infectes = [p for p in G.nodes() if etat[p] == "I"]
    if infectes:
        nx.draw_networkx_nodes(G, pos, nodelist=infectes, node_size=[(G.degree(p)*200)+1000 for p in infectes], 
                               node_color="red", alpha=0.15)

    nx.draw_networkx_edges(G, pos, width=largeurs, edge_color='gray', alpha=0.4)
    nx.draw_networkx_nodes(G, pos, node_color=couleurs, node_size=tailles, edgecolors="white", linewidths=2)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    labels_poids = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_poids, font_size=7)

    plt.title(f"JOUR {etape+1}  —  Sains: {nb_s}  |  Infectés: {nb_i}  |  Guéris: {nb_r}\n(L est isolé)", 
              fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.show()


for t in range(NB_ETAPES):
    nb_i = list(etat.values()).count("I")
    print(f"\n--- JOUR {t+1} ---")
    afficher_graphe(G, etat, t)
    
    if nb_i == 0:
        print("L'épidémie est terminée !")
        break
        
    etat, rapports = propagation(G, etat)
    for r in rapports: print(r)


plt.figure(figsize=(10, 4))
plt.plot(stats_i, label="Infectés", color="red", linewidth=3)
plt.plot(stats_s, label="Sains", color="limegreen", linestyle="--")
plt.plot(stats_r, label="Guéris", color="steelblue", linestyle="--")
plt.title("Évolution sur 10 jours")
plt.legend(); plt.grid(axis='y', alpha=0.3); plt.show()