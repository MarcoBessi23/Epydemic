from src.graphs import *
from src.tests import *
from src.config import *


def main():
    # GRAPHS FOR TESTS
    # PG, VG, IG = cycle_graph_test()
    PG, VG, IG = random_graph_test(n_nodes, p=0.3, infected=init_infect)  # TODO: Check components graphs divided by zero
    # PG, VG, IG = scale_free_graph_test(nodes, m, 0.5, init_infect)
    # plot_all_graphs(PG, 0.2, 0.1)

    # TESTS
    # critical_j_test(PG, ts, js, rec_prob=rec_prob, immunity=immunity, plot=False)
    mean_field_critical_j_test(PG, init_infect, iterations, ts, js)
    not_approx_critical_j_test(PG, init_infect, iterations, ts, js)
    approx_critical_j_test(PG, init_infect, iterations, ts, js)


if __name__ == "__main__":
    main()
