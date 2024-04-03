import numpy as np
import networkx as nx

from src.config import zero_threshold
from src.infection import infection, simulated_mean_field_infection, simulated_j_percolation, \
    simulated_approx_j_percolation
from src.plot import plot_critical_j
from src.utils import *


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


def mean_field_critical_j_test(G: nx.Graph, c: float, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
    :param c: initial percentage of infected nodes
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :return: return the critical J values
    """

    # Calculate the average degree of the graph
    k = int(sum(d for n, d in G.degree()) / G.number_of_nodes())

    results = {t_test: [], j_test: [], j_pred: []}
    for t in reversed(ts):
        jc_pred = k * np.log(k * t)
        print(f"Critical J prediction: {jc_pred}")
        for j in js:
            print(f"t: {round(t,2)}, j: {round(j,2)}")
            v = simulated_mean_field_infection(k, t, c, T, j)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=mean_field_jc_plot)


def not_approx_critical_j_test(G: nx.Graph, c: float, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
    :param c: initial percentage of infected nodes
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :return: return the critical J values
    """

    # Calculate the average degree of the graph
    k = int(sum(d for n, d in G.degree()) / G.number_of_nodes())

    results = {t_test: [], j_test: [], j_pred: []}
    for t in reversed(ts):
        jc_pred = k * np.log(k * t)
        print(f"Critical J prediction: {jc_pred}")
        for j in js:
            print(f"t: {round(t,2)}, j: {round(j,2)}")
            v = simulated_j_percolation(G.copy(), t, j, c, T)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=not_approx_jc_plot)


def approx_critical_j_test(G: nx.Graph, c: float, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
    :param c: initial percentage of infected nodes
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :return: return the critical J values
    """

    # Calculate the average degree of the graph
    k = int(sum(d for n, d in G.degree()) / G.number_of_nodes())

    results = {t_test: [], j_test: [], j_pred: []}
    for t in reversed(ts):
        jc_pred = k * np.log(k * t)
        print(f"Critical J prediction: {jc_pred}")
        for j in js:
            print(f"t: {round(t,2)}, j: {round(j,2)}")
            v = simulated_approx_j_percolation(G.copy(), t, j, c, T)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=approx_plot_jc_plot)


