import networkx as nx
import numpy as np
import random as rd

from matplotlib import pyplot as plt

from src.plot import plot_update
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


def simple_tau_percolation(G: nx.Graph, iterations: int):
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
    tau = np.zeros(nx.number_of_nodes(G))

    # Iterate T times to update tau values
    for _ in range(iterations):
        # Create a copy of tau to avoid overwriting values during iteration
        ct = tau.copy()

        # Iterate over each node in the graph
        for i in range(len(tau)):
            max_values = []

            # Iterate over neighbors of the node
            for j in G.neighbors(i):
                r = np.random.uniform(0, 1)
                max_values.append(max(r, ct[j]))

            # Update tau[i] using the minimum of max_values
            if max_values:
                tau[i] = min(max_values)

    return tau


def critic_j_percolation(J: list, G: nx.Graph, tau: float, T: int):
    """
    Calculate the critical J values for percolation.

    I aim to determine the parameter J for which there is no long-term infection spread.
    [J < −(k/s) ln(r/τ)] is the condition for a node to become infected.
    In the function, I extract r and check if it equals 1. J[i] is the minimum value of J that causes node i to become infected.
    Skipping the calculations, I directly move to formula (15), which is the one I want to implement.
    Ji (t + 1) = max min (Jj(t), (ki/si[Jj(t)]) * ln(rij(t)/τ)). si[J] is a function that sums [Jj(t) >= J] for all neighbors.

    :param J: Initial J values for each node
    :param G: NetworkX graph
    :param tau: Infection probability
    :param T: Number of iterations
    :return: Updated critical J values
    """

    for t in range(T):
        j_copy = [G.nodes[node][j_value] for node in G.nodes()]

        for i in G.nodes():
            m = []
            k = G.degree(i)
            for j in G.neighbors(i):
                s = sum(1 for neighbor in G.neighbors(i) if
                        G.nodes[neighbor][j_value] > G.nodes[neighbor][j_value])  # Calculate sum term
                r = np.random.uniform(0, 1)
                m.append(min(j_copy[j], (k / s) * np.log(r / tau)))  # Calculate min max term
            G.nodes[i][j_value] = max(m)  # Update J with the maximum value calculated
    return [G.nodes[node][j_value] for node in G.nodes()]

                

                





