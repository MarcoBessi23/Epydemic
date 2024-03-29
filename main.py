import numpy as np

from src.graphs import *
from src.plot import plot_all_graphs, plot_graph, plot_critical_j
from src.tests import critical_j_test
from src.utils import *


def main():
    # Values for the tests
    js = np.arange(10000, 100000, 10000)  # Risk perception
    ts = np.arange(0.9, 1, 0.05)  # Tau values
    nodes = 10  # Number of nodes
    immunity = healthy  # Immunity
    rec_prob = 0.1  # Recovery probability
    init_infect = 1  # Initial infected nodes
    m = 4  # Number of edges to attach from a new node

    # Graphs for the tests
    # PG, VG, IG = cycle_graph_test()
    PG, VG, IG = random_graph_test(nodes, p=0.3, infected=init_infect)  # TODO: Check components graphs divided by zero
    # PG, VG, IG = scale_free_graph_test(nodes, m, 0.5, init_infect)
    # plot_all_graphs(PG, 0.2, 0.1)

    # Tests
    critics = critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=True)
    plot_critical_j(critics)


if __name__ == "__main__":
    main()
