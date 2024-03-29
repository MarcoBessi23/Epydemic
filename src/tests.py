import numpy as np
import networkx as nx
from src.infection import infection
from src.percolation import simple_percolation
from src.utils import *


def critical_j_test(G: nx.graph,
                    ts: np.array,
                    js: np.array,
                    rec_prob: float = 0.2,
                    immunity: str = healthy,
                    plot: bool = False) -> dict:
    """
    Get the critical J values test

    :param G: graph
    :param ts: values of tau
    :param js: values of risk perception J
    :param rec_prob: recovery probability
    :param immunity: if the nodes have immunity
    :param plot: if the graph should be displayed
    :return: return the critical J values
    """
    t_crit = []
    j_crit = []
    for t in ts:
        for j in js:
            print(f"t: {t}, j: {j}")
            v = infection(G.copy(), j, t, rec_prob=rec_prob, immunity=immunity, plot=plot)
            if v == 0:
                t_crit.append(t)
                j_crit.append(j)
                break
    return {t_test: t_crit, j_test: j_crit}


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

