import networkx as nx
import numpy as np

from src.infection import init_infected


def cycle_graph_test(nodes: int = 20, q: float = 0.5, infected: int = 3):
    """
    Test the cycle graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.cycle_graph(nodes)
    init_infected(PG, infected)
    VG = nx.cycle_graph(nodes)
    IG = get_information_graph(PG, VG, q)
    return PG, VG, IG


def scale_free_graph_test(nodes: int = 5, m: int = 3, q: float = 0.5, infected: int = 2):
    """
    Test the scale free graph

    :param nodes:
    :param m:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.barabasi_albert_graph(nodes, m)
    init_infected(PG, infected)
    VG = nx.barabasi_albert_graph(nodes, m)
    IG = get_information_graph(PG, VG, q)
    return PG, VG, IG


def random_graph_test(nodes: int = 10, p: float = 0.4, q: float = 0.5, infected: int = 2):
    """
    Test the random graph

    :param nodes:
    :param p:
    :param q:
    :param infected:
    :return:
    """
    PG = nx.gnp_random_graph(nodes, p)
    init_infected(PG, infected)
    VG = nx.gnp_random_graph(nodes, p)
    IG = get_information_graph(PG, VG, q)
    return PG, VG, IG


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
