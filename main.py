from src.graphs import *
from src.plot import plot_all_graphs
from src.tests import *
from src.config import *


def test_graphs():
    # GRAPHS FOR TESTS
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    # PG, VG = cycle_graph_test(n_nodes)
    # PG, VG = scale_free_graph_test(n_nodes, mPG=prob_m, mVG=prob_m)
    IG = get_information_graph(PG, VG, q=0.5)
    plot_all_graphs(PG, VG, IG)
    return PG, VG


def critical_j_test():
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    # critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=False)
    mean_field_jc_test(PG, perc_init_infect, iterations, ts, js)


def percolation_test():
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    # simple_tau_percolation_test(PG, iterations, ts)
    # FIXME The percolation jc test is not working
    percolation_jc_test(PG, iterations, ts, js)
    # multiplex_percolation_jc_test(PG, VG, iterations, ts, qs)


def main():
    # GRAPH TESTS
    # test_graphs()

    # TESTS
    # critical_j_test()
    percolation_test()


if __name__ == "__main__":
    main()
