import networkx as nx
import numpy as np

from src.infection import get_information_graph
from src.utils import *


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


# TODO Fare test per tipo di grafo, media dei tau, plottare distribuzione dei tau
def simple_tau_percolation(G: nx.Graph, iterations: int) -> dict:
    """
    Update the values of tau parameters associated with the nodes in graph G based on simple percolation.

    taui[t+1] = min max(rij(t), taui(t)) calculated for each neighbor of node i

    This formula updates the value tau[i] as indicated in the simple percolation section.
    Tau is a vector such that the i-th component of tau corresponds to the tau value for node i.
    We start from the scenario where all nodes are infected, so tau is a vector of zeros.
    I copy the tau vector into a vector ctau to avoid overwriting the value of tau at each iteration of the min max.
    The nonzero function returns indices corresponding to the neighbors of node i.
    M is the vector of max values from which I extract the minimum.

    :param G: NetworkX graph
    :param iterations: Number of iterations
    :return: Updated tau values for each node
    """
    # Initialize tau values for each node
    tau = {node: 0.0 for node in G.nodes()}

    for _ in range(iterations):
        ct = tau.copy()
        # Iterate over each node in the graph
        for i in G.nodes():
            m = []
            # Iterate over neighbors of the node
            for j in G.neighbors(i):
                r = np.random.uniform(0, 1)
                m.append(max(r, ct[j]))
            # Update tau[i] using the minimum of max_values
            tau[i] = min(m)
    return tau


# TODO Fare test per tipo di grafo, per tipo di j iniziale, per tipo di tau, media e distribuzione di j
def critic_j_percolation(init_j: list, G: nx.Graph, tau: float, T: int) -> dict:
    """
    Calculate the critical J values for percolation.

    I aim to determine the parameter J for which there is no long-term infection spread.
    [J < −(k/s) ln(r/τ)] is the condition for a node to become infected.
    In the function, I extract r and check if it equals 1.
    J[i] is the minimum value of J that causes node i to become infected.
    Skipping the calculations, I directly move to formula (15), which is the one I want to implement.
    Ji (t + 1) = max min (Jj(t), (ki/si[Jj(t)]) * ln(rij(t)/τ)).
    si[J] is a function that sums [Jj(t) >= J] for all neighbors.

    :param init_j: Initial J values
    :param G: NetworkX graph
    :param tau: Infection probability
    :param T: Number of iterations
    :return: Updated critical J values
    """

    # Initialize J values for each node
    js = {node: init_j[i] for i, node in enumerate(G.nodes())}

    for _ in range(T):
        for i in G.nodes():
            m = []
            k = G.degree(i)
            for j in G.neighbors(i):
                # Calculate sum term
                s = sum(1 for k in G.neighbors(i) if js[k] > js[j])
                r = np.random.uniform(0, 1)
                # Calculate min max term
                m.append(min(js[j], (k / s) * np.log(r / tau)))
            # Update J with the maximum value calculated
            G[i][j_value] = max(m)
        js = {node: G.nodes[node][j_value] for node in G.nodes()}
    return js


# TODO Fare test per tipo di grafo, per tipo di j iniziale, per tipo di tau, e per q, media e distribuzione di j
def multiplex_percolation(init_j: list, tau: float, T: int, PG: nx.Graph, VG: nx.Graph, q: float):
    """
    Multiplex percolation model

    :param init_j:
    :param tau:
    :param T:
    :param PG:
    :param VG:
    :param q:
    :return:
    """
    IG = get_information_graph(PG, VG, q)

    # Initialize J values for each node
    js = {node: init_j[i] for i, node in enumerate(IG.nodes())}

    for _ in range(T):

        for i in IG.nodes():
            m = []
            k = IG.degree(i)  # Calculate the degree of node i

            for j in IG.neighbors(i):  # Iterate over neighbors of node i
                # Count neighbors with J greater than J[j]
                s = sum(1 for k in IG.neighbors(i) if js[k] > js[j])

                # Calculate min max term
                r = np.random.uniform(0, 1)
                m.append(min(js[j], (k / s) * np.log(r / tau)))
            IG[i][j_value] = max(m)  # Update J[i] with the maximum value calculated

        js = {node: IG.nodes[node][j_value] for node in IG.nodes()}
    return js



