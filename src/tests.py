import numpy as np
import networkx as nx

from src.config import zero_threshold
from src.graphs import get_information_graph
from src.infection import get_average_graph_degree, simulated_mean_field_infection, \
    simulated_tau_percolation, simulated_j_percolation
from src.plot import plot_critical_j, plot_critical_t, plot_q_value
from src.percolation import critic_j_percolation, simple_tau_percolation, multiplex_percolation
from src.utils import *


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
    k = get_average_graph_degree(G)

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


def simple_tau_perc_test(G: nx.Graph, T: int, ts: np.array):
    """
    Get the value of tau_critical
    :param G: graph
    :param T: iteration
    :param ts: values of tau
    :return: return the critical tau values
    """
    results = {t_test: [], t_pred: []}
    tc_pred = simple_tau_percolation(G.copy(), iterations=T)
    print(f"Critical tau prediction: {tc_pred}")
    for t in reversed(ts):
        print(f"t: {round(t,2)}")
        v = simulated_tau_percolation(G.copy(), T, tau=t)
        print(f"Valore di c: {v}")
        if v <= zero_threshold:
            results[t_test].append(t)
            results[t_pred].append(tc_pred)
            break
    print("--------------------------------------------------", end="\n\n")
    plot_critical_t(results, file=critical_t_plot)


def percolation_critical_j_test(G: nx.Graph, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :return: return the critical J values
    """

    results = {t_test: [], j_test: [], j_pred: []}
    for t in reversed(ts):
        # Calculate the jc prediction about percolation
        jc_pred = critic_j_percolation(G, t, T)
        print(f"Critical J prediction: {jc_pred}")
        for j in js:
            print(f"t: {round(t,2)}, j: {round(j,2)}")
            # Simulate the infection with the percolation scenario
            v = simulated_j_percolation(G.copy(), t, j, T)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=approx_plot_jc_plot)


def multiplex_percolation_critical_j_test(PG: nx.Graph, VG: nx.Graph, T: int, ts: np.array, js: np.array, qs: np.array):
    """
    Get the critical J values test

    :param PG: Physical graph
    :param VG: Virtual graph
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :param qs: values of q
    :return: return the critical J values
    """
    results = {q_test: [], t_test: [], j_test: [], j_pred: []}
    for q in qs:
        for t in reversed(ts):
            # Calculate the jc prediction about percolation
            jc_pred = multiplex_percolation(PG, VG, t, T, q)
            print(f"Critical J prediction: {jc_pred}")
            for j in js:
                print(f"t: {round(t,2)}, j: {round(j,2)}")
                # Simulate the infection with the percolation scenario
                v = simulated_j_percolation(PG.copy(), t, j, T)
                if v <= zero_threshold:
                    results[q_test].append(q)
                    results[t_test].append(t)
                    results[j_test].append(j)
                    results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                    break
            print("--------------------------------------------------", end="\n\n")


def multiplex_percolation_critical_j_test_test(PG: nx.Graph, VG: nx.Graph, T: int, ts: np.array, qs: np.array):
    """
    Get the critical J values test

    :param PG: Physical graph
    :param VG: Virtual graph
    :param T: iteration
    :param ts: values of tau
    :param qs: values of q
    :return: return the critical J values
    """
    results = {q_test: [], t_test: [], j_pred: []}
    for q in qs:
        for t in reversed(ts):
            # Calculate the jc prediction about percolation
            jc_pred = multiplex_percolation(PG, VG, t, T, q)
            results[q_test].append(q)
            results[t_test].append(t)
            results[j_pred].append(jc_pred if jc_pred > 0 else 0)
            print(f"q: {round(q, 2)}, t: {round(t, 2)}, jc: {round(jc_pred, 2)}")
        print("--------------------------------------------------", end="\n\n")
    plot_q_value(results, file=q_plot)
