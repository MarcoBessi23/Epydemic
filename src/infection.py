import networkx as nx
import numpy as np
import random as rd

from matplotlib import pyplot as plt

from src.plot import plot_update
from src.utils import *


def critical_j(k: int, t: float) -> float:
    """
    Compute the critical J value

    :param k: degree
    :param t: bare infection probability
    :return: return the critical J value
    """
    return k * np.log(k * t)


def init_infected(G: nx.Graph, n: int = 1) -> None:
    """
    Initialize the graph G with n infected nodes

    :param G: graph
    :param n: number of infected nodes, default 10
    """
    infected_nodes = rd.sample(range(G.number_of_nodes()), n)
    for node in G.nodes:
        if node in infected_nodes:
            G.nodes[node][state] = infected
        else:
            G.nodes[node][state] = healthy


def get_infected(G: nx.Graph) -> int:
    """
    Count the number of infected nodes in a graph G

    :param G:
    :return: return the number of infected nodes
    """
    n = 0
    for node in G.nodes:
        if G.nodes[node][state] == infected:
            n += 1
    return n


def get_infected_neighbors(G: nx.Graph, node: int) -> int:
    """
    Count the number of infected neighbors of a node in the graph G

    :param G: graph
    :param node: list of neighbors
    :return: return the number of infected neighbors
    """
    n = 0
    for node in G.neighbors(node):
        if G.nodes[node][state] == infected:
            n += 1
    return n


def update_risk(G: nx.Graph, J: float, t: float) -> None:
    """
    Function to evaluate the risk perception of each node in the graph G

    :param G: graph
    :param J: perception risk
    :param t: bare infection probability
    """
    for node in G.nodes:
        k = G.degree(node)
        s = get_infected_neighbors(G, node)
        G.nodes[node][risk] = infected_prob(s, k, t, J)


def infected_prob(s: int, k: int, t: float, J: float) -> float:
    """
    Compute the probability of being infected

    :param s: number of infected neighbors
    :param k: degree of the node
    :param t: bare infection probability
    :param J: perception risk
    :return: return the probability of being infected
    """
    return t * np.exp(-J * s / k)


def new_infected(G: nx.Graph) -> nx.Graph:
    """
    Propagate the disease in the graph G with infected probability

    :param G: graph
    :return: return the propagated graph
    """
    next_graph = G.copy()
    for node in G.nodes:
        u = G.nodes[node][risk]
        r = np.random.uniform(0, 1)
        if r < u and G.nodes[node][state] == healthy:
            next_graph.nodes[node][state] = infected
    return next_graph


def change_state(G: nx.Graph, rec_prob: float, new_state: str) -> nx.Graph:
    """
    Change the state of all nodes in the graph G

    :param G: graph
    :param rec_prob: recovery probability
    :param new_state: new state
    :return: return the graph with the changed state
    """
    next_graph = G.copy()
    for node in G.nodes:
        r = np.random.uniform(0, 1)
        if G.nodes[node][state] == infected and r < rec_prob:
            next_graph.nodes[node][state] = new_state
    return next_graph


def get_information_graph(PG: nx.Graph, VG: nx.Graph, q: float) -> nx.Graph:
    """
    Create the information graph from the two graphs Physical and Virtual graph

    :param PG: Physical graph
    :param VG: Virtual graph
    :param q: q value
    :return: return the information graph
    """
    IG = nx.Graph()
    IG.add_nodes_from(PG.nodes())

    for node in PG.nodes():
        for neighbor in PG.neighbors(node):
            r = np.random.uniform(0, 1)
            if r < (1 - q):
                IG.add_edge(node, neighbor)

    for node in VG.nodes():
        for neighbor in VG.neighbors(node):
            r = np.random.uniform(0, 1)
            if r < q:
                IG.add_edge(node, neighbor)

    return IG


def infection(G: nx.Graph,
              J: float,
              t: float,
              rec_prob: float,
              iteration: int = 50,
              infected_nodes: int = 1,
              immunity: str = healthy,
              plot: bool = False,
              ) -> int:
    """
    Propagate the disease in the graph G

    :param G: graph
    :param J: perception risk
    :param t: bare infection probability
    :param rec_prob: prob of recovering at each step
    :param iteration: number of iterations, default 10
    :param infected_nodes: number of infected nodes, default 2
    :param immunity: recovered if immunity is possible
    :param plot: if the graph should be plotted
    :return: return the number of infected nodes
    """
    init_infected(G, infected_nodes)

    pos = nx.spring_layout(G)
    plt.figure()

    for i in range(iteration):
        if plot:
            plot_update(G, pos)
        update_risk(G, J, t)
        G = new_infected(G)
        G = change_state(G, rec_prob, immunity)
        print(f"Step: {i + 1}, Infected: {get_infected(G)}")
        print(G.nodes.data())
        print("\n")

    return get_infected(G)
