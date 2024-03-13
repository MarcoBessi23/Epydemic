import numpy as np

from src.graphs import *
from src.plot import plot_all_graphs, plot_graph, plot_critical_j
from src.tests import critical_j_test
from src.utils import *


def main():
    # Values for the tests
    js = np.arange(0, 10)  # Risk perception
    ts = np.arange(0.5, 1, 0.05)  # Tau values
    nodes = 20  # Number of nodes
    immunity = recovered  # Immunity
    rec_prob = 0.1  # Recovery probability
    init_infect = 2  # Initial infected nodes
    m = 4  # Number of edges to attach from a new node

    # Graphs for the tests
    # PG, VG, IG = cycle_graph_test()
    # PG, VG, IG = random_graph_test() TODO: Check components graphs divided by zero
    PG, VG, IG = scale_free_graph_test(nodes, m, 0.5, init_infect)
    # plot_all_graphs(PG, 0.2, 0.1)

    # Tests
    critics = critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=True)
    plot_critical_j(critics)


if __name__ == "__main__":
    main()
