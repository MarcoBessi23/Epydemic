import networkx as nx
import numpy as np
import random as rd

from matplotlib import pyplot as plt

from src.plot import plot_update
from src.utils import *


# funzione per aggiornare lo stato del nodo la uso ad ogni passaggio, deve restituire lo stato
def updating_node_percolation(G: nx.Graph, node: int, tau: float):
    res=False
    for node in G.neighbors[node]:
        r= np.random.uniform(0, 1)
        res= res or (tau>r and node[state]==infected)
    if res:
        return infected
    else:
        return  healthy

#Ho bisogno di copiare il grafo ad ogni passaggio e applicare la funzione di sopra ai nodi del grafi G, non finita
def simple_percolation(G: nx.graph, tau, iterations):
    
    for t in iterations:
        Support_graph = G.copy()
        for node in G.nodes:
            G.nodes[node][state] = updating_node_percolation(Support_graph,node,tau)


    return G