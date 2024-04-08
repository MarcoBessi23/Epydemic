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
        for node in G.nodes():
            # Generate random numbers for all neighbors at once
            r = [random.random() for _ in G.neighbors(node)]
            # Get tau values for all neighbors
            tau_neighbors = [ct[j] for j in G.neighbors(node)]
            # Calculate max values for all neighbors
            max_values = np.maximum(r, tau_neighbors)
            # Update tau[node] using the minimum of max_values
            tau[node] = np.min(np.append(1, max_values))  # append 1 to max_values before finding the min
    return min(tau.values())



