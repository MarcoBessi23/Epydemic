import networkx as nx
import numpy as np

from src.config import zero_threshold
from src.infection import get_average_graph_degree, simulated_j_percolation, simulated_approx_j_percolation
from src.plot import plot_critical_j
from src.utils import infected, state, healthy, t_test, j_test, j_pred, not_approx_jc_plot, approx_plot_jc_plot


def not_approx_critical_j_test(G: nx.Graph, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
    :param T: iteration
    :param ts: values of tau
    :param js: values of risk perception J
    :return: return the critical J values
    """

    # Calculate the average degree of the graph
    k = get_average_graph_degree(G)

    results = {t_test: [], j_test: [], j_pred: []}
    for t in reversed(ts):
        # Calculate the critical J prediction from the mean field approximation
        jc_pred = k * np.log(k * t)
        print(f"Critical J prediction: {jc_pred}")
        for j in js:
            print(f"t: {round(t,2)}, j: {round(j,2)}")
            v = simulated_j_percolation(G.copy(), t, j, T)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=not_approx_jc_plot)


def approx_critical_j_test(G: nx.Graph, T: int, ts: np.array, js: np.array):
    """
    Get the critical J values test

    :param G: graph
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
            v = simulated_approx_j_percolation(G.copy(), t, j, T)
            if v <= zero_threshold:
                results[t_test].append(t)
                results[j_test].append(j)
                results[j_pred].append(jc_pred if jc_pred > 0 else 0)
                break
        print("--------------------------------------------------", end="\n\n")
    plot_critical_j(results, file=approx_plot_jc_plot)


def multiplex_percolation_critical_j_test(IG: nx.DiGraph, PG: nx.Graph, T: int, ts: np.array, js: np.array, qs: np.array):
    """
    Get the critical J values test

    :param IG: Information graph
    :param PG: Physical graph
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
            jc_pred = multiplex_percolation(IG, PG, t, T)
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


def simulated_multiplex(PG: nx.Graph,
                        VG: nx.Graph,
                        q: float,
                        tau: float,
                        J: float,
                        T: int) -> float:
    """
    Simulated J percolation

    :param PG: graph just infected
    :param VG: virtual graph
    :param q: connection probability for the information graph
    :param tau: bare infection probability
    :param J: risk perception
    :param T: number of iterations
    :return: return the percentage of infected nodes
    """
    IG = get_information_graph(PG, VG, q)
    for _ in range(T):
        cIG = IG.copy
        for node in PG.nodes:
            k = PG.degree(node)
            s = get_infected_neighbors(cIG, node)  # quenched version @TODO: implementation of the annealed version
            r = np.random.uniform(0, 1)
            psk = 1 - pow(1-infected_prob(s, k, tau, J), s)
            if r < psk:
                PG.nodes[node][state] = infected
                IG.nodes[node][state] = infected
            else:
                PG.nodes[node][state], IG.nodes[node][state] = healthy
    return get_infected(PG) / PG.number_of_nodes()


def critical_j_test():
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=False)
