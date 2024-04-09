import warnings

from src.graphs import *
from src.plot import plot_all_graphs, plot_critical_t
from src.tests import *
from src.config import *


def test_graphs():
    # RANDOM GRAPH WITH K
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    IG = get_information_graph(PG, VG, q=0.5)
    plot_all_graphs(PG, VG, IG)

    # RANDOM GRAPH WITH K*2
    kk = 2 * k
    prob_kk = kk / n_nodes
    PG, VG = random_graph_test(n_nodes, pPG=prob_kk, pVG=prob_kk)
    IG = get_information_graph(PG, VG, q=0.5)
    plot_all_graphs(PG, VG, IG)

    # CYCLE GRAPH
    PG, VG = cycle_graph_test(n_nodes)
    IG = get_information_graph(PG, VG, q=0.5)
    plot_all_graphs(PG, VG, IG)

    # SCALE FREE GRAPH WITH K
    PG, VG = scale_free_graph_test(n_nodes, mPG=prob_k, mVG=prob_k)
    IG = get_information_graph(PG, VG, q=0.5)
    plot_all_graphs(PG, VG, IG)


# TODO Test with different values of k and different number of nodes and initial infected
def mean_field_test():
    results = {}

    # RANDOM GRAPH WITH K = 6
    kk = 6
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    results[graph_type] = result

    # RANDOM GRAPH WITH K = 4
    kk = 4
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    results[graph_type] = result

    # RANDOM GRAPH WITH K = 2
    kk = 2
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    results[graph_type] = result

    # PLOT ALL RESULTS
    plot_critical_j(results, file=mean_field_jc_plot)


# TODO Test with different values of k and different number of nodes and initial infected
def simple_percolation_test():
    results = {}

    # RANDOM GRAPH WITH K
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    graph_type = "Poisson <k>=" + str(k)
    result = simple_tau_percolation_test(PG, iterations, ts)
    results[graph_type] = result

    # RANDOM GRAPH WITH K*2
    kk = 2 * k
    prob_kk = kk / n_nodes
    PG, VG = random_graph_test(n_nodes, pPG=prob_kk, pVG=prob_kk)
    graph_type = "Poisson <k>=" + str(kk)
    result = simple_tau_percolation_test(PG, iterations, ts)
    results[graph_type] = result

    # CYCLE GRAPH
    PG, VG = cycle_graph_test(n_nodes)
    graph_type = "Cycle"
    result = simple_tau_percolation_test(PG, iterations, ts)
    results[graph_type] = result

    # SCALE FREE GRAPH WITH K
    PG, VG = scale_free_graph_test(n_nodes, mPG=k, mVG=k)
    graph_type = "Scale Free <k>=" + str(k)
    result = simple_tau_percolation_test(PG, iterations, ts)
    results[graph_type] = result

    # PLOT ALL RESULTS
    plot_critical_t(results, file=critical_t_plot)


def percolation_test():
    results = {}

    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    # FIXME The percolation jc test and multiplex percolation is not working
    graph_type = "Poisson <k>=" + str(k)
    # percolation_jc_test(PG, iterations, ts, js)
    result = percolation_jc_test_2(PG, iterations, ts)
    results[graph_type] = result

    plot_critical_j(results, file=approx_plot_jc_plot, prediction=False)


def multiplex_percolation_test():
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    multiplex_percolation_jc_test(PG, VG, iterations, ts, qs)


def main():
    # Ignore warnings
    warnings.filterwarnings("ignore")

    # GRAPH TESTS
    # test_graphs()

    # TESTS
    mean_field_test()
    # simple_percolation_test()
    # percolation_test()
    # multiplex_percolation_test()


if __name__ == "__main__":
    main()
