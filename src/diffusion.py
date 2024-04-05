import networkx as nx
import numpy as np

from src.infection import infection
from src.plot import plot_critical_j
from src.utils import healthy, t_test, j_test, critical_j_plot


def critical_j_test(G: nx.Graph,
                    ts: np.array,
                    js: np.array,
                    rec_prob: float = 0.2,
                    immunity: str = healthy,
                    plot: bool = False):
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
    results = {t_test: [], j_test: []}
    for t in ts:
        for j in js:
            print(f"t: {t}, j: {j}")
            v = infection(G.copy(), j, t, rec_prob=rec_prob, immunity=immunity, plot=plot)
            if v <= 0:
                results[t_test].append(t)
                results[j_test].append(j)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=critical_j_plot, prediction=False)