import warnings

from src.graphs import *
from src.plot import plot_all_graphs, plot_critical_t
from src.save_csv import save_results
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


def mean_field_test():
    test = "MF/"
    results = {}

    # RANDOM GRAPH WITH K = 6
    kk = 6
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    path_test = "k-"+str(kk)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_j({graph_type: result}, file=test+path_test+".png")

    # RANDOM GRAPH WITH K = 4
    kk = 4
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    path_test = "k-"+str(kk)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_j({graph_type: result}, file=test+path_test+".png")

    # RANDOM GRAPH WITH K = 2
    kk = 2
    graph_type = "<k>=" + str(kk)
    result = mean_field_jc_test(kk, perc_init_infect, iterations, ts, js)
    path_test = "k-"+str(kk)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_j({graph_type: result}, file=test+path_test+".png")

    # PLOT ALL RESULTS
    plot_critical_j(results, file=test+mean_field_jc_plot)


def simple_percolation_test():
    test = "SIM/"+str(n_nodes)+"/"
    results = {}

    # RANDOM GRAPH WITH K
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    graph_type = "Poisson <k>=" + str(k)
    result = simple_tau_percolation_test(PG, iterations, ts)
    path_test = "Poisson-k-"+str(k)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_t({graph_type: result}, file=test+path_test+".png")

    # RANDOM GRAPH WITH K*2
    kk = 2 * k
    prob_kk = kk / n_nodes
    PG, VG = random_graph_test(n_nodes, pPG=prob_kk, pVG=prob_kk)
    graph_type = "Poisson <k>=" + str(kk)
    result = simple_tau_percolation_test(PG, iterations, ts)
    path_test = "Poisson-k-"+str(kk)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_t({graph_type: result}, file=test+path_test+".png")

    # CYCLE GRAPH
    PG, VG = cycle_graph_test(n_nodes)
    graph_type = "Cycle"
    result = simple_tau_percolation_test(PG, iterations, ts)
    path_test = "Cycle"
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_t({graph_type: result}, file=test+path_test+".png")

    # SCALE FREE GRAPH WITH K
    PG, VG = scale_free_graph_test(n_nodes, mPG=k, mVG=k)
    graph_type = "Scale Free <k>=" + str(k)
    result = simple_tau_percolation_test(PG, iterations, ts)
    path_test = "Scale_Free-k-"+str(k)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_critical_t({graph_type: result}, file=test+path_test+".png")

    # PLOT ALL RESULTS
    plot_critical_t(results, file=test+critical_t_plot)

# TODO With k = 6
def percolation_test():
    test = "PERC/Nodes_"+str(n_nodes)+"/Iteration_"+str(iterations)+"/"
    results = {}

    # RANDOM GRAPH WITH K
    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    graph_type = "Poisson <k>=" + str(k)
    result = risk_percolation_j_test(PG, iterations, ts)
    path_test = "Poisson-k-"+str(k)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_percolation_critical_j({graph_type: result}, file=test+path_test+".png")

    # CYCLE GRAPH
    PG, VG = cycle_graph_test(n_nodes)
    graph_type = "Cycle"
    result = risk_percolation_j_test(PG, iterations, ts)
    path_test = "Cycle"
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_percolation_critical_j({graph_type: result}, file=test+path_test+".png")

    # SCALE FREE GRAPH WITH K
    PG, VG = scale_free_graph_test(n_nodes, mPG=k, mVG=k)
    graph_type = "Scale Free <k>=" + str(k)
    result = risk_percolation_j_test(PG, iterations, ts)
    path_test = "Scale_Free-k-"+str(k)
    save_results(result, file=test+path_test+".csv")
    results[graph_type] = result
    plot_percolation_critical_j({graph_type: result}, file=test+path_test+".png")

    # PLOT ALL RESULTS
    plot_percolation_critical_j(results, file=test+graficoJC)


# TODO with k = 6
def multiplex_percolation_test():
    test = "MUL/Nodes_"+str(n_nodes)+"/Iteration_"+str(iterations)+"/"

    PG, VG = random_graph_test(n_nodes, pPG=prob_k, pVG=prob_k)
    graph_type = "Poisson <k>=" + str(k)
    results = multiplex_percolation_jc_test(PG, VG, iterations, ts, qs)
    path_test = "Poisson-k-"+str(k)
    save_results(results, file=test+path_test+".csv")
    plot_q_value(results, file=test+path_test+".png")

    PG, VG = cycle_graph_test(n_nodes)
    graph_type = "Cycle"
    results = multiplex_percolation_jc_test(PG, VG, iterations, ts, qs)
    path_test = "Cycle"
    save_results(results, file=test+path_test+".csv")
    plot_q_value(results, file=test+path_test+".png")

    PG, VG = scale_free_graph_test(n_nodes, mPG=k, mVG=k)
    graph_type = "Scale Free <k>=" + str(k)
    results = multiplex_percolation_jc_test(PG, VG, iterations, ts, qs)
    path_test = "Scale_Free-k-"+str(k)
    save_results(results, file=test+path_test+".csv")
    plot_q_value(results, file=test+path_test+".png")


def main():
    # Ignore warnings
    warnings.filterwarnings("ignore")

    # GRAPH TESTS
    # test_graphs()

    # TESTS
    # mean_field_test()
    # simple_percolation_test()
    # percolation_test()
    # multiplex_percolation_test()


if __name__ == "__main__":
    main()
