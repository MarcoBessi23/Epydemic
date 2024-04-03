import networkx as nx
import numpy as np

from src.utils import infected, state, healthy


def updating_node_percolation(G: nx.Graph, node: int, tau: float):
    """
    Update the state of a node in the graph G
    @TODO funzione per aggiornare lo stato del nodo la uso ad ogni passaggio, deve restituire lo stato

    :param G: graph
    :param node:
    :param tau: bare infection probability
    :return: updated node state
    """
    return infected if any(
        tau > np.random.uniform(0, 1) and G.nodes[n][state] == infected for n in G.neighbors(node)) else healthy


def simple_percolation(G: nx.graph, tau: float, iterations: int):
    """
    Simple percolation model
    @TODO Ho bisogno di copiare il grafo ad ogni passaggio e applicare la funzione di sopra ai nodi del grafi G, non finita

    :param G: graph
    :param tau: bare infection probability
    :param iterations: number of iterations
    :return: return the updated graph
    """
    for _ in range(iterations):
        Gc = G.copy()
        for node in G.nodes:
            G.nodes[node][state] = updating_node_percolation(Gc, node, tau)
    return G


def percolation_test(G: nx.Graph, tau: float, iterations: int = 50):
    """
    Test the percolation
    @TODO da finire

    :param G: graph
    :param tau: bare infection probability
    :param iterations: number of iterations
    :return: return the graph after the percolation
    """
    for _ in range(iterations):
        G = simple_percolation(G, tau, iterations)
    return G
