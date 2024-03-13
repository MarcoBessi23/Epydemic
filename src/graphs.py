import networkx as nx
from src.infection import init_infected, get_information_graph


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


def random_graph_test(nodes: int = 10, p: int = 0.4, q: float = 0.5, infected: int = 2):
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
