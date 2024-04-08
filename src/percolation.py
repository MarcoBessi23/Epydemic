import networkx as nx
import numpy as np

from src.utils import *


# TODO Fare test per tipo di grafo, media dei tau, plottare distribuzione dei tau
def simple_tau_percolation(G: nx.Graph, iterations: int) -> float:
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
            m = [1]
            # Iterate over neighbors of the node
            for j in G.neighbors(i):
                r = np.random.uniform(0, 1)
                m.append(max(r, ct[j]))
            # Update tau[i] using the minimum of max_values
            tau[i] = min(m)
            # return the critical tau(min of tau)
    return min(tau.values())


# TODO Fare test per tipo di grafo, per tipo di j iniziale, per tipo di tau, media e distribuzione di j
def critic_j_percolation(G: nx.Graph, tau: float, T: int) -> float:
    """
    Calculate the critical J values for percolation.

    I aim to determine the parameter J for which there is no long-term infection spread.
    [J < -(k/s) ln(r/τ)] is the condition for a node to become infected.
    In the function, I extract r and check if it equals 1.
    J[i] is the minimum value of J that causes node i to become infected.
    Skipping the calculations, I directly move to formula (15), which is the one I want to implement.
    Ji (t + 1) = max min (Jj(t), (-ki/si[Jj(t)]) * ln(rij(t)/τ)).
    si[J] is a function that sums [Jj(t) >= J] for all neighbors.

    :param G: NetworkX graph
    :param tau: Infection probability
    :param T: Number of iterations
    :return: Updated critical J values
    """

    # Initialize J values for each node
    for node in G.nodes():
        G.nodes[node][j_value] = np.random.uniform(0, 1)

    for _ in range(T):
        cG = G.copy()
        for i in G.nodes():
            m = [0]
            k = G.degree(i)
            for j in G.neighbors(i):
                # Calculate sum term
                s = sum(1 for n in G.neighbors(i) if cG.nodes[n][j_value] >= cG.nodes[j][j_value])
                r = np.random.uniform(0, 1)
                # Calculate min max term
                m.append(min(cG.nodes[j][j_value], (-(k / s) * np.log(r / tau))))
            # Update J with the maximum value calculated
            G.nodes[i][j_value] = max(m)
    return max(G.nodes[node][j_value] for node in G.nodes())


# TODO Fare test per tipo di grafo, per tipo di j iniziale, per tipo di tau, e per q, media e distribuzione di j
def multiplex_percolation(IG: nx.DiGraph, PG: nx.graph, tau: float, T: int) -> float:
    """
    Multiplex percolation model

    :param IG:
    :param PG:
    :param tau:
    :param T:
    :return:
    """
    # Initialize J values for each node
    for node in PG.nodes():
        PG.nodes[node][j_value] = np.random.uniform(0, 1)

    for _ in range(T):
        cPG = PG.copy()
        for i in PG.nodes():
            m = [0]
            k = PG.degree(i)  # Calculate the degree of node i
            for j in PG.neighbors(i):  # Iterate over neighbors of node i in PG
                # Count neighbors with J greater than J[j]
                si = sum(1 for n in IG.successors(i) if cPG.nodes[n][j_value] >= cPG.nodes[j][j_value]) + 1e-8
                # Calculate min max term
                r = np.random.uniform(0, 1)
                m.append(min(cPG.nodes[j][j_value], (-(k / si) * np.log(r / tau))))
            PG.nodes[i][j_value] = max(m)  # Update J[i] with the maximum value calculated
    return max(PG.nodes[node][j_value] for node in PG.nodes())
