import networkx as nx
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import tqdm
from matplotlib.animation import FuncAnimation

state = "state"
infected = "infected"
healty = "healty"

def insert_infected(PG, init_infected):
    selected_nodes = rd.sample(list(PG.nodes), 20)

    for node in PG.nodes:
        PG.nodes[node][state] = healty

    for node in selected_nodes:
        PG.nodes[node][state] = infected


def update_graph(PG, init_infected, J, t):
    insert_infected(PG, init_infected)
    next_graph = PG
    for node in PG.nodes:
        neighbors = PG.nodes[node].neighbors
        k = PG.nodes[node].degree
        s = 0
        for i in neighbors:
            if i[state] == infected:
                s = s + 1
        u = infected_prob(s, k, t, J)
        r = rd.choice([0, 1], weights=[1-u, u])#Forse più semplice np.random.uniform(0,1)
        if r == 1:                             #r<u
            next_graph.nodes[node][state] = infected
    PG = next_graph

def infected_prob(s, k, t, J):
    return t*np.exp(-J*s/k)


def information_graphs(PG, VG, q=0.5):
    AP = nx.adjacency_matrix(PG)
    AG = nx.adjacency_matrix(VG)
    AI = np.matrix()
    for x, y in AP:
        r = np.random.uniform(0,1) # BINOMIAL
        if r < q:
            AI[x, y] = AG[x, y]
        else:
            AI[x, y] = AP[x, y]
    IG = nx.from_numpy_matrix(AI)
    return IG


def main():
    nodes = 20
    m = 2 # Connective nodes
    q = 0.6
    init_infectes = 2
    PG = nx.cycle_graph(nodes, m)
    VG = nx.cycle_graph(nodes, m)
    IG = information_graphs(PG, VG, q)

    m = 5
    PG = nx.scale_free_graph(nodes, m)
    VG = nx.scale_free_graph(nodes, m)


if __name__ =="__main__":
    main()
