from src.graphs import *
from src.tests import *
from src.config import *
from src.plot import plot_all_graphs

def main():
    # GRAPHS FOR TESTS
    # PG, VG, IG = cycle_graph_test()
    # TODO: Check components graphs divided by zero
    PG, VG, IG = random_graph_test(n_nodes, p=0.6, infected=init_infect)
    # PG, VG, IG = scale_free_graph_test(nodes, m, 0.5, init_infect)
    # plot_all_graphs(PG, VG, IG)

    # TESTS
    # critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=False)
    # mean_field_critical_j_test(PG, init_infect, iterations, ts, js)
    # percolation_critical_j_test(PG, iterations, ts, js)
    # simple_perc_test(PG, iterations, ts)
    multiplex_percolation_critical_j_test_test(PG, VG, iterations, ts, qs)


if __name__ == "__main__":
    main()
